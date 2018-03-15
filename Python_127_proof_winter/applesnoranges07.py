#When a fruit falls from its tree, it lands  units of distance from its tree of origin along the -axis.
# A negative value of  means the fruit fell  units to the tree's left, and
#a positive value of  means it falls  units to the tree's right.
#Given the value of  for  apples and  oranges,
#can you determine how many apples and oranges will fall on Sam's house (i.e., in the inclusive range )?
#Print the number of apples that fall on Sam's house as your first line of output,
#then print the number of oranges that fall on Sam's house as your second line of output.
#Input Format
#The first line contains two space-separated integers denoting the respective values of  and .
#The second line contains two space-separated integers denoting the respective values of  and .
#The third line contains two space-separated integers denoting the respective values of  and .
#The fourth line contains  space-separated integers denoting the respective distances that each apple falls from point .
#The fifth line contains  space-separated integers denoting the respective distances that each orange falls from point .
#Constraints
#Output Format
#Print two lines of output:
#On the first line, print the number of apples that fall on Sam's house.
#On the second line, print the number of oranges that fall on Sam's house.
#Sample Input 0
#7 11
#5 15
#3 2
#-2 2 1
#5 -6
#Sample Output
#1
#1
def fruitree():
    totalapple=0
    totalorange=0
    print("mark the start and end points of Sam's house")
    s,t=input().split(' ')
    s=int(s)
    t=int(t)
    print('what are the endpoints of the apple tree located?')
    a,b=input().split(' ')
    a=int(a)
    b=int(b)
    print('Almost there. Write the number of apples and oranges')
    m,n=input().split(' ')
    m=int(m)
    n=int(n)
    print('Final steps. write the position of the apples')
    arange=[int(arange) for arange in input().split(' ')]
    print('Now write the position of the oranges')
    orrange=[int(orrange) for orrange in input().split(' ')]
    for i in arange:
        if s<=i+a<=t:
            totalapple+=1
    for z in orrange:
        if s<=z+b<=t:
            totalorange+=1
    print(totalapple)
    print(totalorange)
fruitree()
