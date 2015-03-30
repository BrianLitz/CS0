cxv import random

def loadWord():
    
    ''' Populate each list with at least 10 different items.  Create a variable called secretWord that is assigned a random word from one of the lists. 
    
    return a tuple in the following format:  (secretWord, list the secretWord is from)   
    
    Hint:  You will need to randomly choose one of the lists, and THEN choose a random word from that list.
    '''
    persons = ['tom','collin','steve','eddie','mike','brian','bill','phillip','james','paul','spock','kirk','vader','elton','hank',]
    places = ['disney','ocala','tampa','massachuetts','portland','china','mexico','vegas','trinity','orlando']
    things = ['dog','cat','fish','hangman','computer','dinosaur','wrestling','suplex','microsoft','televison','starwars','xbox','wii']
    listOfLists = [persons,places,things]
    selectedList= random.choice(listOfLists)
    secretWord=random.choice(selectedList)
    hint=''
    
    if selectedList == persons:
        hint= 'person'
    elif selectedList ==places:
        hint = 'place'
    else:
        hint = 'thing'
    
    return(secretWord,hint)
     


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    
    for letter in secretWord:
        if letter not in lettersGuessed:
            return False
    return True
    



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    printWord = ''
    for letter in secretWord:
        if letter in lettersGuessed:
            printWord += letter + " "
        else:
            printWord += '_ '
    return printWord
    



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    lettersNotGuessed = ''
    alphabet = list(alphabet)
    for letter in lettersGuessed:
        alphabet.remove(letter)
    for letter in alphabet:
        lettersNotGuessed += letter + " "
    return lettersNotGuessed
    
def HangmanPic(wrongGuesses):
        hangmanPics = ['''
    +---+
    |   |
        |
        |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
        |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
    |   |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
   /|   |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
   /|\  |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
    =========''', '''
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
    ========='''] 
    
        return hangmanPics[wrongGuesses]

def hangman():
    '''
    secretWord: string, the secret word to guess.                                                                                                            

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    alphabet= 'abcdefghijklmnopqrstuvwxyz'
    wrongGuesses = 0    
    lettersGuessed = []
    loaded = loadWord()
    secretWord = loaded[0]
    hint = loaded[1]
    print "I'm thinking of a " + str(hint)
    while isWordGuessed(secretWord, lettersGuessed) != True:
        if wrongGuesses == 6:
            return "Game Over!" 
        else:
            
            guess = raw_input('Pick a letter:      ')
            
            while (guess not in alphabet or guess in lettersGuessed) or len(guess) != 1:
                guess = raw_input("Invalid guess.  Please pick an available letter from the English language:   ")
            if guess not in secretWord:
                wrongGuesses += 1
            lettersGuessed.append(guess)
            print getGuessedWord(secretWord, lettersGuessed)
            print getAvailableLetters(lettersGuessed)
            print "You have", 6- wrongGuesses, "left", HangmanPic(wrongGuesses)
            
    return "You Win, Live Long and Prosper"
    
    
        
        
    
    
    
           







