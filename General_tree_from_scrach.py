# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 17:29:56 2023

@author: Shubham Jha
"""

class treenode:
    def __init__(self,data):
        self.data = data 
        self.children = []
        self.parent = None 
    
    def add_child(self,child):
        child.parent = self
        self.children.append(child)
        
    def get_level(self):
        level = 0 
        p = self.parent
        while p:
            level = level+1
            p =  p.parent
        return level
    def print_tree(self):
        space = " " * self.get_level() * 3
        if self.get_level():
            prefix = space+'|--'
        else:
            prefix = ""
        
        print(prefix +self.data)
        for child in self.children:
            child.print_tree()
        
if __name__ =='__main__':
    #### Create a root node (Top Node) ####
    root = treenode('Electronics') ### Here self is electronics
    
    ### Laptops First Node###
    laptop = treenode('Laptops')
    root.add_child(laptop)
    
    ### First Node, all leaf nodes ###########
    laptop.add_child(treenode('Mac Book'))
    laptop.add_child(treenode('Hp Pavelian'))
    laptop.add_child(treenode('Dell'))
    
    ### Second Node Cell Phones ###
    cellphones = treenode('cellphones')
    root.add_child(cellphones)
    
    ### create leaf nodes (cell phones categories) ##
    cellphones.add_child(treenode('Lenovo K3 Note'))
    cellphones.add_child(treenode('Redmi Note 10'))
    cellphones.add_child(treenode('Samsung M12'))
    
    ### Create Thrid Node (TV) ## 
    tv = treenode('Televisions')
    root.add_child(tv)
    
    #### Create leaf nodes (tv categories)
    tv.add_child(treenode('Samsung tv'))
    tv.add_child(treenode('Mi tv'))
    tv.add_child(treenode('Philips tv')) 
    
    root.print_tree()