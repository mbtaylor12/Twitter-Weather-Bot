from weather import Weather
import twitter
import datetime

#city can be zip code or city, state
city = ""
#TOKEN, TOKEN_KEY, CON_SEC, CON_SEC_KEY can all be found on your Twitter Application Page
TOKEN = ""
TOKEN_KEY = ""
CON_SEC = ""
CON_SEC_KEY = ""

def getWeather():

	try:
		weather = Weather()
		now = datetime.datetime.now()

		location = weather.lookup_by_location(city)
		condition = location.condition()
		region = location.location()

		currentTime = now.strftime("%H:%M %m/%d/%Y")

		message = "It is currently " + condition['text'] + " and " + condition['temp'] + " Degrees Fahrenheit in #" + region['city'] + " ," + region['region'] + " at " + currentTime + " #Weather"
	except Exception,e:
		print str(e)
		message = "Error getting weather."

	return message

def sendTweet(tweet):
	my_auth = twitter.OAuth(TOKEN,TOKEN_KEY,CON_SEC,CON_SEC_KEY)
	my_account = twitter.Twitter(auth=my_auth)
	my_account.statuses.update(status=tweet)

	print "done"

if __name__ == '__main__':
    print getWeather()
    #sendTweet(getWeather())
    print 'completed'

