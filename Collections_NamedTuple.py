#import the function from collections library
#This is similar to creating a class

from collections import namedtuple

Dog = namedtuple('Dog', 'breed, age, color')
coco = Dog(breed = 'mix', age = 4, color ='brown')

print(coco.age)