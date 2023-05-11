class Node:
    #create the contructor with two elements on a Node inside LinkedList
    #data: element which can harbor any element type (text, number)
    #next: to link the next node
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    #create constructor with the first Node = head is empty
    def __init__(self):
        self.head=None
    
    #to add a node in the LinkedList
    def append(self,data):
        newNode=Node(data)
        #review if the linked list  is empty
        if self.head==None:
            self.head=newNode
            return
        #the beginning of the list
        lastNode=self.head
        #looking for the end of the list  
        #condition until the lasNode.next not be empty
        while lastNode.next:
            #move the lastNode to the nextNode
            lastNode=lastNode.next
        #add the new node 
        lastNode.next=newNode
    #print the list
    def printList(self):  
        #start the list with the first Node
        # by default the first node is head   
        cur_node=self.head
        while cur_node:
            print(cur_node.data)
            cur_node=cur_node.next
    #add element to the first place
    def prepend(self,data):
        newNode= Node(data)
        newNode.next=self.head
        self.head=newNode
    
    def insert(self,prevNode,data):
        if not prevNode:
            print("Previous node does not exist.")
            return
        newNode =Node(data)
        newNode.next=prevNode.next
        prevNode.next=newNode
            
    def delete(self,key):
        curNode= self.head
        if curNode and curNode.data== key:
            self.head= curNode.next
            curNode=None
            return    
        prev=None
        if curNode and curNode.data!=key:
            prev=curNode
            curNode=curNode.next
        if curNode is None:
            return
        prev.next=curNode.next
        curNode=None

    def deletePos(self,pos):
        if self.head:
            curNode=self.head
            if pos==0:
                self.head= curNode.next
                curNode=None
                return    
        prev=None
        count=0
        while curNode and count !=pos:
            prev=curNode
            curNode=curNode.next
            count+=1
        if curNode is None:
            return
        prev.next=curNode.next
        curNode=None
    
    def lenght(self):
        curNode=self.head 
        count=0
        while curNode:
            print (curNode.data)
            curNode=curNode.next 
            count+=1
        return count
    
    def lenghtRec(self,node):
        if node is None:
            return 0
        return 1+ self.lenghtRec(node.next)
    
    def swap_nodes (self,key1,key2):
        if key1==key2:
            return 
        prev1=None
        curNode1=self.head
        while curNode1 and curNode1.data!=key1:  
            prev1=curNode1
            curNode1=curNode1.next
        prev2=None
        curNode2=self.head
        while curNode2 and curNode2.data!=key2:  
            prev2=curNode2
            curNode2=curNode2.next
        
        #not exist these nodes in the linkedlist
        if not curNode1 or not  curNode2:
            return 

        if prev1:
            prev1.next=curNode2
          
        else:
            self.head=curNode2

        if prev2:
            prev2.next=curNode1
        else:
            self.head=curNode1
        
        curNode1.next, curNode2.next= curNode2.next, curNode1.next




            


        





    

llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
#llist.prepend("D")

llist.printList() 
llist.insert(llist.head, "P")
llist.delete("A")
llist.printList() 
print ("hola")
llist.append("R")
llist.printList()
print ("hola")
llist.deletePos(0)
llist.printList()
print ("list")
print(llist.lenght())
print(llist.lenghtRec(llist.head))
print ("listFinal")
llist.printList()
llist.swap_nodes("B", "C")
print("Swapping nodes B and C that are  head nodes")
llist.printList()

llist.swap_nodes("A", "B")
print("Swapping nodes A and B where key_1 is head node")
llist.printList()

llist.swap_nodes("B", "R")
print("Swapping nodes D and B where key_2 is head node")
llist.printList()

llist.swap_nodes("C", "B")
print("Swapping nodes C and C where both keys are same")
llist.printList()