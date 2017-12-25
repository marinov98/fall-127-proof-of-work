##Do the Collatz problem at the end of chapter 3 in the text
##Write a function named collatz() that has one parameter named number .
#If number is even, then collatz() should print number // 2 and return this value.
#If number is odd, then collatz() should print and return 3 * number + 1.
#Then write a program that lets the user type in an integer and that keeps calling collatz() on that number until the function returns the value 1 .
#(Amazingly enough, this sequence actually works for any integer—sooner or later, using this sequence, you’ll arrive at 1!
#Even mathematicians aren’t sure why.
#Your program is exploring what’s called the Collatz sequence, some- times called “the simplest impossible math problem.”)
#Remember to convert the return value from input() to an integer with the int() function;
#otherwise, it will be a string value.
#Hint: An integer number is even if number % 2 == 0 ,
#it’s odd if number % 2 == 1 .
#The output of this program could look something like this:
#Enter number:
#3
#10
#5
#16
#8
#4
#2
#1
def Collatz():
    print("give me any number and watch it go to 1 ahaha!")
    number=int(input())
    while number!=0:
        if number==1:
            break
        if number % 2 == 0:
            print(number // 2)
            number=number//2
            continue
        if number % 2 ==1:
            print(3*number+1)
            number=number*3+1
            continue
        return list.append(number)
Collatz()

