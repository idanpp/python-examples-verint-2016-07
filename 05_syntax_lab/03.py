from random import randint

sum = 0

num = randint(1,10000)
print num 
while num > 0 :
    diggit = num % 10 
    sum = sum + diggit
    num = num / 10 
print sum