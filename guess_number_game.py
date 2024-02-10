import sys
import random

minNum = int(input("Please input MIN number?"))
maxNum = int(input("Please input MAX number?"))
if (minNum >= maxNum):
    print("MIN number must be lower than the MAX number.")
else:
    targetNum = random.randint(minNum, maxNum)
    print(targetNum)
    guessNum = int(input("Please guess target number?"))
    while(guessNum != targetNum):
        if (guessNum > targetNum):
            guessNum = int(input(f"Your guess: {guessNum} is higher than the target. Please try it again?"))
        elif (guessNum < targetNum):
            guessNum = int(input(f"Your guess: {guessNum} is lower than the target. Please try it again?"))

    print(f"Your guess: {guessNum} is target number! Congrats!!")