def isLetterInWord(secretword):
    guess = raw_input("Please guess a letter:   ")
    alphabet='abcdefghijklmnopqrstuvwxyz'
    secretWord= secretWord.lower()
    guess = guess.lower()
    
    while len(guess) !=1:
            guess = raw_input("Please pick Only One Letter!:   ")
    while guess not in alphabet:
        guess = raw_input("PLease make sure you pick a letter: ")
    if guess in secretword:
        return True
    else:
        return False