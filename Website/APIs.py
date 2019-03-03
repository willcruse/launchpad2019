import requests
import datetime

class destination:
    def __init__(self, pos, name, airport):
        self.pos = pos
        self.name = name
        self.airport = airport



class weather:
    def __init__(self):
        self.windspeed = [-1, -1]
        self.direction = [-1, -1]
        self.temp = [-1, -1]
        self.day = [-1, -1]

    def __str__(self):
        return "Windspeed: " + str(self.windspeed) + "   Direction: " + str(self.direction) + "   Temp: " + str(self.temp) + " Day: " + str(self.day)

    def convertToUnix(self, dt):
        start = datetime.date(1970, 1, 1)
        return int((dt-start).total_seconds())

    def findDay(self, time, lis):
        count = 0
        for i in lis:
            if i["dt"]+43100 >= time and i["dt"]-43100 <= time:
                return count
            count += 1
        return -1

    def pullWeather(self, dates, dest):
        self.day = dates
        apiKey = "36785063bdf731228df7be0df5b5562c"
        reqString = "http://api.openweathermap.org/data/2.5/forecast?lat=" + \
            str(dest.pos[0]) + "&lon=" + str(dest.pos[1]) + "&appid=" + apiKey
        req = requests.get(reqString)
        result = req.json()
        lis = result["list"]
        for k in range(2):
            fro = self.findDay(self.convertToUnix(dates), lis)
            self.windspeed[k] = lis[fro]["wind"]["speed"]
            self.direction[k] = lis[fro]["wind"]["deg"]
            self.temp[k] = lis[fro]["main"]["temp"]


class flight:

    def __init__(self):
        self.price = 150
        self.timeLeave = 1000
        self.timeArrive = 1200
        self.dest = "SID"
        self.fro = "LGW"
        self.company = "Tap Air Portugal"
