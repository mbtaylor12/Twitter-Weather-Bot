from weather import Weather

#city can be zip code or city, state
city = ""

def sendTweet(TOKEN, TOKEN_KEY, CON_SEC, CON_SEC_KEY, message):
	print "message"

def getWeather(location):
	weather = Weather()


	location = weather.lookup_by_location(location)
	condition = location.condition()
	region = location.location()
	#date = location.results()

	return "It is currently " + condition['text'] + " and " + condition['temp'] + " Degrees Fahrenheit in " + region['city'] + "," + region['region']

if __name__ == '__main__':
        print getWeather(city)
        print 'completed'

