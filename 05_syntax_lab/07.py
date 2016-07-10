from random import randint 

mispar = randint(1,100)

while True:
    input = int (raw_input())
    if input > mispar:
        print "BIG"
    elif input < mispar:
        print  "SMALL"
    else:
        print "Exctaly"
        break
