from random import randint

one = randint(1,10)
two = randint(1,10)

for i in range(1,  (one * two)+1) :
    if ((i % one == 0) and (i % two == 0)) :
        print i
        break

print one,two
    
