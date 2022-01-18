from statistics import mean

print("Swallow Speed Analysis: Version 1.0")        #headline printed
new_list = []                                       #empty list created
reading = input("Enter the Next Reading: ")         #reading taken

#condition to check the reading
if reading == "":                                   
    print("No reading entered. Nothing to do.")
else:
    #input data type checked
    while reading:                                  
        if reading[0].upper() == "U":                
            print("Reading saved")
            new_list.append(float(reading[1:])*1.61) 
            reading = input("Enter next reading:")   
        elif reading[0].upper() == "E":
            print("Reading saved")
            new_list.append(float(reading[1:]))
            reading = input("Enter the Next Reading: ")
        else:
            break
        #if the data list is not empty then maximum and minimum printed  
    if (len(new_list)!= 0):
        print("\nResults Summary\n")
        print(len(new_list),"Reading Analysed.")
        print(f"Max Speed: {max(new_list)/1.61:.1f} MPH,  {max(new_list):.1f} KPH")
        print(f"Min Speed: {min(new_list)/1.61:.1f} MPH,  {min(new_list):.1f} KPH")

        average_mean = mean(new_list) 
        print (f"Avg Speed: {(average_mean/1.61):.1f} MPH,  {average_mean:.1f} KPH.")
        #when the data is invalid below syntax is run
    else:
        print("Invalid")