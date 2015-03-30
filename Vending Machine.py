#   on function call, print out message asking user to select drink or snack
#      Then, print appropriate choices depending on user input
#       check if payment is enough
#       check if choice is correct
#       if so, return change, choice

def vendingMachine(money):
    drinkList = ["Sprite","Coke","Water"]
    snackList = ["Oreos","Popcorn","Chips"]
    
    userChoice = raw_input("Drinks are $1.50.  Snacks are $1.75.  Press 1 for drinks, or 2 for snacks:    ")
    while userChoice != 1 or userChoice != 2:
        userChoice = raw_input("That is not a valid choice.  Please enter 1 for drinks, or 2 for snacks:    ")
    if userChoice == 1:
        print "Drink Choices:  " + str(drinkList)
        drinkChoice = raw_input("Please enter your drink choice:   ")
        drinkChoice = drinkChoice.lower()
        while drinkChoice not in drinkList:
            drinkChoice = raw_input("Please select a valid drink choice from the drink list: \n   " + str(drinkList)  )
    elif userChoice == 2:
        print "Snack Choices:  " + str(snackList)
        snackChoice = raw_input("Please enter your snack choice:   ")
        snackChoice = snackChoice.lower()
        while snackChoice not in snackList:
            snackChoice = raw_input("Please select a valid snack choice from the snack list: \n   " + str(snackList)  )
    
             
    
        
    
    




def Drink(Choice,Stock):
    drinks = ["Sprite","Coke","Water"]
    elif Choice == "Sprite" or Choice == "Water":
        print "1.50" 
    elif Choice== "Coke":
        print "Out of Stock, Try Again"
def Snack(SnackChoice,SnackStock):
    snacks = ["Oreos","Popcorn","Chips"]s
    elif SnackChoice == "Chips" or SnackChoice == " Popcorn":
        print "1.75"
    elif SnackChoice == "Oreos":
        print "No More Oreos!, Eat an Apple!"


                