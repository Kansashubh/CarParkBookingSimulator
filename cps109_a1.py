#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time

"""
Problem Description:
    Imagine you are driving to visit a city but in the downtown area where parking becomes super tough and you exhaust energy in parking your vehicle because you have to look for places and find parking. 
In addition, you have to pay for the parking after arriving at that place which altogether delays your time of parking due to understanding the terms and conditions that the car parking area has for its customers. 
This is why I am building an online platform which allows you to book your parking through payment and vehicle information provided by the user through the online platform. 
This online platform corresponds to online parking booking for a particular business and the aim is to allow customers to travel to their destination without worrying about their parking issues. 
This is because as soon as they arrive at their desired destination, they can simply park without any hassle and freely travel. 
The car parking center is open 24/7. 

    So this platform will ask the user for their name and license plate, car type. 
Then it will ask for the customer's choice on whether they pick to do valet parking or not and it will give the terms and conditions for parking. 
After it will provide the user with parking options/costs, ask the user to input hours that the car will be parked for and tip percentage they would like to give. 
Later, cost will be calculated and the customer will be asked to give their card information (Give random card information because this is just a test application, it is not supposed to be real). 
Lastly, the platform will thank them for their time. 
"""
# This is the major variable that checks if the customer has verified their parking spot
paymentdone = False
# A while loop will be developed to check if the condition has been satisfied
while paymentdone == False:
    checkvalidityoffirstname = False
    # Getting user input of first name and also checking validity
    while checkvalidityoffirstname != True:
        firstname = input("Type your first name (All Characters must be alphabetic and no spaces):")
        counterofvalidcharacters = 0
        # Using a for loop to check if number of valid characters
        for i in range(len(firstname)):
            if firstname[i].isalpha() == True:
                counterofvalidcharacters += 1
            else:
                continue
        if counterofvalidcharacters == len(firstname):
            checkvalidityoffirstname = True
        else:
            print("Invalid Input")           
            # Keeping space between lines
            print("")    
    # This will allow me to skip lines when I am asking the next question
    print("--------------------------------------------------------------")   
    checkingvalidityoflastname = False
    # Getting user input of last name and also checking validity
    while checkingvalidityoflastname != True:
        lastname = input("Type your last name (All Characters must be alphabetic and no spaces):")
        counterofvalidcharacterslast = 0
        # Using a for loop to check number of valid characters
        for i in range(len(lastname)):
            if lastname[i].isalpha() == True:
                counterofvalidcharacterslast += 1
            else:
                continue
        if counterofvalidcharacterslast == len(lastname):
            checkingvalidityoflastname = True
        else:
            print("Invalid Input")
            # Keeping space between lines
            print("")    
    print("-------------------------------------------------------------")    
    lplatevalidity = False
    # Getting user input of liscence plate and also checking validity
    while lplatevalidity != True:
        lplate = input("Type your liscence plate (All characters must be uppercase letters or numbers and no spaces):")
        lplatecounter = 0
        # Using a for loop to check number of valid characters
        for i in range(len(lplate)):
            if lplate[i].isalpha() == True and lplate.isupper() == True:
                lplatecounter += 1
            elif lplate[i].isnumeric() == True:
                lplatecounter += 1
            else:
                continue
        if lplatecounter == len(lplate):
            lplatevalidity = True
        else:
            print("Invalid Input")
            # Keeping space between lines
            print("")        
    print("------------------------------------------------------------")     
    ctypevalidity = False
    # Getting user input of cartype and checking its validity
    while ctypevalidity != True:
        # Reading a text file line by line 
        with open("ctype.txt", "r") as file:
            for option in file:
                print(option)
        # Using error handling to make sure user inputs a string that can be converted to a number
        try:
            ctypechoice = int(input("Pick a car type by typing the number option in brackets before the car type:"))
            if ctypechoice >= 1 and ctypechoice <= 12:
                ctypevalidity = True
            else:
                time.sleep(2)
                print("Invalid Input")                
        except Exception as e:
            time.sleep(2)
            print("Invalid Input")                       
    print("----------------------------------------------------------")
            
    ptypevalidity = False
    
    # Describing what Valet Parking is
    print("Valet Parking is when your car gets parked for you")
    # Getting user input of parking type and checking its validity
    while ptypevalidity != True:
        # Reading a text file line by line
        with open("ParkingType.txt", "r") as file:
            for option in file:
                print(option)
        # Using error handling to make sure user inputs a string that can be converted to a number
        try:
            ptypechoice = int(input("Pick a car parking type by typing the number option in brackets before the car type: "))
            if ptypechoice >= 1 and ptypechoice <= 2:
                ptypevalidity = True
            else:
                time.sleep(2)
                print("Invalid Input")
                
        except Exception as e:
            time.sleep(2)
            print("Invalid Input")
    print("---------------------------------------------------------")
    
    useragree = False
    # Getting the user to read the terms and conditions and assking them to agree on it
    while useragree != True:
        print("After paying an confirming parking user has three hours to cancel their confirmation, otherwise we cannot refund")
        time.sleep(2)
        print("For the given time you select, your car must be parked for that duration or else it will be towed")
        time.sleep(2)
        print("Property of our parking lot is under video surveilance 24/7")
        time.sleep(2)
        print("We are open from 6am in the morning to 9pm in the night so you can park car for maximum of 15 hours")
        time.sleep(2)
        print("If your car is left in the parking lot after the time of closing then we tow the car")
        time.sleep(2)
        print("When you confirm your booking you pay an initial fee of $15 for registration")
        time.sleep(2)       
        userconfirmation = input("To confirm that you agree type the sentence exactly type the word Yes:    ")
        if userconfirmation == "Yes":
            useragree = True
        else:        
            time.sleep(2)
            print("You did not follow the instructions")
            time.sleep(2)          
    print("--------------------------------------------------------")  
    optionselection = False
    # Getting the user to pick a parking option that would select their cost
    while optionselection != True:
        # Reading a text file line by line
        with open("ParkingOptions.txt", "r") as file:
            for option in file:
                print(option)
        # Using error handling to make sure input is done properly
        try:
            cchoice = int(input("Which option would you like to select, type the number corresponding to option:"))
            if cchoice >= 1 and cchoice <= 3:
                optionselection = True
                print("Regardless the number of hours you park, suppose you park between 0 to 4 hours and 59 mins, your price will be adjusted on the basis of option 1")
                time.sleep(2)
                print("Regardless the number of hours you park, suppose you park between 5 to 9 hours and 59 mins, your price will be adjusted on the basis of option 2")
                time.sleep(2)
                print("Regardless the number of hours you park, suppose you park between 10 to 14 hours and 59 mins, your price will be adjusted on the basis of option 3")
                time.sleep(2)                
            else:
                print("Invalid Input")
                time.sleep(2)
                
        except Exception as e:
            print("Invalid Input")
            time.sleep(2)             
    print("--------------------------------------------------------------")         
    timeinputvalid = False
    # Getting user input of number hours and checking validity
    while timeinputvalid != True:
        try:
            tchoice = float(input("Type in number of hours you would like to park car for: "))
            if tchoice >= 0 and tchoice <= 15:
                if tchoice >= 0.0 and tchoice < 5.0:
                    cchoice = 1
                    timeinputvalid = True
                elif tchoice >= 5.0 and tchoice < 10.0:
                    cchoice = 2
                    timeinputvalid = True
                else:
                    cchoice = 3
                    timeinputvalid = True
            else:
                print("Hours is out of range")              
        except Exception as e:
            print("Invalid Input")
            time.sleep(2)           
    print("-------------------------------------------------------------")       
    tippercentvalid = False
    # Getting user tip percent and checking if input is valid
    while tippercentvalid != True:
        try:
            print("How much tip would you like to give")
            percent = float(input("Just type the percentage number and dont put percentage sign in your input: "))
            if percent >= 0.0 and percent <= 100.0:
                tippercentvalid = True
            else:
                print("Percentage is between 0 to 100")
                time.sleep(2)              
        except Exception as e:
            print("Invalid input")
            time.sleep(2)          
    print("-------------------------------------------------------------")  
    # Calculating cost
    # Tax will be calculated as if it is 13%
    def cost(tchoice, percent, cchoice):
        originalcost = 0
        Tipadjustedcost = 0
        Taxadjustedcost = 0
        finalcost = 0
        if cchoice == 1:
            originalcost = (tchoice * 10 + 15)
            Tipadjustedcost = ((originalcost) * (percent / 100)) + (originalcost)
            Taxadjustedcost = (Tipadjustedcost * 0.13) + Tipadjustedcost
        elif cchoice == 2:
            # First finding cost excluding tax and substracting the discounted percent
            originalcost = (tchoice * 10 + 15) - ((tchoice * 10 + 15) * 0.15) 
            # Then adding tip
            Tipadjustedcost = ((originalcost) * (percent / 100)) + (originalcost)
            # Lastly adding the tax
            Taxadjustedcost = (Tipadjustedcost * 0.13) + Tipadjustedcost
        else:
            # Fist finding cost by excluding cost and substracting the discounted amount
            originalcost = (tchoice * 10 + 15) - ((tchoice * 10 + 15) * 0.30)
            # Then adding tip
            Tipadjustedcost = ((originalcost) * (percent / 100)) + (originalcost)
            # Lastly adding the tax
            Taxadjustedcost = (Tipadjustedcost * 0.13) + Tipadjustedcost
        finalcost = round(Taxadjustedcost,2)
        return finalcost         
    value = cost(tchoice, percent, cchoice)   
    print("The cost will be: ", value, " dollars")  
    print("------------------------------------------------------------")
    cardtypepicked = False
    # Getting user to select between card options
    while cardtypepicked != True:
        # Reading a text file line by line
        with open("CardType.txt", "r") as file:
            for option in file:
                print(option)
        try:
            cardtype = int(input("Pick a card type by selecting one of the options above: "))
            if cardtype >= 0 and cardtype <= 4:
                cardtypepicked = True
            else:
                print("Option number is out of range")
                time.sleep(2)
        except Exception as e:
            print("Invalid input")
            time.sleep(2)     
    print("--------------------------------------------------------------")
    cardnumbervalidity = False
    # Passing in card number and checking its validity based on input type
    while cardnumbervalidity != True:
        try:            
            print("Card Number")
            num = int(input("Number must be 15 to 20 digits: "))
            if len(str(num)) >= 15 and len(str(num)) <= 20:
                cardnumbervalidity = True
            else:
                print("Incorrect number of digits")
        except Exception as e:
            print("Invalid Input")
            time.sleep(2)          
    print("--------------------------------------------------------------") 
    cardexpvalidity = False
    # Passing in card number and checking its validity based on input type
    while cardexpvalidity != True:
         try:        
             print("Card Expiry")
             mm = int(input("number must be between 1 and 12 (This is for month number): "))
             yyyy = int(input("number must be 4 digits, so type the year number (Year has to be after 2024): "))
             if (mm >= 1 and mm <= 12) and (len(str(yyyy)) <= 4) and yyyy >= 2024:
                 cardexpvalidity = True
             else:
                 print("Incorrect number of digits for month or year")
         except Exception as e:
             print("Invalid Input")
             time.sleep(2)          
    print("---------------------------------------------------------------")
    cardsecurityvalidity = False
    # Passing in card number and checking its validity based on input type
    while cardsecurityvalidity != True:
         try:            
             print("Security Code")
             security = int(input("Type your 3 digit code: "))
             if len(str(security)) == 3:
                 cardsecurityvalidity = True
                 paymentdone = True
             else:
                 print("Incorrect number of digits security number")
         except Exception as e:
             print("Invalid Input")
             time.sleep(2) 
             
print("Thank you for filling up the information, ",firstname)
            
        
    
        
        
        
            
    
        
        
        
        


