#use in distance formula
#ord() convert character to ascii number ex. ord('a')= 97
#chr()conver ascii number to character  ex chr(97)= 'a'
#65-90 correspond to uppercase letters , 97-122 correspond to lowercase letters
#convert the letter to ascii number, rotate it, and then convert back to letter
import math

real_stats = [0.08167,0.01492,0.02782,0.04253,0.12702,0.02228,0.02015,0.06094,0.06966,0.00153,0.00772,0.04025,0.02406,0.06749,0.07507,0.01929,0.00095,0.05987,0.06327,0.09056,0.02758,0.00978,0.02360,0.00150,0.01974,0.00074]

def encode_letter(c,r):#one letter encoding
    if ord(c) <= 90:#uppercase
        anum=ord(c)+r
        if anum > 90:
            anum=(anum % 90)+ 65
    else:#lowercase
        if ord(c)<=122:
            anum=ord(c)+r
        if anum > 122:
            anum=(anum % 122) + 97
    letter = chr(anum)
    return letter
#print(encode_letter('A',3))
#print(encode_letter('a',3))
#print(encode_letter('Z',5))
#print(encode_letter('z',5))
def encode_string(s,r):##encoding a string of letters
    astring=''
    for i in s:
        if (65<=ord(i)<=90) or (97<=ord(i)<=122):
            astring+=encode_letter(i,r)
        else:
            astring+=i
    return astring
#print(encode_string('AAAC',3))
#print(encode_string('aaabbvd',3))
#print(encode_string('WWWZZZY',5))
#print(encode_string('ZZzzvu',5))
def full_encode(s):#all possible rotations of a string of letters!!! ***include newline
    n=''
    for i in range(27):
        n+=encode_string(s,i)+'/n'
    n=n.strip('/n')
    return n
#print(full_encode('aaab'))
#print(full_encode('AAAB'))
#print(full_encode('ZZZY'))
#print(full_encode('It is done!'))
def distance(l1,l2):#Eclidean distance formulat between two lists, the closer they are, the more SIMILIAR they are
    length=len(l1)
    if len(l1)>len(l2):
        length=len(l2)
    sum=0
    for i in range(length):
       sum = sum+((l1[i]-l2[i])**2)
           d = math.sqrt(sum)
     return d
 #l1=[1,5,7]
 #l2=[16,4,3]
#################################
def build_frequency_vector(s):
#count the letters in the string
#count each letter to see how many times it appears.
    spaces = s.count(' ')
    num_letters = len(s) - spaces
    v = []
    for letter in "abcdefghijklmnopqrstuvwxyz":
        v.append(s.count(letter) / num_letters)
    return v
def print_vector_table(v):
  s = "abcdefghijklmnopqrstuvwxyz"
  for i in range(26):
            print(s[i], " : ", v[i])
 ###############################################
def build_vect_list(s):
    for i in range(0, 26):
        freq_vect_list.append(build_frequency_vector(encodeList[i]))
#############################################################
freq_vect_list = []
sentence='It will never be over until you say it is over and you give up mentally. Remember shame lies not in failure but in refusing to rise back up.'
def decode(s):#does the inverse of full_encode
    lst=[]
    for y in range(27):
        lst.append(encode_string(s,y))
        build_frequency_list(s)
        i=0
        for z in range(27):
            if distance_form(freq_vect_list[i], stat) < distance_form(freq_vect_list[index], stat):
                i = z
        return encode_string(s,i)
    #print(decode(sentence))
