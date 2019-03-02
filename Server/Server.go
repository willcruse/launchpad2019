package main

import (
	"bytes"
	"encoding/json"
	"fmt"
	"net/http"
	"strconv"
	"strings"
	"time"
)

type Weather struct {
	windspeed float64
	direction float64
	temp      float64
}

type Destination struct {
	lat  float64
	long float64
	name string
}

//Dates in format YYYY-MM-DD eg 2019-02-28
func main() {
	bath := Destination{
		51.3758,
		-2.3599,
		"Bath",
	}
	res := pullWeather([]string{"2019-03-03", "2019-03-06"}, bath)
	fmt.Printf("Windspeed: %.3f\tDirection %.3f\tTemp: %.3f\n", res[0].windspeed, res[0].direction, res[0].temp)
}

func pullWeather(date []string, dest Destination) []Weather {
	apiKey := "36785063bdf731228df7be0df5b5562c"
	reqString := fmt.Sprintf("http://api.openweathermap.org/data/2.5/forecast?lat=%f&lon=%f&appid=%s", dest.lat, dest.long, apiKey)
	req, err := http.Get(reqString)
	if err != nil {
		fmt.Println(err)
		return []Weather{Weather{
			-1,
			-1,
			-1,
		}}
	}
	buf := new(bytes.Buffer)
	buf.ReadFrom(req.Body)
	st := buf.String()
	var result map[string]interface{}
	result = make(map[string]interface{})
	err = json.Unmarshal([]byte(st), &result)
	if err != nil {
		fmt.Println(err)
		return []Weather{Weather{
			-1,
			-1,
			-1,
		}}
	}
	list := result["list"].([]interface{})
	from := findDay(float64(convertToUnix(date[0])), list)
	to := findDay(float64(convertToUnix(date[1])), list)
	if from == -1 || to == -1{
		fmt.Printf("No valid time\t%d\t%d\n", from, to)
		return []Weather{Weather{
			-1,
			-1,
			-1,
		}}
	}
	var final []Weather
	final = append(final, getWeatherStuff(list[from]))
	final = append(final, getWeatherStuff(list[to]))
	return final
}

func convertToUnix(date string) int64 {
	spl := strings.Split(date, "-")
	var intSpl [3]int
	for pos, val := range spl {
		var err error
		intSpl[pos], err = strconv.Atoi(val)
		if err != nil {
			fmt.Println(err)
			return -1.0
		}
	}
	location, err := time.LoadLocation("UTC")
	if err != nil {
		fmt.Println(err)
		return -1.0
	}
	unix := time.Date(intSpl[0], time.Month(intSpl[1]), intSpl[2], 12, 0, 0, 0, location)
	return unix.Unix()
}

func getWeatherStuff(obj interface{}) Weather {
	la := obj.(map[string]interface{})
	wind := la["wind"].(map[string]interface{})
	maiN := la["main"].(map[string]interface{})
	return Weather{
		wind["speed"].(float64),
		wind["deg"].(float64),
		maiN["temp"].(float64),
	}
}

func findDay(time float64, toSearch []interface{}) int {
	for pos, val := range toSearch {
		mapped := val.(map[string]interface{})
		tim := mapped["dt"]
		if tim.(float64)+43100 >= time && tim.(float64)-43100 <= time {
			return pos
		}
	}
	return -1
}

func typeof(v interface{}) string {
	return fmt.Sprintf("%T", v)
}
