#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
from Stack import Stack
from Stack import Node
from Stack import EmptyStackException

QUESTION = "3.3"


class SetOfStacks:
     capacity = 0
     currentStack = 0
     currentNode = 0
     Stacks = []
     def __init__(self, cap):
          self.capacity = cap
          firstStack = Stack()
          self.Stacks.append(firstStack)

     def generateFromArray(self, arr):        
           for i in range(len(arr)):
               el = arr[i]
               self.push(el)


     def pop(self):
          if self.Stacks[self.currentStack].isEmpty():
               if self.currentStack == 0:
                   raise Exception("Empty Set of Stacks")
               else:
                   self.currentStack = self.currentStack - 1  
                   self.currentNode = self.capacity - 1

          value = self.Stacks[self.currentStack].pop() 
          self.currentNode = self.currentNode - 1
          return value

     def push(self,data):  
         # print(self.currentStack) 
          if self.currentNode == self.capacity:
               nextStack = Stack()               
               nextStack.push(data)
               self.currentNode = 1
               self.currentStack += 1
               self.Stacks.append(nextStack)
          else:
               self.Stacks[self.currentStack].push(data) 
               self.currentNode = self.currentNode + 1
          

     def peek(self):
          if self.currentStack == 0 and self.Stacks[self.currentStack].isEmpty():
               raise EmptyStackException("Empty Stack")
          else:
               return self.Stacks[self.currentStack].peek()
     
     def printSet(self):
          for i in range(self.currentStack,-1, -1):
               Stack = self.Stacks[i]
              
               print("Printing Stack " + str(i))
               print(Stack.returnAsArray())

import sys

if __name__ == '__main__':

     start = time.perf_counter()
     capacity = 7
     arr = [11,5,6,8,3,5,8,9,10,3, 5, 99]    
     print(arr)
     Set = SetOfStacks(capacity)
     Set.generateFromArray(arr) 
     Set.printSet()
   