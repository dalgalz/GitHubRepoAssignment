#1. What query would you run to get all the countries that speak Slovene?
#Your query should return the name of the country, language and language percentage.
#Your query should arrange the result by language percentage in descending order. (1)
#select * from countries;
#select * from languages;
#select countries.name, languages.language, languages.percentage from countries join languages
#on countries.code = languages.country_code where language = 'Slovene' order by percentage desc;

#2. What query would you run to display the total number of cities for each country?
#Your query should return the name of the country and the total number of cities.
#Your query should arrange the result by the number of cities in descending order. (3)
select countries.code, SUM(cities.name) as TotalOfCities from countries join cities
on countries.code = cities.country_code
group by countries.code order by countries.code desc limit 100;
#select * from cities;