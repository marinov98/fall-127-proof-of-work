def check_for_letter(w):
    return (l for l in w if w.isalpha==True)
#print check_for+letter('hello')
def sorting_words(wordlist):
    d = collections.defaultdict(lambda: [])
    control = 0
    for w1, w2 in zip(word_list, word_list[1:]):
        d[w1].append(w2)
    return d
sorting_words
def file_letter_occurence(f):###Reads a full text from file and then returns a dictionary of all the letters and their occurence in it
    f = open(f).read()
    l = []
    for w.lower() in f.split():
        w = check_for_letter(w)
        l.append(w)
    d = file_letter_occurence(l)
    return d
