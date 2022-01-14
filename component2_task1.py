print("Stop! Who would cross the Bridge of Death\nMust answer me these questions three, 'ere the other side he see.")

name=input("What is your name? ")       #Ask the passer-by's name
name=name.upper()                       

if "ARTHUR" in name:                    #If King Arthur passes, he is allowed to pass
    print("My liege! You may pass!")    
else:
    quest=input("What do you seek? ")    #If it is not King Arthur who passes, he is asked more questions
    quest=quest.upper()
    if "GRAIL" not in quest:            #If he does not seek the Grail, he is denied access
        print("Only those who seek the Grail may pass!")    
    else:                                 
        colour=input("What is your favourite colour? ")  #If the Knight does not know his favourite colour, he has to face the Gorge of Eternal  Peril
        colour=colour.upper()
        if name[0]==colour[0]:      #The Knight's favourite colour should start with the first letter of his name
            print("You may pass!")  #If the answer is correct, he is allowed to pass
        else:
            print("Wrong! Now you must face the Gorge of Eternal Peril!")