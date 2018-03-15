s=''
def RLE(s):
    prev=''
    n=1
    l=[]
    for i in s:
        if i!=prev:
            if prev:
                if n!=1:
                    l.append(n)
                l.append(prev)
            n=1
            prev=i
        else:
            n+=1

    else:
        if n!=1:
            l.append(n)
        l.append(prev)

    return l
print(RLE('aaaabbceff'))
