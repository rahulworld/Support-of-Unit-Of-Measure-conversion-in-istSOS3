# -*- coding: utf-8 -*-
lookups = {
    "°C":["°C", "celcius", "degree Celsius", "degree-celsius", "degree-celsius", "degree", "degree centigrade", "degcelsius", "degC"],
    "°F":["°F", "fahrenheit", "degfahrenheit", "degF", "degfahrenheit", "degree-fahrenheit", "degree fahrenheit"],
    "°K":["°K", "kelvin", "degK", "tempK"],
     }


class LookUpTable(object):
	def findLookUp(self, unit):
		for key, value in lookups.items():
		    if str(unit).lower() in (n.lower() for n in value):
		        return key


a=LookUpTable()
print('hello world')
print(a.findLookUp("degF"))
# print(findLookUp1("degF"))