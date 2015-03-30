def vendingMachineChange(amount,cost):
    return amount - cost 
    
    
    

    
    
    
def vendingMachine(money):    
    drinkList = ["sprite","coke","water"]
    snackList = ["oreos","popcorn","chips"]
    
    userChoice = int(raw_input("Drinks are $1.50.  Snacks are $1.75.  Press 1 for drinks, or 2 for snacks:    "))
    while not (userChoice == 1 or userChoice == 2):
        userChoice = int(raw_input("That is not a valid choice.  Please enter 1 for drinks, or 2 for snacks:    "))
    if money >= 1.50:
        if userChoice == 1:
            drinkChoice =""
            while drinkChoice not in drinkList:
                print str(drinkList)
                drinkChoice = raw_input("Please select a valid drink choice from the drink list: \n   "   )
                print "Drink Choices:  " + str(drinkList)
                drinkChoice = drinkChoice.lower()
    elif money >=1.75:
        if userChoice == 2: 
            snackChoice=""
            while snackChoice not in snackList:
                print str(snackList)
                snackChoice = raw_input("Please select a valid snack choice from the drink list: \n  "  )
                print "Snack Choices:  " + str(snackList)
                snackChoice = snackChoice.lower()
            

           
def vend(money, choice):
     drinkList = ['a', 'b', 'c']
     if money >= 1.50:
         if choice in drinkList:
             return (choice,money - 1.5)
         else:
             return ('invalid choice', money)
     else: 
         return ("not enough money", money)           
        
            