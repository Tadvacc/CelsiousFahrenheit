#Problem: convert Celsius temperatures to Fahrenheit

#Input: a possibly empty list of temperatures in Celsius
celsius_values = [28, 33, 29, 32, 27]

#Output: the list of temperatures in Fahrenheit
fahrenheit_values = []

for celsius in celsius_values:
    fahrenheit = celsius * 1.8 + 32
    fahrenheit_values = fahrenheit_values + [fahrenheit]
    
print ('The temperatures in fahrenheit are', fahrenheit_values)
