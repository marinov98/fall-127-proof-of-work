l = []
def fizzbuzz(start, end):
    for i in range(start, end + 1):
        s = ''
        if i%3 == 0:
            s += "fizz"
        if i%5 == 0:
            s += "buzz"
        if (i%3 != 0 and i%5 != 0):
            s += str(i)
        l.append(s)
 
    for z in l:
        print(z)
    
print(fizzbuzz(1, 50))
