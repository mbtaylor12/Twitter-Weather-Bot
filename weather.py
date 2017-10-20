from weather import Weather

weather = Weather()

location = weather.lookup_by_location('24141')
condition = location.condition()

print("It is currently " + condition['text'] + " and " + condition['temp'] + " Degrees Fahrenheit in Radford, VA.")