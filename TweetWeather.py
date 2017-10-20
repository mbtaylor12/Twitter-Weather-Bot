from weather import Weather

#city can be zip code or city, state
city = ""
#TOKEN, TOKEN_KEY, CON_SEC, CON_SEC_KEY can all be found on your Twitter Application Page
TOKEN = ""
TOKEN_KEY = ""
CON_SEC = ""
CON_SEC_KEY = ""

def sendTweet(message):
	print "done"

def getWeather():
	weather = Weather()


	location = weather.lookup_by_location(city)
	condition = location.condition()
	region = location.location()

	return "It is currently " + condition['text'] + " and " + condition['temp'] + " Degrees Fahrenheit in " + region['city'] + "," + region['region']

if __name__ == '__main__':
        print getWeather()
        sendTweet("hi")
        print 'completed'

