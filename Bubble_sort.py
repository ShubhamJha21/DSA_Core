# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 15:42:14 2023

@author: Shubham Jha
"""

def bubble_sort(nums):
    for i in range(len(nums)-1):
        swap = False 
        for j in range(len(nums)-1-i):  #### Subtract i to stop lterating over last elements
            if nums[j]>nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp 
                swap = True
        if not swap:     ### Flag condition to break loop if list elemenets are already sorted 
            break 
    return nums 
if __name__ == '__main__':
    nums = [1,3,5,1,3,9,7,6]
    k = bubble_sort(nums)
    print(k)
    
            
    