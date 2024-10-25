

def login():
    Brugernavn= "Nexttech1"
    password= "3Dprint"


    userinput = input("hvad er dit brugernavn?\n")

    if userinput == Brugernavn:
        passInput = input("hvad er dit password?\n")
        if passInput == password:
            print("velkommen")
        else:
            print("Forkert password") 
            
                    
    else:
        print("Forkert brugernavn")
login()