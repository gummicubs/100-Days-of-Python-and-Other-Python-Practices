# Notes for grader: My notes are not indented into functions like the assignment instructions

from config import dictionaryloc
from config import turntextloc
from config import wheeltextloc
from config import maxrounds
from config import vowelcost
from config import roundstatusloc
from config import finalprize
from config import finalRoundTextLoc

import random

players={0:{"roundtotal":0,"gametotal":0,"name":""},
         1:{"roundtotal":0,"gametotal":0,"name":""},
         2:{"roundtotal":0,"gametotal":0,"name":""},
        }

roundNum = 0
# What is roundNum for?
dictionary = []
turntext = ""
wheellist = []
roundWord = ""
blankWord = []
vowels = {"a", "e", "i", "o", "u"}
roundstatus = ""
finalroundtext = ""

# Need to consider case sensitivity
# Need to consider no numbers
# Need to consider no repeated guesses
# Need to consider formatting blankword
# Need to check for only vowels left
# Need to check only one character is submitted


def readDictionaryFile():
    global dictionary
    with open(dictionaryloc, 'r') as f:
        dictionary = f.read().splitlines()
    # Read dictionary file in from dictionary file location
    # Store each word in a list.

   
def readTurnTxtFile():
    global turntext
    with open(turntextloc, 'r') as f:
        turntext = f.read()        
    #read in turn intial turn status "message" from file
       
def readFinalRoundTxtFile():
    global finalroundtext  
    with open(finalRoundTextLoc, 'r') as f:
        finalroundtext = f.read()
# format winner


def readRoundStatusTxtFile():
    global roundstatus
    with open(roundstatusloc, 'r') as f:
        roundstatus = f.read()
    # read the round status  the Config roundstatusloc file location
# format num, contestant1, money1, contestant2, money2, contestant3, money3

def readWheelTxtFile():
    global wheellist
    with open(wheeltextloc, 'r') as f:
        wheellist = f.read().splitlines()
    # read the Wheel name from input using the Config wheelloc file location
   
   
def getPlayerInfo():
    global players
    for key,values in players.items():
        players[key]['name'] = input(f'What is the name of our number {key+1} contestant?')
    # read in player names from command prompt input


def gameSetup():
    # Read in File dictionary
    # Read in Turn Text Files
    global turntext
    global dictionary

    readDictionaryFile()
    readTurnTxtFile()
    readWheelTxtFile()
    getPlayerInfo()
    readRoundStatusTxtFile()
    readFinalRoundTxtFile()
   
def getWord():
    global dictionary
    roundWord = random.choice(dictionary)
    roundUnderscoreWord = len(roundWord)*'_'
    # choose random word from dictionary
    # make a list of the word with underscores instead of letters.
    return roundWord.lower(),roundUnderscoreWord

def wofRoundSetup():
    global players
    global roundWord
    global blankWord
    # Set round total for each player = 0
    for key,values in players.items():
        players[key]['roundtotal']= 0
    # Return the starting player number (random)
    initPlayer = players[random.randint(0,2)]['name']
    # Use getWord function to retrieve the word and the underscore word (blankWord)
    (roundWord, blankWord)= getWord()
    return initPlayer


def spinWheel(playerNum):
    global wheellist
    global players
    global vowels
    # Get random value for wheellist
    outcome = random.choice(wheellist)
    # Check for bankrupcy, and take action.
    if outcome == 'BANKRUPT':
        print('You have landed on BANKRUPT! Your round total has dropped to 0.')
        players[playerNum]['roundtotal'] = 0
        stillinTurn = False
    # Check for loose turn
    elif outcome == 'LOSE A TURN':
        print('You lose your turn! Better luck next time.')
        stillinTurn = False
    # Get amount from wheel if not loose turn or bankruptcy
    else:
        outcome = int(outcome)
    # Ask user for letter guess
        letter = input(f'You get ${str(outcome)} for each time your guess is in the word. Please guess a consonant.')
        while letter in vowels:
            letter = input('That is not a consonant. Please guess a consonant.')
# ensure letter is a consonate.
    # Use guessletter function to see if guess is in word, and return count
        (stillinTurn, count) = guessletter(letter)
    # Change player round total if they guess right.
        if count > 0:
            players[playerNum]['roundtotal'] += count*outcome
# Player gets value * count
    return stillinTurn



def guessletter(letter):
    global players
    global blankWord
    # parameters:  take in a letter guess and player number
# Removed playerNum parameter
    # ensure letter is a consonate.
# Does not check for consonent. Checks for consonent in spin wheel for reusability of function for vowels.
    count = 0
    new_blank = ''
    goodGuess = False
    for i in range(len(roundWord)):
        if roundWord[i] == letter:
            new_blank += letter
            count +=1
    # return count of letters in word.
            goodGuess = True
        else:
             new_blank += blankWord[i]
    print(f'{letter} shows up in our word {count} times.')          
    # Change position of found letter in blankWord to the letter instead of underscore
    # return goodGuess= true if it was a correct guess
    blankWord = new_blank
    print(f'Our updated clue is now: {blankWord}')
    return goodGuess, count
# Why do I need playnum?



def buyVowel(playerNum):
    global players
    global vowels
    # Take in a player number
    # Ensure player has 250 for buying a vowelcost
