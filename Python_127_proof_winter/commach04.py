##Comma code problem chapter 4
#Say you have a list value like this:
#spam = ['apples', 'bananas', 'tofu', 'cats']
#Write a function that takes a list value as an argument and returns
#a string with all the items separated by a comma and a space, with and
#inserted before the last item. For example, passing the previous spam list to
#the function would return 'apples, bananas, tofu, and cats'. But your function should be able
#to work with any list value passed to it.
spam=['Beckham','Rooney','Ronaldo','Messi','Neymar']
def Comma(spam):
    n=''
    for i in spam[0:-1]:
        n+=i+','
    return n+'and'+' '+spam[-1]
Comma(spam)

