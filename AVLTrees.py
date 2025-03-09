import random

"""A class represnting a node in an AVL tree"""

class AVLNode(object):
        """Constructor, you are allowed to add more fields. 

        @type value: str
        @param value: data of your node
        """
        def __init__(self, value):#O(1)
                self.value = value
                self.left = None
                self.right = None
                self.parent = None
                self.height = -1 # Balance factor
                self.size = 0
                self.key = -1


        """returns the left child
        @rtype: AVLNode
        @returns: the left child of self, None if there is no left child
        """
        def getLeft(self): #O(1)
                if self:
                           return self.left
                return None

        """returns the right child

        @rtype: AVLNode
        @returns: the right child of self, None if there is no right child
        """
        def getRight(self):#O(1)
                if self:
                           return self.right
                return None
                

        
        """returns the paren @rtype: AVLNode @returns: the parent of self, None if there is no parent"""
        def getParent(self):#O(1)
                if self:
                           return self.parent
                return None

        """return the value

        @rtype: str
        @returns: the value of self, None if the node is virtual
        """
        def getValue(self):#O(1)
                if self:
                           return self.value
                return None

        """returns the height

        @rtype: int
        @returns: the height of self, -1 if the node is virtual
        """
        def getHeight(self):#O(1)
                if self:
                           return self.height
                return -1

        """sets left child

        @type node: AVLNode
        @param node: a node
        """
        def setLeft(self, node):#O(1)
                if self:
                           self.left = node
                return None

        """sets right child

        @type node: AVLNode
        @param node: a node
        """
        def setRight(self, node):#O(1)
                if self:
                           self.right = node
                return None

        """sets parent

        @type node: AVLNode
        @param node: a node
        """
        def setParent(self, node):#O(1)
                if self:
                           self.parent = node
                return None

        """sets value

        @type value: str
        @param value: data
        """
        def setValue(self, value):#O(1)
                if self:
                           self.value=value
                return None 
        """sets the balance factor of the node

        @type h: int
        @param h: the height
        """
        def setHeight(self, h):#O(1)
                if self:
                           self.height = h
                return None

        """returns whether self is not a virtual node 

        @rtype: bool
        @returns: False if self is a virtual node, True otherwise.
        """
        def isRealNode(self):#O(1)
                return AVLNode.getHeight(self) != -1

        
        """returns the size 
        @rtype: int
        @returns: returns the size of self, 0 if self == None
        """   
        def getSize(self):#O(1)
                if not self:
                       return 0
                return self.size
        """sets the size

        @type s: int
        @param s: the size
        """
        def setSize(self, s):#O(1)
                if self:
                           self.size = s
        
        """updates the size using the childs size"""
        def updateSize(self):#O(1)
                if self:   
                           self.size = AVLNode.getSize(self.left) + AVLNode.getSize(self.right) + 1

        """updates the Height using the childs Height"""   
        def updateHeight(self):#O(1)
                if self:
                           self.height = max(AVLNode.getHeight(self.left) , AVLNode.getHeight(self.right)) + 1

        

"""
A class implementing the ADT list, using an AVL tree.
"""

