# Do not modify these lines
__winc_id__ = 'd0d3cdcefbb54bc980f443c04ab3a9eb'
__human_name__ = 'operators'

# Add your code after this line
#1 The language spoken the most in Switzerland is the same as in Spain.

switz_lang = "German(or Swiss German)"
spain_lang = "Castilian Spanish"
print(switz_lang == spain_lang)

#2 The most prevalent religion in Switzerland is the same as in Spain.
switz_religion = "Roman Catholic"
spain_religion = "Roman Catholic"
print(switz_religion == spain_religion)

#3 The name length of Spain's capital does not equal that of Switzerland.
switz_capital = "Bern"
spain_capital = "Madrid"
print(len(spain_capital) != len(switz_capital))

#4 Switzerland's GDP is greater than Spain's GDP.
switz_gdp = 580 * 10 * 9
spain_gdp = 1778 * 10 * 9
print(switz_gdp > spain_gdp)

#5 The population growth is less than 1% in Switzerland and Spain.
switz_popgrowth = 0.0066
spain_popgrowth = 0.0067
print(spain_popgrowth < 0.01 and switz_popgrowth < 0.01)

#6 At least one of the two countries has a population count of over 10 million.
ten_million = 10 ** 7

switz_popcount = 8.4 * 10 ** 6
spain_popcount = 50 * 10 ** 6
print(spain_popcount > ten_million or switz_popcount > ten_million)

#7 Exactly one of the two countries has a population count of over 10 million.

switz_popcount = 8.4 * 10 ** 6
spain_popcount = 50 * 10 ** 6
print((spain_popcount > ten_million and switz_popcount <= ten_million)
or (switz_popcount <= ten_million and switz_popcount > ten_million))