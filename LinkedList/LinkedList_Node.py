class Node:
    def __init__(self,item):
        self.data=item
        self.next=None

class LinkedList:
    def __init__(self):
        self.NodeCount=0
        self.head=None
        self.tail=None

    def getAt(self,pos):
        if(pos<=0 or pos>self.NodeCount):
            return None
        i=1
        curr=self.head
        while(i<pos):
            curr=curr.next
            i+=1
