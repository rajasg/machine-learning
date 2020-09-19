# matplotlib library is widely used to visualize data
from matplotlib import pyplot as plt

# GDP of Cambodia according to https://www.worldometers.info/gdp/cambodia-gdp/
years = [1994, 1996, 1998, 2000, 2002, 2004, 2006, 2008, 2010, 2012, 2014, 2016]
gdp = [2.8, 3.5, 3.1, 3.7, 4.3, 5.3, 7.3, 10.4, 11.2, 14.0, 16.7, 20.0]

# create a line chart, years on x-axis, gdp on y-axis
plt.plot(years, gdp, color='blue', marker='o', linestyle='solid')
plt.title("Nominal GDP of Cambodia") #add a title
plt.xlabel("Year") #add a xlabel
plt.ylabel("Billions of USD") #add a ylabel
plt.show()