#found in stillinturn function. Removes option if too poor
    # Ensure letter is a vowel
    letter = input('What vowel would you like to buy?')
    while letter not in vowels:
        letter = input('That is not a vowel. What vowel would you like to buy?')
    # Use guessLetter function to see if the letter is in the file
    goodGuess = guessletter(letter)[0]
    # If letter is in the file let goodGuess = True
# Need to update players
    players[playerNum]['roundtotal'] -= vowelcost
    return goodGuess          



def guessWord(playerNum):
    global players
    global blankWord
    global roundWord
    # Take in player number
    # Ask for input of the word and check if it is the same as wordguess
    word = input('Guess the word.')
    # Fill in blankList with all letters, instead of underscores if correct
    if word == roundWord:
        blankWord = roundWord
        print('Congratulations! You\'ve won this round!')
    else:
        print('Unfortunately, that is not the word but good try!')
    # return False ( to indicate the turn will finish)  
    return False
   
   
def wofTurn(playerNum):  
    global roundWord
    global blankWord
    global turntext
    global players

    # take in a player number.
    # use the string.format method to output your status for the round
    choice = input(turntext.format(contestant = players[playerNum]['name'], money = players[playerNum]['roundtotal']))
# Needs formatting contestant, money
    # and Ask to (s)pin the wheel, (b)uy vowel, or G(uess) the word using
    # Keep doing all turn activity for a player until they guess wrong
    # Do all turn related activity including update roundtotal    
    stillinTurn = True
    turn = 1
    while stillinTurn:        
        # use the string.format method to output your status for the round
        # Get user input S for spin, B for buy a vowel, G for guess the word
        if turn >1:
            choice = input('What would you like to do next?')    
# Only want this to show after first turn        
        if(choice.strip().upper() == "S"):
            stillinTurn = spinWheel(playerNum)
        elif(choice.strip().lower() == 'b'):
            if players[playerNum]['roundtotal'] < vowelcost:
                print('You do not have enough to buy a vowel. Please choose a different option.')
            else:
                stillinTurn = buyVowel(playerNum)
        elif(choice.upper() == "G"):
            stillinTurn = guessWord(playerNum)
        else:
            print("Not a correct option. Please choose one of the three given options")
        turn +=1

   
        if blankWord == roundWord:
            stillinTurn = False
            print(f"The word has been solved by {players[playerNum]['name']}!")
            players[playerNum]['gametotal'] += players[playerNum]['roundtotal']
    
    # Check to see if the word is solved, and return false if it is,
    # Or otherwise break the while loop of the turn.


def wofRound(nm):
    global players
    global roundWord
    global blankWord
    global roundstatus
    initPlayer = wofRoundSetup()
    for i in range(3):
        if players[i]['name'] == initPlayer:
            playerNum = i
    
    print(f"Let's get started with Round {str(nm)}. \n")
    print(f'Your clue is: {blankWord}.')
    print('The first player is chosen at random.')
    
    stillinRound = True
    # Keep doing things in a round until the round is done ( word is solved)
    while stillinRound:
        if '_' not in blankWord:
            stillinRound = False
        else:
            if playerNum > 2:
                playerNum -= 3
            wofTurn(playerNum)
            if '_' in blankWord:
                playerNum +=1
        # While still in the round keep rotating through players
        # Use the wofTurn fuction to dive into each players turn until their turn is done.
    
    # Print roundstatus with string.format, tell people the state of the round as you are leaving a round.
    print(roundstatus.format(num = str(nm), contestant1 = players[0]['name'], contestant2 = players[1]['name'], contestant3 = players[2]['name'],
                             money1 = str(players[0]['gametotal']), money2 = str(players[1]['gametotal']), money3 = str(players[2]['gametotal'])))
# format num, contestant1, money1, contestant2, money2, contestant3, money3


def wofFinalRound():
    global roundWord
    global blankWord
    global finalroundtext
#     winplayer = 0
# Why default winner to first contestant?
    # amount = 10000
# What is amount for?
    # Find highest gametotal player.  They are playing.
    score = []
    for key, value in players.items():
        score.append(players[key]['gametotal'])
    winplayer = score.index(max(score))
    # Print out instructions for that player and who the player is.
    print(finalroundtext.format(winner = players[winplayer]['name']))
    # Use the getWord function to reset the roundWord and the blankWord ( word with the underscores)
    (roundWord, blankWord) = getWord()
    # Use the guessletter function to check for {'R','S','T','L','N','E'}
    for letter in ['r', 's', 't', 'l', 'n', 'e']:
        guessletter(letter)
    # Print out the current blankWord with whats in it after applying {'R','S','T','L','N','E'}
    # Gather 3 consonats and 1 vowel and use the guessletter function to see if they are in the word
    guesses = input('Please guess 3 consonants and 1 vowel. Do not include spaces or commas in between.')
    Guesses = [x for x in guesses]
    for guess in Guesses:
        guessletter(guess)
    # Print out the current blankWord again
    print(blankWord)
    # Remember guessletter should fill in the letters with the positions in blankWord
    # Get user to guess word
    word = input('Please guess the word.')
    if word == roundWord:
        players[winplayer]['gametotal'] += finalprize
        print(f"You've guessed correctly! Your grand total is {players[winplayer]['gametotal']}!")
    else:
        print(f"Unforunately, that is not the correct word. The word is {roundWord}.")
    # If they do, add finalprize and gametotal and print out that the player won


def main():
    gameSetup()    

    for i in range(0,maxrounds):
        if i in [0,1]:
            wofRound(i+1)
        else:
            wofFinalRound()

if __name__ == "__main__":
    main()