##Write a program named bondify.py. It should assign a string to a
##2. variable on the first line. The string will be in the form
##3. "Firstname Lastname"; so for example it could be "James Bond"; Note
##4. that there is no period in the string but grammar rules dictate
###5. that the punctuation ALWAYS goes in the quotes and I can't
##6. break the habit. The program will make a new string that
##7. transforrms the original into something in the form: "Lastname,
##8. Firstname Lastname" or in the example case "Bond, James Bond" This
##9. should work for any string value.
def bondify():
    Firstname=''
    while Firstname!='nobody':
        print("Who am I? What is my first name")
        Firstname=input()
        print("and what is my last name?")
        Lastname=input()
        print("Oh I see... I am",Lastname,",",Firstname, Lastname,",","How could I forget")
bondify()
