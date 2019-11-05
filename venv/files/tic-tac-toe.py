import operator
import os
import sys
import test
from time import sleep

from numpy import *


class Game:
    mat = []
    player_one = ""
    player_two = ""
    notcross1 = ''
    notcross2 = ''
    engine = ''
    chance = 0

    def __init__(self):

        test.listen("This is tic tac toe")

    def matrixBuild(self):
        self.mat.clear()
        p = 0;
        for i in range(3):
            temp = []
            for j in range(3):
                p += 1
                temp.append(str(p))
            self.mat.append(temp)

    def startGame(self):
        self.matrixBuild()
        self.chance = 0
        print("\n1. Start Game\n2. Exit\n")
        test.listen("Press 1 for start and 2 for exit")
        print("Select = ", end='')
        test.listen("Please select")
        option = int(input())
        if option == 1:
            self.playerEntry()
        elif option == 2:
            sys.exit(0)
        else:
            print("Invalid choice!!!")
            test.listen("Invalid choice!!! select again")
            sleep(1.0)
            os.system('CLS')
            self.startGame()

    def playerEntry(self):
        print("Enter player one name = ", end='')
        test.listen("Enter player one name")
        self.player_one = input()
        choice = input(self.player_one + ",\nselect 1 for 'X'\n2 for '0' = ")
        if choice == '1':
            self.notcross1 = 'X'
        elif choice == '2':
            self.notcross1 = '0'

        if self.notcross1 == 'X':
            self.notcross2 = '0'
        else:
            self.notcross2 = 'X'
        print("Enter player two name -> ", end='')
        test.listen("Enter player two name")
        self.player_two = str(input())
        self.printArray()
        self.startWithPlayerOne()

    def startWithPlayerOne(self):
        print(self.player_one + " your move = ")
        test.listen(self.player_one + ", your move")
        move = str(input())
        if int(move) >= 10 or int(move) <= 0:
            print("Choose valid entry...")
            test.listen("Choose valid entry")
            self.startWithPlayerOne()
        tmp = 0
        for i in range(3):
            for j in range(3):
                if move == self.mat[i][j]:
                    tmp = 1
                    self.mat[i][j] = self.notcross1
                    self.chance += 1
                    if (self.chance == 9):
                        self.printArray()
                        print("All move done...")
                        test.listen("All move done")
                        self.startGame()
                    self.printArray()
                    if self.matchConditions(self.player_one) == 1:
                        print(self.player_one + " Won")
                        test.listen(self.player_one + " Won")
                        self.startGame()
                    self.startWithPlayerTwo()
        if (tmp == 0):
            self.chance -= 1
            print("Move already done, Try another move")
            test.listen("Move already done,Try another move")
            self.startWithPlayerOne()

    def startWithPlayerTwo(self):
        print(self.player_two + " your move = ")
        test.listen(self.player_two + ", your move")
        move = str(input())
        if int(move) >= 10 or int(move) <= 0:
            print("Choose valid entry...")
            test.listen("Choose valid entry")
            self.startWithPlayerTwo()
        tmp = 0
        for i in range(3):
            for j in range(3):
                if move == self.mat[i][j]:
                    tmp = 1
                    self.mat[i][j] = self.notcross2
                    self.chance += 1
                    if (self.chance == 9):
                        self.printArray()
                        print("All move done...")
                        test.listen("All move done")
                        self.startGame()
                    self.printArray()
                    if self.matchConditions(self.player_one) == 1:
                        print(self.player_two + " Won")
                        test.listen(self.player_two + " Won")
                        self.startGame()
                    self.startWithPlayerOne()
        if (tmp == 0):
            self.chance -= 1
            print("Move already done, Try another move")
            test.listen("Move already done, Try another move")
            self.startWithPlayerTwo()

    def matchConditions(self, flagName):
        if (self.mat[0][0] == '0' and self.mat[0][1] == '0' and self.mat[0][2] == '0') or (
                self.mat[0][0] == 'X' and self.mat[0][1] == 'X' and self.mat[0][2] == 'X'):
            return 1
        elif (self.mat[1][0] == '0' and self.mat[1][1] == '0' and self.mat[1][2] == '0') or (
                self.mat[1][0] == 'X' and self.mat[1][1] == 'X' and self.mat[1][2] == 'X'):
            return 1
        elif (self.mat[2][0] == '0' and self.mat[2][1] == '0' and self.mat[2][2] == '0') or (
                self.mat[2][0] == 'X' and self.mat[2][1] == 'X' and self.mat[2][2] == 'X'):
            return 1
        elif (self.mat[0][0] == '0' and self.mat[1][0] == '0' and self.mat[2][0] == '0') or (
                self.mat[0][0] == 'X' and self.mat[1][0] == 'X' and self.mat[2][0] == 'X'):
            return 1
        elif (self.mat[0][1] == '0' and self.mat[1][1] == '0' and self.mat[2][1] == '0') or (
                self.mat[0][1] == 'X' and self.mat[1][1] == 'X' and self.mat[2][1] == 'X'):
            return 1
        elif (self.mat[0][2] == '0' and self.mat[1][2] == '0' and self.mat[2][2] == '0') or (
                self.mat[0][2] == 'X' and self.mat[1][2] == 'X' and self.mat[2][2] == 'X'):
            return 1
        elif (self.mat[0][0] == '0' and self.mat[1][1] == '0' and self.mat[2][2] == '0') or (
                self.mat[0][0] == 'X' and self.mat[1][1] == 'X' and self.mat[2][2] == 'X'):
            return 1
        elif (self.mat[2][0] == '0' and self.mat[1][1] == '0' and self.mat[0][2] == '0') or (
                self.mat[2][0] == 'X' and self.mat[1][1] == 'X' and self.mat[0][2] == 'X'):
            return 1
        else:
            return 0

    def printArray(self):
        os.system('CLS')
        print('\n')
        for i in range(3):
            for j in range(3):
                print(self.mat[i][j], end="   ")
            print('\n')


gameobject = Game()
gameobject.startGame()
