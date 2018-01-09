def ladybug():
  g=int
  strg=1
  b=str()
  while strg<=g:
    n=int(input())
    b=input().strip()
    if n==2 and b[1]==b[0]and b[1]!='_':
      print('Yes!')
    elif n<2:
      print('No!)
    elif '_' not in b:
      for i in range(1,len(b)-1):
        if b[i]!=b[i+1] or b[i]!=b[i-1]:
            print('No!')
    totallady={}
    valbug=list(totallady.values())
    for lady in b:
      totallady.setdefault(lady,0)
      totallady[lady]+=1
    if valbug.count(1)==0:
      print('Yes!')
    else:
      print('No!')
    srtg+=1
ladybug()
