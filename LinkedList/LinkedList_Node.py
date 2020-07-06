#출처 : 프로그래머스 - 연결리스트

class Node:
    def __init__(self,item):
        self.data=item
        self.next=None

class LinkedList:
    def __init__(self):
        self.NodeCount=0
        self.head=None
        self.tail=None

    def getAt(self,pos): #노드의 위치
        if(pos<=0 or pos>self.NodeCount):
            return None
        i=1
        curr=self.head
        while(i<pos):
            curr=curr.next
            i+=1
