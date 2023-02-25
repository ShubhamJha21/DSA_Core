# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 02:22:17 2023

@author: Shubham Jha
"""


'''Shell '''
def shell_sort(nums):
    size = len(nums)
    gap = size//2 
        
    while gap>0:
        for i in range(gap,len(nums),gap):
            temp = nums[i]           
            j = i - gap           
            while j>= 0 and temp < nums[j]:
                nums[j+gap] = nums[j]
                j = j - gap
                
            nums[j+gap] = temp
        gap = gap//2
    
    return nums 


tests = [[],[21,38,29,17,4,25,11,32,9,21],[21],[21,21],[69],[1,2,3]]
for test in tests:
    print(shell_sort(test))
# nums = [21,38,29,17,4,25,11,32,9,21]
# print(shell_sort(nums))

# for i in range(2,10,2):
#     print(i)