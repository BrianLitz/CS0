def vendingMachine(money,choice): 
    ''' Enters arguement money and choice , choice must come from vendlsit.
    If not from vendlist returns money
    if from vendlist but not enough money return money
    If choice is right return money and choice''' 
    vendlist = ['oreos','popcorn','apples', 'coke', 'sprite','water']
   
    if money >= 1.45:
        if choice in vendlist:
            return (money-1.45 , choice)
        else:
            return ('Choice is wrong!',money)
    else:
        return ('Not enough money', money)
    if money == 1.45:
        return ('Here You Go!', money - 1.45) 
        
        
                
    