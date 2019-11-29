#import the function from collections library
from collections import Counter as c

#sample object
namelist = ['mike','john', 'gary','mike','john', 'mike']


print(c(namelist))

print(c(namelist).items())

print(c(namelist).most_common(2))

#Set the 2 most values and their counts to a lit of touples
popularNames = c(namelist).most_common(2)
print(popularNames)



#requires integer counters
#








