from weather import Weather
import datetime

#city can be zip code or city, state
city = "24141"
#TOKEN, TOKEN_KEY, CON_SEC, CON_SEC_KEY can all be found on your Twitter Application Page
TOKEN = ""
TOKEN_KEY = ""
CON_SEC = ""
CON_SEC_KEY = ""

def sendTweet(message):
	print "done"

def getWeather():
	weather = Weather()
	now = datetime.datetime.now()

	location = weather.lookup_by_location(city)
	condition = location.condition()
	region = location.location()

	currentTime = now.strftime("%H:%M %m/%d/%Y")

	return "It is currently " + condition['text'] + " and " + condition['temp'] + " Degrees Fahrenheit in " + region['city'] + "," + region['region'] + " at " + currentTime

if __name__ == '__main__':
        print getWeather()
        sendTweet("hi")
        print 'completed'

