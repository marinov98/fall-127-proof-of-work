b=str()
def ladybug(b):
    print('how many games do you want to play?')
    g=int(input())
    srtg=1

    while srtg<=g:
        print('how many cells with there be on the board')
        n=int(input())
        print("what colors will you be using? Use '_' to indicate an empty cell")
        b=input().strip()
        if n==2 and  b[1]==b[0] and b[1]!='_':
            print('YES!')
        elif n<2:
            print('No!')
        elif '_' not in b:
            for i in range(1,len(b)-1):
                if b[i]!=b[i+1] or b[i]!=b[i-1]:
                    print('No!')
        totallady = {}
        valbug = list(totallady.values())
        for lady in b:
            totallady.setdefault(lady,0)
            totallady[lady]+=1
        if valbug.count(1) == 0:
                print('Yes!')
        else:
                print('NO!')

        srtg+=1
ladybug(b)
