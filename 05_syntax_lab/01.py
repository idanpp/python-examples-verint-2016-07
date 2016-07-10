
print "Please choose Number"
x = int(raw_input())

for number in range(1,10) :
    print "choose agian"
    num = int(raw_input())
    x = max(num,x)

print "Highes number is" ,x