#출처 : 프로그래머스 - 연결리스트

def popAt(self, pos): # 삭제 노드
    if pos < 1 or pos > self.nodeCount: #영역 밖
        raise IndexError
    else:
        if pos == 1:
            curr = self.head
            self.head = curr.next
            if self.nodeCount == 1:
                self.tail = None
        else:
            prev = self.getAt(pos - 1)
            curr = prev.next
            prev.next = curr.next
            if pos == self.nodeCount:
                self.tail = prev
        self.nodeCount -= 1
    return curr.data