class AVLTreeList(object):

        """
        Constructor, you are allowed to add more fields.  

        """
        def __init__(self):
                self.size = 0
                self.root = AVLNode(None)
                self.min = None
                self.max = None
                

       

        """returns whether the list is empty

        @rtype: bool
        @returns: True if the list is empty, False otherwise
        """
        def empty(self): #O(1)
                return AVLTreeList.length(self) == 0


        """retrieves the value of the i'th item in the list

        @type i: int
        @pre: 0 <= i < self.length()
        @param i: index in the list
        @rtype: str
        @returns: the the value of the i'th item in the list
        """
        def retrieve(self, i):#O(logn)
                
                return str(AVLNode.getValue(self.select(self.root,i+1)))
        
        

        
                        

        """inserts val at position i in the list

        @type i: int
        @pre: 0 <= i <= self.length()
        @param i: The intended index in the list to which we insert val
        @type val: str
        @param val: the value we inserts
        @rtype: int
        @returns: the number of rebalancing operation due to AVL rebalancing
        """
        def insert(self, i, val):#O(logn)
                node = self.create_node(val)
                
                #inserting the first object to the list
                if i == 0 and self.length() == 0:
                        self.root = node
                        self.max = node
                        self.min = node
                        self.size += 1
                        return 0

                #insert_last
                if i == self.length():
                        self.max.setRight(node)
                        node.setParent(self.max)
                        self.max = node


                
                
                #insert_first
                elif i == 0:
                        self.min.setLeft(node)
                        node.setParent(self.min)
                        self.min = node
                        
                else:
                        succ = self.select(self.root, i+1)
                        if not succ.getLeft().isRealNode():
                                succ.setLeft(node)
                                node.setParent(succ)

                        else:
                                pre = self.predecessor(succ)
                                pre.setRight(node)
                                node.setParent(pre)
                

                self.size += 1
              
                #fixing the tree and reterning the number of rotations
                cnt = 0
                rotated = False
                parent = node.getParent()
                while parent != None:
                        #detrmening if the height of the parent has changed
                        parent.updateSize()
                        if not rotated:
                                prev_height = parent.getHeight()
                                parent.updateHeight()
                                height_changed = prev_height != parent.getHeight()     
                                BF = self.BF_q(parent)
                                if abs(BF) == 2:
                                        cnt = self.func(parent, BF)
                                        rotated = True
                                        
                        parent = parent.getParent()        
                return cnt
                
                
                


        
                
                
                

        """deletes the i'th item in the list

        @type i: int
        @pre: 0 <= i < self.length()
        @param i: The intended index in the list to be deleted
        @rtype: int
        @returns: the number of rebalancing operation due to AVL rebalancing
        """
        def delete(self, i):#O(logn)
                if i >= self.length() or i< 0:
                        return -1
                     
                #Edge cases
                if i == 0 and self.length() == 1:
                        self.size = 0
                        self.root = None
                        self.min = None
                        self.max = None
                        return 0

                #finding the node to delete      
                node = self.select(self.root, i+1)
                parent = node.getParent()
                updated_parent= None
                succ = self.successor(node)
                is_left_child = node == AVLNode.getLeft(parent)
                
                if i == 0:
                        self.min = succ
                if i == self.length() - 1:
                        self.max = self.predecessor(node)
                
                

                #node is a leaf
                if node.getSize() == 1:
                        if is_left_child:
                                        AVLNode.setLeft(parent,node.getRight())
                        else:
                                        AVLNode.setRight(parent, node.getRight())
                        node.getRight().setParent(parent)
                        updated_parent = parent
                      
                #node has 2 children
                elif  node.getLeft().isRealNode() and node.getRight().isRealNode():
                      if node.getRight() == succ:
                           if is_left_child:
                                      AVLNode.setLeft(parent, succ)
                           else:
                                      AVLNode.setRight(parent, succ)
                                      
                           succ.setLeft(node.getLeft())
                           succ.getLeft().setParent(succ)
                           AVLNode.setParent(succ,parent)
                           updated_parent = succ
                      else:
                           updated_parent = succ.getParent()
                           succ.getRight().setParent(updated_parent)
                           updated_parent.setLeft(succ.getRight())
                           
                           succ.setLeft(node.getLeft())
                           succ.setRight(node.getRight())
                           AVLNode.setParent(succ.getRight(),succ)
                           AVLNode.setParent(succ.getLeft(),succ)
                           
                           succ.setParent(parent)
                           if is_left_child:
                                      AVLNode.setLeft(parent, succ)
                           else:
                                      AVLNode.setRight(parent, succ)
                           
                           succ.setHeight(node.getHeight())
                           succ.updateSize()

                      if node == self.root:
                           self.root = succ

                #node has only one child
                else:
                        p = node.getRight() if node.getRight().isRealNode() else node.getLeft()

                        if is_left_child:
                                   AVLNode.setLeft(parent, p)
                        else:
                                   AVLNode.setRight(parent, p)
                        updated_parent = parent
                        p.setParent(parent)
                        if node == self.root:
                           self.root = p
              

                self.size -=1 
                #fixing the tree and reterning the number of rotations
                cnt = 0
                while updated_parent != None:
                        #detrmening if the height of the parent has changed
                        updated_parent.updateSize()
                        prev_height = updated_parent.getHeight()
                        updated_parent.updateHeight()
                        height_changed = prev_height != updated_parent.getHeight()     
                        BF = self.BF_q(updated_parent)
                        if abs(BF) == 2:
                                   cnt = self.func(updated_parent, BF)
                                        
                        updated_parent = updated_parent.getParent()        
                return cnt                
                
                
                        


        """returns the value of the first item in the list

        @rtype: str
        @returns: the value of the first item, None if the list is empty
        """
        def first(self): #O(1)
                return self.min.getValue()

        """returns the value of the last item in the list

        @rtype: str
        @returns: the value of the last item, None if the list is empty
        """
        def last(self): #O(1)
                return self.max.getValue()

        """returns an array representing list 

        @rtype: list
        @returns: a list of strings representing the data structure
        """
        def listToArray(self):#O(n)
                   p = self.min
                   lst = []
                   while p != None:
                              lst.append(str(p.getValue()))
                              p = self.successor(p)
                   return lst           
                     
           
                
        """
        returns the size of the list 

        @rtype: int
        @returns: the size of the list
        """
        def length(self): #O(1)
                return self.size

        """sort the info values of the list

        @rtype: list
        @returns: an AVLTreeList where the values are sorted by the info of the original list.
        """
        def sort(self): #O(nlogn)
           array = self.listToArray()
           lst = self.sort_rec(array)
           tree = AVLTreeList()
           for i in range(len(lst)):
                      tree.insert(i , lst[i])
           return tree
                
        def sort_rec(self, array):
                if len(array) < 2:
                        return array
                else:
                        pivot = array[0]
                        less = [i for i in array[1:] if i <= pivot]
                        greater = [i for i in array[1:] if i > pivot]
                        return self.sort_rec(less) + [pivot] + self.sort_rec(greater)

                

        """permute the info values of the list 

        @rtype: list
        @returns: an AVLTreeList where the values are permuted randomly by the info of the original list. ##Use Randomness
        """
        def permutation(self): #O(nlogn)
                n = self.length()
                not_choosen = [i for i in range(n)]
                perm = [i for i in range(n)]
                for i in range(n):
                        j = random.choice(not_choosen)
                        not_choosen.remove(j)
                        perm[i] = j
                perm_lst = AVLTreeList()
                for i in range(n):
                        perm_lst.insert(i,self.retrieve(perm[i]))
                return perm_lst
                

        """concatenates lst to self

        @type lst: AVLTreeList
        @param lst: a list to be concatenated after self
        @rtype: int
        @returns: the absolute value of the difference between the height of the AVL trees joined
        """
        def concat(self, lst): #O(logn)
                h1, h2 = AVLNode.getHeight(AVLTreeList.getRoot(self)) ,AVLNode.getHeight(AVLTreeList.getRoot(lst))
                if AVLTreeList.empty(lst):
                           return abs(h1-h2)
                if AVLTreeList.empty(self):
                        self.root = lst.root
                        self.max = lst.max
                        self.min = lst.min
                        return abs(h1-h2)
                      

                node = self.max
                self.delete(self.length()-1)
                self.join(lst, node)
                      
                return abs(h1-h2)
                
                


        """searches for a *value* in the list

        @type val: str
        @param val: a value to be searched
        @rtype: int
        @returns: the first index that contains val, -1 if not found.
        """
        def search(self, val):#O(n)
                p = self.min
                i = 0
                while p!=None and p.getValue() != val:
                           i += 1
                           p = self.successor(p)
                if p == None:
                           return -1
                return i



        """returns the root of the tree representing the list

        @rtype: AVLNode
        @returns: the root, None if the list is empty
        """
        def getRoot(self):#O(1)
                return self.root






