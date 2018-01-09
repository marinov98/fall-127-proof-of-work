C=['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'X', 'Z','W','Y']
V=['A','E','O','I','U']
def piglatin(word):
    if word[0].upper()in C:
        return word[1:]+word[0].lower()+"ay"
    if word[0].upper()in V:
        return word+"ay"
def inout():
    word=''
    while word!='endit':
        print('type any word to be translated to piglatin. Type endit to stop')
        word=input()
        print(piglatin(word))
inout()

