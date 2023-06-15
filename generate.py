import random


countries = {'Russia': 1, 'Spain': 1, 'Italy': 1, 'Germany': 1, 'France': 1, 'England': 1}
fcs = {'FC Moscow': 1, 'FC Sochi': 1, 'FC St. Petersburg': 1, 'Barcelona FC': 1, 'Athletic Bilbao': 1, 'Valencia CF': 1, 'AS Roma': 1, 'Juventus FC': 1, 'AC Milan': 1, 'FC Bayern Munich': 1, 'Borussia Dortmund': 1, 'FC Schalke 04': 1, 'Paris Saint Germain': 1, 'Olympique Marseille': 1, 'AS Monaco': 1, 'Manchester United': 1, 'Liverpool FC': 1, 'Arsenal FC': 1, 'FC Rostov': 1, 'FC Ufa': 1, 'FC Ural': 1, 'Real Madrid CF': 1, 'Atletico Madrid': 1, 'Sevilla FC': 1, 'Inter Milan': 1, 'SS Lazio': 1, 'Cagliari Calcio': 1, 'Bayer 04 Leverkusen': 1, 'TSG 1899 Hoffenheim': 1, 'VfL Wolfsburg': 1, 'Olympique Lyon': 1, 'Stade Rennais': 1, 'Stade de Reims': 1, 'Chelsea FC': 1, 'Manchester City': 1, 'Tottenham Hotspur': 1, 'FC Krasnodar': 1, 'FC Tambov': 1, 'FC Orenburg': 1, 'RCD Mallorca': 1, 'Getafe CF': 1, 'RC Celta de Vigo': 1, 'US Sassuolo': 1, 'Benevento Calcio': 1, 'SPAL 2013': 1, 'FC Augsburg': 1, 'FSV Mainz 05': 1, 'SC Freiburg': 1, 'Stade Brestois': 1, 'FC Metz': 1, 'FC Lorient': 1, 'Leicester City': 1, 'Sheffield United': 1, 'West Ham United': 1, '1. FC Köln': 1, 'Aston Villa': 1, 'Real Betis': 1, 'Real Sociedad': 1}
city = {'Moscow': 1, 'Sochi': 1, 'St. Petersburg': 1, 'Barcelona': 1, 'Bilbao': 1, 'Valencia': 1, 'Rome': 1, 'Turin': 1, 'Milan': 1, 'Munich': 1, 'Dortmund': 1, 'Gelsenkirchen': 1, 'Paris': 1, 'Marseille': 1, 'Monaco': 1, 'Manchester': 1, 'Liverpool': 1, 'London': 1, 'Rostov': 1, 'Ufa': 1, 'Yekaterinburg': 1, 'Madrid': 1, 'Seville': 1, 'Cagliari': 1, 'Leverkusen': 1, 'Hoffenheim': 1, 'Wolfsburg': 1, 'Lyon': 1, 'Rennes': 1, 'Reims': 1, 'Krasnodar': 1, 'Tambov': 1, 'Orenburg': 1, 'Palma de Mallorca': 1, 'Getafe': 1, 'Vigo': 1, 'Sassuolo': 1, 'Benevento': 1, 'Ferrara': 1, 'Augsburg': 1, 'Mainz': 1, 'Freiburg': 1, 'Brest': 1, 'Metz': 1, 'Lorient': 1, 'Leicester': 1, 'Sheffield': 1, 'Cologne': 1, 'Birmingham': 1, 'San Sebastian': 1}
year = [1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]
name = {'John Smith': 1, 'James Johnson': 1, 'Adam Williams': 1, 'Norman White': 1, 'Thomas Brown': 1, 'Brian Miller': 1, 'Paul Davis': 1, 'George Wilson': 1, 'Mark Anderson': 1, 'Steven Taylor': 1, 'Joseph Evans': 1, 'Michael Thompson': 1, 'David King': 1, 'Richard Walker': 1, 'William Robinson': 1, 'Kenneth Hall': 1, 'Matthew Nelson': 1, 'Kevin Campbell': 1, 'Carl Taylor': 1, 'Jeffrey Adams': 1, 'Thomas Edwards': 1, 'Matthew Baker': 1, 'Nicholas Moore': 1, 'Edward Phillips': 1, 'Joshua Miller': 1, 'John Lewis': 1, 'Albert Gonzalez': 1, 'David James': 1, 'William Moore': 1, 'Joseph Perez': 1, 'Ronald Wilson': 1, 'Richard White': 1, 'Christopher Taylor': 1, 'Timothy Harris': 1, 'Brian Walker': 1, 'Andrew Clark': 1}
point = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]

AMOUNT = 25000
f = open(f"ds_{AMOUNT}.csv", "w")
for i in range(AMOUNT):
    f.write(f"{random.choice(list(countries))},{random.choice(list(fcs))},{random.choice(list(city))},{random.choice(year)},{random.choice(list(name))},{random.choice(point)}\n")

f.close()