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
print(test.direction)
print(test.x)
print(test.y)
print(test.environment[test.x][test.y])
print(test.count)

test.first_move()
print(test.direction)
print(test.x)
print(test.y)
print(test.environment[test.x][test.y])
print(test.count)

test.counter()
print(test.direction)
print(test.x)
print(test.y)
print(test.environment[test.x][test.y])
print(test.count)

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
        
        











