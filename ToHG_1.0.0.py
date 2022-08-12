'''
ToHG_1.0.0.py
@author: Noah Totzke

Description: 
Tower of Hanoi Game
An interactive game where the objective is to move all the rings to the middle peg without making any illegal moves

08-05-2022: v1.0.0 - Initial Release version
'''

from turtle import left
from termcolor import cprint

win = 0 #Used to keep track of win condition
player = "default" #Stores the player's name

class PostFun:
    def __init__(self):
        self.post = ['∏', '∏', '∏']
        self.taRing = 0

    def searchPost(self):
        if 'S' in self.post:
            taRing = 'S'
        elif 'M' in self.post:
            taRing = 'M'
        elif 'L' in self.post:
            taRing = 'L'
        else:
            print(f"No ring was found in {self.post} in legal position")
            taRing = 0
        return taRing
    
    def cleanPost(self, taRing):
        if self.post[2] == taRing:
            self.post[2] = '∏'
        elif self.post[1] == taRing:
            self.post[1] = '∏'
        elif self.post[0] == taRing:
            self.post[0] = '∏'
        
    
    def placePost(self, taRing):
        if taRing == 'S':
            if self.post[2] == '∏':
                self.post[2] = 'S'
            elif self.post[1] == '∏':
                self.post[1] = 'S'
            elif self.post[0] == '∏':
                self.post[0] = 'S'
        elif taRing == 'M':
            if self.post[2] == '∏':
                self.post[2] = 'M'
            elif self.post[1] == '∏' and self.post[2] != 'S':
                self.post[1] = 'M'
        elif taRing == 'L':
            if self.post[2] == '∏':
                self.post[2] = 'L'
        else:
            print(f"No valid move on {self.post}")


def win_check(win): #Will check that all rings are correctly located on the middle post
    if middlepost.post[0] == "S" and middlepost.post[1] == "M" and middlepost.post[2] == "L":
        win = 1
        print(f"""Player {player} WINS!!! 
        (ﾉ＾◡＾)ﾉ︵ ┻━┻
        """)
    else:
        win = 0
    return win

def display(): #Will display the current status of all rings and posts
    print(f"""
    {leftpost.post[0:1]}            {middlepost.post[0:1]}          {rightpost.post[0:1]}
    {leftpost.post[1:2]}            {middlepost.post[1:2]}          {rightpost.post[1:2]}
    {leftpost.post[2:3]}            {middlepost.post[2:3]}          {rightpost.post[2:3]}
    """)

cprint("\nTower of Hanoi Interactive Game v0.0.2", 'red', attrs=['bold']) #Displays intro for the game
cprint("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~", 'cyan', attrs=['blink'])

leftpost = PostFun()
middlepost = PostFun()
rightpost = PostFun()

leftpost.post[0] = "S" #These three lines sets the starting point for the rings on the left post
leftpost.post[1] = "M" 
leftpost.post[2] = "L"

correct = "no"
while correct == "no":
    player = input("What is your name?\n") #Takes player's input for the name
    print(f"""You entered {player}.""")
    correct = input("Is that correct?\n (Type yes or no)\n").lower() #Checks if the player entered their name correctly

serRing = 0
tarPost = 0
if player == 'auto241':
    pass
else:
    while win == 0: #Main gameplay loop that loops as long as win condition is not met
        display()

        choice = input("Which post do you wish to target?\n Please enter left, middle or right\n").lower() #Asks player for post that they wish to target

        if choice == "left": #Checks if left was chosen
            serRing = leftpost.searchPost()
            tarPost = input("Which post do you wish to move target to?\n Please enter middle or right\n").lower()
            if tarPost == 'middle':
                middlepost.placePost(serRing)
                if serRing in middlepost.post:
                    leftpost.cleanPost(serRing)
            elif tarPost == 'right':
                rightpost.placePost(serRing)
                if serRing in rightpost.post:
                    leftpost.cleanPost(serRing)
            else:
                print("Invalid input.")
            choice = 0
            serRing = 0
            tarPost = 0

        elif choice == "middle": #Checks if middle was chosen
            serRing = middlepost.searchPost()
            tarPost = input("Which post do you wish to move target to?\n Please enter left or right\n").lower()
            if tarPost == 'left':
                leftpost.placePost(serRing)
                if serRing in leftpost.post:
                    middlepost.cleanPost(serRing)
            elif tarPost == 'right':
                rightpost.placePost(serRing)
                if serRing in rightpost.post:
                    middlepost.cleanPost(serRing)
            else:
                print("Invalid input.")
            choice = 0
            serRing = 0
            tarPost = 0

        elif choice == "right": #Checks if right was chosen
            serRing = rightpost.searchPost()
            tarPost = input("Which post do you wish to move target to?\n Please enter left or middle\n").lower()
            if tarPost == 'left':
                leftpost.placePost(serRing)
                if serRing in leftpost.post:
                    rightpost.cleanPost(serRing)
            elif tarPost == 'middle':
                middlepost.placePost(serRing)
                if serRing in middlepost.post:
                    rightpost.cleanPost(serRing)
            else:
                print("Invalid input.")
            choice = 0
            serRing = 0
            tarPost = 0

        else: #Creates alert if choice was not valid
            print("Input is not valid")

        win_check(win)