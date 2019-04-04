#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 17:08:13 2019

@author: harryodell-mac
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.DataFrame(np.zeros((100, 100)))
# df = pd.DataFrame(index=range(100), columns=range(100))
#counter = 1

class spiral:
    
    def __init__(self, environment, direction):        
        self.environment = environment
        self.direction = direction
        self.x = 50
        self.y = 50
        self.count = 1
      
    def first_count(self):
        self.environment[self.x][self.y] = self.count
        self.count = self.count + 1
        
    def first_move(self):
        self.x = self.x + 1
    
    def move(self):          
        if self.direction == 'East':
            if self.environment[self.x][self.y - 1] == 0:
                self.y = (self.y - 1)
                self.direction = 'North'
            else:
                self.x = self.x + 1
        
        elif self.direction == 'North':
            if self.environment[self.x - 1][self.y] == 0:
                self.x = (self.x - 1)
                self.direction = 'West'
            else:
                self.y = self.y - 1
                
        elif self.direction == 'West':
            if self.environment[self.x][self.y + 1] == 0:
                self.y = (self.y + 1)
                self.direction = 'South'
            else:
                self.x = self.x - 1
                
        elif self.direction == 'South':
            if self.environment[self.x + 1][self.y] == 0:
                self.x = (self.x + 1)
                self.direction = 'East'
            else:
                self.y = self.y + 1
       
    def counter(self):
        self.environment[self.x][self.y] = self.count
        self.count = self.count + 1
        
                             
test = spiral(df, direction = 'East')

'''
test.first_count()
test.first_move()
test.counter()
test.move()
print(test.direction)
print(test.x)
print(test.y)
print(test.environment[test.x][test.y])
print(test.count)
'''

test.first_count()
test.first_move()

for i in range(9800):
    test.counter()
    test.move()

env = test.environment

plt.imshow(env)







class knight:
    
    def __init__(self, environment):        
        self.environment = environment
        self.x = 50
        self.y = 50
        
    def move(self):
        self.x, self.y = self.x + 1, self.y + 1
        
    def moves(self):
        
        allMoves = []
        move1 = self.environment[self.x + 1][self.y - 2]
        move2 = self.environment[self.x + 2][self.y - 1]
        move3 = self.environment[self.x + 2][self.y + 1]
        move4 = self.environment[self.x + 1][self.y + 2]
        move5 = self.environment[self.x - 1][self.y + 2]
        move6 = self.environment[self.x - 2][self.y + 1]
        move7 = self.environment[self.x - 2][self.y - 1]
        move8 = self.environment[self.x - 1][self.y - 2]
        
        self.environment[self.x][self.y] = self.environment[self.x][self.y] + 10000
        
        allMoves.extend([move1, move2, move3, move4, move5, move6, move7, move8])
        
        if min(allMoves) > 10000:
            print("knight trapped")
        
        whichMove = allMoves.index(min(allMoves)) + 1
        
        if whichMove == 1:
            self.x = (self.x + 1)
            self.y = (self.y - 2)
        elif whichMove == 2:
            self.x = (self.x + 2)
            self.y = (self.y - 1)
        elif whichMove == 3:
            self.x = (self.x + 2)
            self.y = (self.y + 1)
        elif whichMove == 4:
            self.x = (self.x + 1)
            self.y = (self.y + 2)
        elif whichMove == 5:
            self.x = (self.x - 1)
            self.y = (self.y + 2)
        elif whichMove == 6:
            self.x = (self.x - 2)
            self.y = (self.y + 1)
        elif whichMove == 7:
            self.x = (self.x - 2)
            self.y = (self.y - 1)
        elif whichMove == 8:
            self.x = (self.x - 1)
            self.y = (self.y - 2)







ron = knight(env)

history = []

for i in range(2020):    
    history.append([ron.x, ron.y])
    ron.moves()
    
ron.x
ron.y
ron.environment[ron.x][ron.y] - 10000
    
ronenv = ron.environment
plt.imshow(ronenv)
plt.plot(ronenv)





ron.moves
ron.x
ron.y
ron.environment[ron.x+1][ron.y+1]


















ron = knight(env)
ron.y
ron.x
ron.environment[ron.x][ron.y]
ron.moves()
ron.x
ron.y

ron.move()
ron.environment[ron.x][ron.y]

for i in range(3000):    
    ron.moves()

ronenv = ron.environment
plt.imshow(ronenv)
plt.plot(ronenv)










