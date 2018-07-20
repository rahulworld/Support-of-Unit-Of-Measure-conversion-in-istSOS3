# -*- coding: utf-8 -*-
lookups = {
    "°C":["°C", "celcius", "degree Celsius", "degree-celsius", "degree-celsius", "degree", "degree centigrade", "degcelsius", "degC"],
    "°F":["°F", "fahrenheit", "degfahrenheit", "degF", "degfahrenheit", "degree-fahrenheit", "degree fahrenheit"],
    "°K":["°K", "kelvin", "degK", "tempK"],
     }


class LookUpTable(object):
	def findLookUp(self, unit):
		for key, value in lookups.items():
		    if str(unit).lower() in value:
		        return key

def findLookUp1(unit="celcius"):
	for key, value in lookups.items():
	    if unit in value:
	        return key.encode('utf-8')
# a=LookUpTable()
print('hello world')
print(findLookUp1("degF"))