from weather import Weather
import twitter
import datetime

#CITY can be zip code or city, state
CITY = ""
#TOKEN, TOKEN_KEY, CON_SEC, CON_SEC_KEY can all be found on your Twitter Application Page
TOKEN = ""
TOKEN_KEY = ""
CON_SEC = ""
CON_SEC_KEY = ""

def getWeather():

	try:
		weather = Weather()
		now = datetime.datetime.now()

		location = weather.lookup_by_location(CITY)
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

	try:
		my_account.statuses.update(status=tweet)
		tweetStatus = "Successfully tweeted."
	except Exception,e:
		print str(e)
		tweetStatus = "Unable to send tweet."

	print tweetStatus

if __name__ == '__main__':
    if "Error" not in getWeather():
    	sendTweet(getWeather())
    print 'completed'

