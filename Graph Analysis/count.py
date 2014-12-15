ac1 = "Miami,Lebanon,Boston,Fremont,Buffalo,Kingston,Fort Valley,Fort Valley,York,Pleasant Hill,New Tazewell,Miamisburg,Tampa,Santa Ana,New York,Las Vegas,Colorado Springs,Mount Morris,New York,Osseo,Clinton,Providence,Pompano Beach,Florence,Carmel,Brooklyn,Naples,New York,Saint Paul,"
ac2 = "Warsaw,Providence,Kingston,Fremont,Florence,Lockport,New York,New York,Pleasant Hill,Las Vegas,"
ac3 = "Kingston,Pleasant Hill,Cathedral City,Osseo,New Tazewell,Miamisburg,Tampa,Lakewood,Mount Morris,Santa Ana,New York,Aiken,Las Vegas,Colorado Springs,Lebanon,Fremont,Minoa,New York,Buffalo,Chatham,Ironton,Phoenixville,Pompano Beach,San Rafael,Florence,Fort Valley,Carmel,Brooklyn,Naples,Westfield,Revere,Fairfield,Taunton,Warsaw,New York,New York,Saint Paul,"
ac4 = "New Tazewell,Miamisburg,Tampa,Lakewood,Santa Ana,Las Vegas,Colorado Springs,New York,Fremont,New York,Kingston,Buffalo,Osseo,Chatham,Bloomfield,Pompano Beach,York,Fort Valley,Brooklyn,Naples,Westfield,Mount Morris,Florence,Lebanon,Taunton,Warsaw,New York,New Orleans,Pleasant Hill,"
ac5 = "Providence,Kingston,Lockport,Florence,New York,New York,Naples,Round Lake,Pleasant Hill,Arlington Heights,Las Vegas"

acceptedcities = ac1 + ac2 + ac3 + ac4 + ac5

cities = {}

#count the cities where results were accepted from
for city in acceptedcities.split(','):
	if city in cities.keys():
		cities[city] += 1
	else:
		cities[city] = 1

#print in the requied google graph format
for city in cities:
	print "['" + city + "', " + (str) (cities[city]) + "],"
