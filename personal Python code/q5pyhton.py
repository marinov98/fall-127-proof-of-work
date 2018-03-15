def eosum():
    even_sum=0
    odd_sum=0
    count1=0
    count2=0
    l=[]
    number=int()
    while number != -1:
        number=int(input())
        if number!=-1:
            l.append(number)
    for i in range(len(l)):
        if i % 2 == 0:
            even_sum+=l[i]
            count1+=1
        if i % 2 == 1:
            odd_sum+=l[i]
            count2+=1
    print ("the even sum is: ",even_sum)
    print ("even average is: ",(even_sum/count1))
    print ("the odd sum is: ",odd_sum)
    print ("the odd average is: ",(odd_sum/count2))

eosum()
