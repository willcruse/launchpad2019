import requests
import datetime

class destination:
    def __init__(self, pos, name, airport):
        self.pos = pos
        self.name = name
        self.airport = airport
    destinations = [
      destination([16.538799, -23.041800], "Cape Verde", "SID"),
      destination([-6.135730, 39.362122], "Zanzibar", "ZNZ"),
      destination([-3.682650, -38.737560], "Cumbuco, Brazil", "FOR"),
      destination([-28.016666, 153.399994], "Gold Coast, Australia", "OOL")
    ]


class weather:
    def __init__(self):
        self.windspeed = [-1, -1]
        self.direction = [-1, -1]
        self.temp = [-1, -1]
        self.day = [-1, -1]

    def __str__(self):
        return "Windspeed: " + str(self.windspeed) + "   Direction: " + str(self.direction) + "   Temp: " + str(self.temp) + " Day: " + str(self.day)

    def convertToUnix(self, dt):
        start = datetime.datetime(1970, 1, 1, 0)
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
            str(dest[0]) + "&lon=" + str(dest[1]) + "&appid=" + apiKey
        req = requests.get(reqString)
        result = req.json()
        lis = result["list"]
        for k in range(2):
            spl = [int(i) for i in dates[k].split("-")]
            fro = self.findDay(self.convertToUnix(
                datetime.datetime(spl[0], spl[1], spl[2], hour=12)), lis)
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

    flights = [
  flight(150, 1000, 1200, "SID", "LGW", "Tap Air Portugal", "2019-04-23"),
  flight(160, 800, 1600, "ZNZ", "LHR", "British Airways", "2019-04-23"),
  flight(170, 900, 1500, "FOR", "STN", "KLM", "2019-04-23"),
  flight(180, 1700, 2100, "OOL", "LHR", "British Airways", "2019-04-23")
  flight(150, 1000, 1200, "LGW", "SID", "Tap Air Portugal", "2019-04-23"),
  flight(160, 800, 1600, "LHR", "ZNZ", "British Airways", "2019-04-23"),
  flight(170, 900, 1500, "STN", "FOR", "KLM", "2019-04-23"),
  flight(180, 1700, 2100, "LHR", "OOL", "British Airways", "2019-04-23")
  ]
