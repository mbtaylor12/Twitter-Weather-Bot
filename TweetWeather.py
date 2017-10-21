"""
TweetWeather.py
Tweets the current weather conditions from any city on any Twitter Account.
Just plug in your information.
"""
from weather import Weather
import twitter
import datetime

#CITY can be zip code or city, state
CITY = ""
#TOKEN, TOKEN_KEY, CON_SEC, CON_SEC_KEY are Twitter app keys.
#They can all be found on your Twitter Application Page.
TOKEN=""
TOKEN_KEY=""
CON_SEC=""
CON_SEC_KEY=""
def getWeather():
	"""Returns the current weather conditions.
	"""
	try:
		weather = Weather()
		now = datetime.datetime.now()

		location = weather.lookup_by_location(CITY)
		condition = location.condition()
		region = location.location()

		currentTime = now.strftime("%H:%M %m/%d/%Y")

		message = "It is currently " + condition['text'] + " and " + \
			condition['temp'] + " Degrees Fahrenheit in #" + region['city'] \
			+ " ," + region['region'] + " at " + currentTime + " #Weather"

	except Exception,e:
		print str(e)
		message = "Error getting weather."

	return message

def sendTweet(tweet):
	"""Tries to tweet your tweet.
	:param tweet: The message to be tweeted.
	"""
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
	tweet = getWeather()

	if "Error" not in tweet:
		sendTweet(tweet)

	print 'completed'