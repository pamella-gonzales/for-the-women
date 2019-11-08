#If statements and comments exercise

year = 1830


if year <2000:
	print ("You are before the 21st century!")
elif year >=2000 and year <=2100:
	print ("Welcome to the 21st century!")
else:
	print ("You are after the 21st century!")


birthyear = 2002
name = "Jasmine"

if birthyear <2000:
	print ("You are born before the 21st century!")
elif birthyear >=2000 and birthyear <=2100:
	print ("You are born on {}, {}. Welcome to the 21st century!".format (birthyear,name))
else:
	print ("You are born after the 21st century!")