# START
from random import random
from time import sleep
from IPython.display import clear_output

import os

difficultyPreset = [
    [2, 0.3, 3, 2],
    [4, 0.5, 5, 1],
    [5, 1, 5, 0.5],
    [1, 0.5, 1, 0.1]
]

score = 0
mistakes = 0
highestDigitRemembered = 0 

def getRandomNumber(numOfDigits):
    return f"{int(random()*(pow(10, numOfDigits))):{0}{numOfDigits}}"
def clearDisplay():
    clear_output()
    os.system('cls' if os.name == 'nt' else 'clear')

def startNewRound(preset):
    global score
    global mistakes
    global highestDigitRemembered
    digitCountFloat = preset[0]
    digitIncrementPerRound = preset[1]
    timeInterval = preset[2]
    timeIncrementPerRound = preset[3]

    clearDisplay()

    number = getRandomNumber(round(digitCountFloat))
    print(number)
    print("-"*len(number))
    if (score): print("Score:", score)
    if (mistakes): print("Mistakes:", f"{mistakes}/3")
    sleep(timeInterval)

    clearDisplay()
    playerNumber = input("> Enter The Number: ")
    clearDisplay()

    if (number == playerNumber):
        print("(*) Correct! Proceeding to next question...")
        score += 1
        highestDigitRemembered = round(digitCountFloat)
        sleep(2)
    else:
        print("(*) Oops. That's incorrect.")
        print("Number         :", number)
        print("Your Number    :", playerNumber)
        mistakes += 1
        sleep(7)
    clearDisplay()

    if (mistakes >= 3):
        difficulty = ["Easy", "Medium", "Hard", "Challenge"][presetIndex] 
        print("(!) Game Over!")
        print("Score:", score)
        print("Difficulty:", difficulty)
        print("Highest No. Of Digits Remembered:", highestDigitRemembered)
        return
    
    preset[0] = digitCountFloat + digitIncrementPerRound
    preset[2] = timeInterval + timeIncrementPerRound
    startNewRound(preset)

print("======\n[MEMO]\n======") 
input("> Start Game? (quit anytime by using CTRL+D): ")
presetIndex = int(input("> Choose Difficulty Number (1:easy, 2:medium, 3:hard, 4:challenge): "))-1
startNewRound(difficultyPreset[presetIndex])