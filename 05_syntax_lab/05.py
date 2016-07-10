from random import randint

while True:
    num = randint(1,1000000)
    if num % 7 == 0:
        if num % 13 == 0:
            if num % 15 == 0:
                 print num
                 break;