###############################################################################
###############################HELP METHODS####################################
###############################################################################
        
        """finds the node with i rank
        @pre: 1 <= i <= self.length()
        @type i: int
        @rtype: AVLNode
        @returns: the node with i rank in the tree"""
        def select(self, node, i):#O(logn)
                   m = node.getLeft().getSize() + 1
                   while m != i:
                       
                       if m > i:
                           node = node.getLeft()
                           
                       elif m < i:
                           i = i - m
                           node = node.getRight()
                       m = node.getLeft().getSize() + 1
                   
                   return node


        """finds the successor of node
        @pre: node in self
        @type node: AVLNode
        @rtype: AVLNode
        @returns: the successor of node in the tree"""
        def successor(self,node):#O(logn)
                p = AVLNode.getRight(node)
                if  AVLNode.isRealNode(p):
                        while  AVLNode.isRealNode(p.getLeft()):
                                p = p.getLeft()
                        return p

                q = node.getParent()        
                while q != None and node ==  AVLNode.getRight(q):
                        node = q
                        q = q.getParent()

                return q

        """finds the predecessor of node
        @pre: node in self
        @type node: AVLNode
        @rtype: AVLNode
        @returns: the predecessor of node in the tree"""
        def predecessor(self,node):#O(logn)
                p = AVLNode.getLeft(node)
                if AVLNode.isRealNode(p):
                        while AVLNode.isRealNode(p.getRight()):
                                p = p.getRight()
                        return p

                q = node.getParent()
                while q != None and node ==  AVLNode.getLeft(q):
                        node = q
                        q = q.getParent()

                return q





        """computes the Balance factor 
        @type node: AVLNode
        @rtype: int
        @returns: the Balance factor of the givven node"""
        def BF_q(self, node):#O(1)
            if node == None or not node.isRealNode():
                    return 0
           
            return AVLNode.getHeight(node.getLeft()) - AVLNode.getHeight(node.getRight())
        """determines the direction of the rotation
           @type q: AVLNode
           @type BF: int
           @param BF: self.BF_q(q)
           @returns: the number of rotations """
        def func(self, q, BF):#O(1)
                   cnt = 0
                   if BF == 2:
                                        A,B,= q , q.getLeft() 
                                        if self.BF_q(q.getLeft()) == -1: #+2,-1
                                                AVLTreeList.rotate(self,B,"L")
                                                AVLTreeList.rotate(self,A, "R")
                                                cnt +=2
                                        else:                         #+2,+1 or 0
                                                AVLTreeList.rotate(self,A, "R")
                                                cnt+=1
                   else:
                                        A,B = q , q.getRight()
                                        if self.BF_q(q.getRight()) <= 0 :   #-2,-1
                                                AVLTreeList.rotate(self, A,"L")
                                                cnt+=1
                                        else:                           #-2,+1
                                                AVLTreeList.rotate(self,B,"R")
                                                AVLTreeList.rotate(self, A,"L")
                                                cnt+=2
                   return cnt
                                                
                   
                
        """ given a direction preforms a single rotation
        @type A, B: AVLNode
        @pre: A.getParent() = B
        @pre: D == "L" or D == "R" """
        def rotate(self, B , D):#O(1)
                root = B == self.root 
                parent = B.getParent()
                is_left_child = AVLNode.getLeft(parent) == B
                if D=="R":
                        A = B.getLeft()   
                        B.setLeft(A.getRight())
                        AVLNode.setParent(B.getLeft(), B)
                        A.setRight(B)
                                          
                if D=="L":
                        A = B.getRight()      
                        B.setRight(A.getLeft())
                        AVLNode.setParent(B.getRight(), B)
                        A.setLeft(B)
                B.setHeight(max(AVLNode.getHeight(AVLNode.getLeft(B)),AVLNode.getHeight(AVLNode.getRight(B)))+1)
                A.setHeight(max(AVLNode.getHeight(AVLNode.getLeft(A)),AVLNode.getHeight(AVLNode.getRight(A)))+1)
                AVLNode.setParent(A, parent)
                B.setParent(A)
                if is_left_child:
                           AVLNode.setLeft(parent,A)
                else:
                           AVLNode.setRight(parent,A)
                           
                #updating the sizes
                AVLNode.updateHeight(parent)           
                AVLNode.updateSize(parent)
                AVLNode.setSize(A, B.getSize())         
                B.setSize(AVLNode.getSize(AVLNode.getLeft(B))+AVLNode.getSize(AVLNode.getRight(B))+1)
                if root:
                        self.root = A
                        
                


        """creates the node in order to insert it
        @param val: the value we inserts
        @rtype: AVLNode
        @returns: the node we want to insert
        """
        def create_node(self, val):#O(1)
                node = AVLNode(val)
                node.setLeft(AVLNode(None))
                node.setRight(AVLNode(None))
                node.getLeft().setParent(node)
                node.getRight().setParent(node)
                node.setSize(1)
                node.setHeight(0)
                return node
           
        """mergs two trees and node into new one
          @type lst: AVLTreeList
          @type node: AVLNode
          @pre: self.max < node < lst.min
          @returns: None"""
        def join(self, lst, node):#O(logn)
                   r1 , r2 = self.getRoot(), lst.getRoot()
                   if r1 == None:
                              r1 = AVLNode(None)
                   if r2 == None:
                              r2 = AVLNode(None)
                   h1, h2 = AVLNode.getHeight(r1) , AVLNode.getHeight(r2)
                   if h1 < h2:
                              b = r2
                              while AVLNode.getHeight(b) > h1:
                                         b = AVLNode.getLeft(b)        
                              c = AVLNode.getParent(b) 
                              AVLNode.setRight(node, r1)
                              AVLNode.setLeft(node, b)
                              node.setHeight(max(AVLNode.getHeight(b),AVLNode.getHeight(r1))+1)
                              node.setSize(AVLNode.getSize(b) + AVLNode.getSize(r1) + 1)
                              AVLNode.setParent(node , c)
                              AVLNode.setLeft(c, node)
                              AVLNode.setParent(b , node)
                              AVLNode.setParent(r1 , node)
                              
                              
                              
                   else:
                              b = r1
                              while AVLNode.getHeight(b) > h2:
                                         b = AVLNode.getRight(b)       
                              c = AVLNode.getParent(b) 
                              AVLNode.setRight(node,r2)
                              AVLNode.setLeft(node, b)
                              node.setHeight(max(AVLNode.getHeight(b),AVLNode.getHeight(r2))+1)
                              node.setSize(AVLNode.getSize(b) + AVLNode.getSize(r2) + 1)
                              AVLNode.setParent(node , c)
                              AVLNode.setRight(c, node)
                              AVLNode.setParent(b , node)
                              AVLNode.setParent(r2 , node)
                             
                   self.max = lst.max           
                   p = node
                   root = node
                   while p != None:
                              p.updateSize()
                              p.updateHeight()
                              BF = self.BF_q(p)
                              if abs(BF) == 2:
                                         self.func(p, BF)
                              root = p              
                              p = p.getParent()

                   self.root = root