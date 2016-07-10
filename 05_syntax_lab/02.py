from random import randint
    
sum = 0
for x in range(1,7) :
    num = randint(1,100)
    sum += num

print sum
if (sum % 7) == 0 :
    print "BOOM"