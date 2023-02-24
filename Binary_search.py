# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 13:59:44 2023

@author: Shubham Jha
"""

def binary_search(val,elements):
    left_index = 0 
    right_index = len(elements)-1
    mid_index = 0 
    
    while left_index <= right_index:
        mid_index = (left_index+right_index)//2
        if val == elements[mid_index]:
            return mid_index
        
        if val<elements[mid_index]:
            right_index = mid_index-1
        else:
            left_index = mid_index+1
    return -1 

if __name__ == '__main__':
    elements = [1,2,3,4,5,6,7,8,9]
    k = binary_search(5, elements)
    print(k)
    
    
            
            
        
    