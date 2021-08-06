"""Non public Node class"""
class _Node:
    def __init__(self, data = None):
        self._data = data
        self._next = None
class SingleLinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        
    """ Insert value based on location """    
    def insert(self, location, value):
        newNode = Node(value)
        
        if self._head is None:              # If LL is empty then 
            self._head = newNode            # set both head and tail to first node
            self._tail = newNode            # else will throw error when inserting at end, tail.next will have null attribute.
        else :
            if location == 0 :               # At begining
                newNode.next = self._head    # Point new Node's next to head
                self._head = newNode         # Set head to new Node

            elif location == 1 :             # At End
                newNode.next = None          # Set new Node's next to null as last  
                self._tail.next = newNode    # Point tail's next to new Node
                self._tail = newNode         # set tail to new Node
            else :
                index = 0                                       # keep counter
                tempTraversalNode = self._head                  # Initialise temp traverse node
                if index < location - 1:                        # Check if counter less than location - 1 , -1 so that node can be inserted as per element count.
                    tempTraversalNode = tempTraversalNode.next  # traverse
                    index +=  1
                nextNode = tempTraversalNode.next               # Make "next node" variable and set traverse node next
                tempTraversalNode.next = newNode                # Set Temp traversed node's next to new Node
                newNode.next = nextNode                         # Set newNode's next to "next node"
          
        
        
        
    """ Delete Node"""    
    def delete(self, location):
        if self._head is None :
            print("Linked List is empty")
        else :
            if location == 0:
                if self._head == self._tail :     #only single element in LL, even if not mentioned explicitly would do
                    self._head = None
                    self._tail = None
                else:
                    self._head = self._head.next #only this would also work for location 0
            
            elif location == 1:
                if self._head == self._tail :     #only single element in LL, even if not mentioned explicitly would do
                    self._head = None
                    self._tail = None
                else :
                    tempTraverseNode = self._head              
                    while tempTraverseNode is not None:
                        if tempTraverseNode.next == self._tail :        # Traverse till tail's previous node
                            break
                        tempTraverseNode = tempTraverseNode.next
                    tempTraverseNode.next = None                        # delete last node reference
                    self._tail = tempTraverseNode                       # set tail to new last node
                    
            else :
                index = 0
                tempTraverseNode = self._head
                while index < location - 1:
                    tempTraverseNode = tempTraverseNode.next
                    index += 1
                    
                """
                ex : 30 20 2 10 5
                tempTraverseNode = 2
                nextNode = 10
                tempTraverseNode.next = 5
                
                
                """    
                nextNode = tempTraverseNode.next # this would be node to be deleted
                
                tempTraverseNode.next = nextNode.next       # set to next of deleted node.
            
    
                    
    """Traversal print Value Function"""        
    def traverse(self) :
        if self._head is None :
            print("Linked List does not exist")
        else:
            traversalNode = self._head
            while traversalNode is not None:
                print(traversalNode.data)
                traversalNode = traversalNode.next
            
        
SL = SingleLinkedList()
SL.insert(0,10)
SL.insert(0,20)
SL.insert(0,30)
SL.insert(1,55)
SL.insert(3,2)

SL.traverse()

# SL.delete(0)
# SL.delete(1)
SL.delete(3)

SL.traverse()
