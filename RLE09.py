#Run length encoding is a form of compression that is sometimes used for images or other data that's repetitive.
#In run length encoding, repeated sequences of values are replaced with a count and a single value.
#We are going to use run length encoding to encode a string into a list.
#For example, the string "aaaaa" would encode to [5, 'a'] since a appears 5 times.
#The string "bbaaa" would encode to [2,'b',3,'a'] since b occurs twice and a once.
#A single letter just gets encoded as is without a count so the string "aabcccdeeeeaaa" encodes to
#[2,'a',b,3,'c',d,4,'e',3,'a'].
#Write a routine encode(s) which will
#run length encode the string s as specified above
s=''
def RLE(s):
    prev=''
    n=1
    l=[]
    for i in s:
        if i!=prev:
            if prev:
                entry=n,prev
                l.append(entry)
            n=1
            prev= i
        else:
            n+=1
    else:
        entry=n,i
        l.append(entry)
    return l
