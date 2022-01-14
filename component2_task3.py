from random import choice
print("Welcome to PopChat\nOne of our operators will be pleased to help you today")
help_user = ["Shubhash","Arogya","Dipeshwar","Shahzaha"]        #List of help_user operators
net_error = ["b","b","b","b","b","c","b","b","b","b"]           #List to check for network error

email = input("Please enter your Poppleton email address: ")    #Input email from user
count = 0

valid = False
if "@" in email:            #If "@" is in email, then only the email is valid
    e = email.split("@")    #Split function to split the part before and after the "@"
    count = 0               #count variable to count the number of cahracters before "@"
    for i in e[0]:          #for loop to extract characters before "@"
        count += 1          #Count value increased by 1 for each character

        #If the part before "@" has two or more characters and the domain is correct, then only email is valid
        if count >=2 and e[1] == "pop.ac.uk":
            valid = True

            operator = choice(help_user)        #Pick any operator from the help_user list
            probability = choice(net_error)     #Pick any number from net_error list


            print("Hi,",e[0].capitalize(),"! Thank you, and welcome to PopChat!")
            print("My name is",operator,", and it will be my pleasure to help you.")

            if probability == "c":              #Situation for network error and exit, only sometimes
                print("*** NETWORK ERROR ***")
                print("Thanks,",e[0].capitalize(),"for using PopChat. See you soon!")
                exit()

            #while loop executes only when the email is valid
            while True:
                #request to ask for what user wants
                request = input("---> ")
                request = request.upper()
                #If request does not match any of the services available, an item from wrong is displayed
                wrong = ["Hmmmm","Tell me more about it","I didn't understand","What do you mean?","Can you repeat it?","Oh yes I see"]
                #If user wants to exit the chat service, an item from stop must be entered
                stop = ["EXIT","QUIT","STOP","END","GOODBYE","BYE"]
                #Any reply from wrong may be displayed
                reply = choice(wrong)
                if "WIFI" in request:
                    print("The wifi is excellent around campus.")
                elif "LIBRARY" in request:
                    print("The library is closed today.")
                elif "DEADLINE" in request:
                    print("Your deadline has been increase by two days.")
                elif "FOOD" in request:
                    print("The cafe is on the ground floor.")
                elif "RESTROOM" in request:
                    print("The washroom is around the corner of each floor.")
                elif "LABORATORY" in request:
                    print("The laboratory is on the 4th floor.")
                else:
            #If the request matches any of the one in stop, then service will stop
                    for j in stop:
                        if j in request.upper():
                            print("Thanks,",e[0].capitalize(),"for using PopChat. See you soon!")
                            exit()
                    else:
                        print(reply)
    else:
        #If the email domain doesn't match the requirement, it is invalid
        print("Email is invalid")      
else:
    #If the email doesn't contact "@", then it is invalid
    print("Email is invalid")           
    exit()
