# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 00:44:47 2023

@author: Shubham Jha
"""

class binary_tree_node:
    def __init__(self,data):
        self.data = data 
        self.left = None 
        self.right = None  
    
    def add_child(self,val):
        if self.data == val:
            return
        if val<self.data:
            # left side 
            if self.left:
                self.left.add_child(val)
            else:
                self.left = binary_tree_node(val)
        else:
            #right side 
            if self.right:
                self.right.add_child(val)
            else:
                self.right = binary_tree_node(val)

    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements
    
    def pre_order_traversal(self):
        elements = []
        elements.append(self.data)
        
        if self.left:
            elements += self.left.pre_order_traversal()
        if self.right:
            elements += self.right.pre_order_traversal()
        return elements
    
    def post_order_traversal(self):
        elements = []
        if self.left:
            elements = elements + self.left.post_order_traversal()
        if self.right:
            elements = elements + self.right.post_order_traversal()
            
        elements.append(self.data)
        
        return elements
    
    def search(self,val):
        if val == self.data:
            return True 
        
        if val<self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
        else:
            if self.right:
                return self.right.search(val)
            else:
                return False 
            
def build_binary_tree(elements):
    root = binary_tree_node(elements[0])
    
    for i in range(1,len(elements)):
        root.add_child(elements[i])
    
    return root

if __name__ == '__main__':
    ele = [17, 4, 1, 20, 9, 23, 18, 34]
    print(build_binary_tree(ele).in_order_traversal())
    print(build_binary_tree(ele).pre_order_traversal())
    print(build_binary_tree(ele).post_order_traversal())
    print(build_binary_tree(ele).search(1))
    print(build_binary_tree(ele).search(36))
    print(build_binary_tree(ele).search(18))
    
    
