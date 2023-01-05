# -*- coding: utf-8 -*-
"""
Created on Sun Jan  1 19:40:51 2023

@author: Shubham Jha
"""

##### Node Class ###############

class Node:
    def __init__(self,data,next):
        self.data = data 
        self.next = next 

##### Linked List class ############


class Linkedlist:
    def __init__(self):
        self.head = None
    
######### Insert element at the begining of linked list Time complexity: O(1) 
    def insert_at_begining(self,data):
        # if self.head == None:
        node = Node(data,self.head) ## Next address of New node would be old head(Right side element)
        self.head = node
    
    
########### Insert element at the end of linked list: Time Complexity O(n)
        # ex: 8>>6>>5>>None
    def insert_element_at_the_end(self,data):
        if self.head == None:  ### Check linkedlist blank status 
            node = Node(data,None)
            self.head = node
            return 
        
        ### If linked list has some values
        curr  = self.head 
        ### Iterate through all elements reach to final linked list element
        while curr.next: 
            curr = curr.next
        node = Node(data,None)
        curr.next = node
    
    def insert_element_after_val(self,prevdata,data):
        # node = Node(data,)
        curr = self.head
        while curr:
            temp = curr.next
            if curr.data == prevdata:
                node = Node(data,curr.next)
                curr.next = node
                # curr = temp
                break
            curr = temp
    
    def remove_element_after_val(self,prev):
        curr = self.head 
        while curr:
            if curr.data == prev:
                curr.next = curr.next.next
                break
            curr = curr.next
        
# ######## Linkedlist Length #########
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next

        return count
    
    #### Insert at index ###
    
    def insert_at(self,index,data):
        if index==0:
            self.insert_at_begining(data)
        elif index>0 and index<self.get_length():
            itr = self.head
            count = 0 
            while itr:
                count = count+1
                if count == index:
                    node=Node(data,itr.next)
                    itr.next = node
                    break
                itr = itr.next
            
        else:
            raise Exception("Invalid Index")            
        
    ### Remove at Index 
    
    def remove_at(self,index):
        itr = self.head 
        count = 0 
        while itr:
            count = count+1
            if count == index:
                itr.next = itr.next.next 
                break 
            itr = itr.next
    
        
#################### Print linked list ################         
    def print_linkedlist(self):
     ### ### Check Linkedlist is empty or Not?
        if self.head == None:
            print("Linked list is empty")
            return 
        
    ##### If Linkedlist is not Empty ##
        curr = self.head 
        linkstr = ""  
        while curr:
            val = curr.data
            linkstr = linkstr+str(val)+" >> "
            curr = curr.next
        print(linkstr)
        
    # Print linkedlist from second mid index 
    def second_mid_link(self):
        slow = self.head 
        fast = self.head 
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next 
        link_str =""
        while slow:
            link_str = link_str + str(slow.data) + " >>"
            slow = slow.next
        return link_str
    
    ## Print linkedlist from first mid index
    def first_mid_link(self):
        slow = self.head 
        fast = self.head 
        
        while fast and fast.next:
            temp = slow
            slow = slow.next
            fast = fast.next.next 
        link_str =""
        while temp:
            link_str = link_str + str(temp.data) + " >>"
            
            temp = temp.next
        return link_str
    
    def create_new_linkedlist(self,data_list):
        self.head = None 
        for ele in data_list:
            self.insert_element_at_the_end(ele)
        
        
        
            
if __name__ =="__main__":
    ob = Linkedlist()
    ob.insert_at_begining(5)
    ob.insert_at_begining(6)
    ob.insert_at_begining(8)
    ob.insert_element_at_the_end(9)
    ob.insert_element_after_val(6,7)
    ob.print_linkedlist()
    ob.remove_element_after_val(6)
    ob.print_linkedlist()
    print(ob.get_length())
    print(ob.second_mid_link())
    print(ob.first_mid_link())
    # ob.lenth_varible_testing()
    ob.insert_at(2, 7)
    # ob.insert_at(100, 7)
    print("Before Removing Value at index:")
    ob.print_linkedlist()
    ob.remove_at(3)
    print("After Removing Value at Index:")
    ob.print_linkedlist()
    print("Create a new linkedlist")
    ob.create_new_linkedlist([1,2,3,4,5,6,7])
    ob.print_linkedlist()
    
        


