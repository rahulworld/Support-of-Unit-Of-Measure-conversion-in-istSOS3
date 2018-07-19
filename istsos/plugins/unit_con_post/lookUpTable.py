lookups = {
    "°C":["°C", "celcius", "degree Celsius", "degree-celsius", "degree-celsius", "degree", "degree centigrade", "degcelsius", "degC"],
    "°F":["°F", "fahrenheit", "degfahrenheit", "degF", "degfahrenheit", "degree-fahrenheit", "degree fahrenheit"],
    "°K":["°K", "kelvin", "degK", "tempK"],
    "°K":["°K", "kelvin", "degK", "tempK"],
    "°K":["°K", "kelvin", "degK", "tempK"],
     }


class LookUpTable():
 	def findLookUp(self, unit):
 		for key, value in lookups.items():
            if str(unit).lower() in value:
                return key