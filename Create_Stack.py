# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 01:23:52 2023

@author: Shubham Jha
"""
from collections import deque

class stack:
    def __init__(self):
        self.container = deque()
        # print(dir(self.container))
    def print_stack(self):
        for ele in self.container:
            print(ele)
    
    def push(self,data):
        self.container.append(data)
        
    def pop(self):
        return self.container.pop()
        
    def peek(self):
        return self.container[-1]
    
    def isstackempty(self):
        return len(self.container)==0
    
    
if __name__=="__main__":
    ob = stack()
    ob.push(2)
    ob.push(3)
    ob.push(4)
    print(ob.pop())
    print(ob.peek())
    print(ob.pop())
    print(ob.pop())
    print(ob.isstackempty())
    ob.push("firstname:shubham")
    ob.push("LastName:Jha")
    print(ob.isstackempty())
    ob.print_stack()

####################### Excercise 01 ###############################

# Write a function in python that can reverse a string using stack data structure. Use Stack class from the tutorial.
# reverse_string("I shall achieve my Goal in 2023") should return "91-DIVOC ereuqnoc lliw eW"


# print(dir(deque()))
class stack:
    def __init__(self):
        self.container = deque()
        
    def append_data(self,data):
        for ch in data:
            self.container.append(ch)
        # print("Original String is ",self.container)
    
    def reverse_string(self):
        reverse_data = ""
        for i in range(len(self.container)):
            reverse_data = reverse_data + self.container.pop()
        return reverse_data

if __name__ =="__main__":
    obj = stack()
    obj.append_data("I shall achieve my Goal in 2023")
    print(obj.reverse_string())
            
        
####### Excercise 02 ###################
# Write a function in python that checks if paranthesis in the string are balanced or not. Possible parantheses are "{}',"()" or "[]".
'''
isValid("({a+b})")     --> True
isValid("))((a+b}{")   --> False
isValid("((a+b))")     --> True
isValid("))")          --> False
isValid("[a+b]*(x+2y)*{gg+kk}") --> True

'''            

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        map = {
                ")":"(",
                "}":"{",
                "]":"["
              }

        for ele in s:
            if ele =="{" or ele == "[" or ele == "(":
                stack.append(ele)
            else:
                if len(stack) == 0:
                    return False 
                if  not (map[ele] == stack.pop()):
                    return False
        return len(stack)==0
            
                
    
    
    
    
        






