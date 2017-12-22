import pyowm
from make_rus import make_rus_stat

owm = pyowm.OWM('YOUR_API_KEY')

def ret_data(output):
	observation = owm.weather_at_place(output)
	w = observation.get_weather()
	status = w.get_status()
	temp =  w.get_temperature(unit='celsius')
	sttr=make_rus_stat(status)+'\n '+str(temp['temp'])+' Celsius'
	return sttr
