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
    
    def find_max(self):
        if self.right:
            return self.right.find_max()
        else:
            return self.data
    
    def find_min(self):
        if self.left is None:
            return self.data
            # return self.left.find_min()
        else:
            return self.left.find_min()
            
            
    def delete(self,val):
        if val<self.data: ### Move left side 
            if self.left:
                self.left = self.left.delete(val)
        elif val>self.data:  #### Move right side 
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left == None and self.right == None: ### Reached at leaf node 
                return None 
            if self.left == None: #### Only right tree is available 
                return self.right 
            if self.right == None: #### Only left tree is available 
                return self.left
            
            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(val)
        
        return self 
    
    def insert(self,val):
        if val<self.data:
            if self.left:
                self.left.insert(val)
            else:
                self.left = binary_tree_node(val)
        else:
            if self.right:
                self.right.insert(val)
            else:
                self.right = binary_tree_node(val)
                
        
        return self 
                
                
            
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
    print(build_binary_tree(ele).delete(9).in_order_traversal())
    # ele.insert(len(ele),10)
    print(build_binary_tree(ele).in_order_traversal())
    print(build_binary_tree(ele).insert(19).in_order_traversal())
    print(build_binary_tree(ele).insert(2).in_order_traversal())
    print(build_binary_tree(ele).find_min())
    print(build_binary_tree(ele).find_max())
    
    
    
