class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class LRUCache(object):
    hashy = {}
    head = None #new stuff
    tail = None #old stuff
    capacity= 0

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.hashy = {}
        self.head = None
        self.tail = None
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        node = self.hashy.get(key,-1)
        
        if node != -1: # exists
            ret = node.data[1]
            existing = node
            if existing is self.head: 
                return ret
            prev_n = existing.prev
            next_n = existing.next
            if prev_n is not None and next_n is not None:
                prev_n.next = next_n
                next_n.prev = prev_n
            else:
                if next_n is not None and prev_n is None:
                    next_n.prev = None
                    existing.next = None
                    self.tail = next_n
            self.head.next = existing
            existing.next = None
            existing.prev = self.head
            self.head = self.head.next
            self.hashy[key] = self.head
            return ret
        else:
            return node

        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if self.head == None:
            self.head = Node((key,value))
            self.tail = self.head
            self.hashy[key] = self.head
            self.head.next = self.head
            self.capacity-=1

            return

        if key not in self.hashy:
            if self.capacity== 0:
                tail_key = self.tail.data[0]
                self.hashy.pop(tail_key, None)
                temp = self.tail.next
                temp.prev = None
                self.tail = None
                self.tail = temp
                self.capacity+=1
            node = Node((key,value))
            self.head.next= node
            node.prev = self.head
            self.head = self.head.next
            self.hashy[key] = self.head
            self.capacity-=1

        else: # key exists so need to move node to head
            existing = self.hashy[key]
            prev_n = existing.prev
            next_n = existing.next
            if prev_n is not None and next_n is not None:
                prev_n.next = next_n
                next_n.prev = prev_n
            else:
                if next_n is not None and prev_n is None:
                    next_n.prev = None
                    existing.next = None
                    self.tail = next_n
            self.head.next = existing
            existing.next = None
            existing.prev = self.head
            self.head = self.head.next
            self.head.data = (key,value)
            self.hashy[key] = self.head


        
        


# Your LRUCache object will be instantiated and called as such:
obj = LRUCache(1)
obj.put(2,1)
obj.get(2)


print(obj.tail.data)
print(obj.tail.next.data)
# while obj.head:
#     print(obj.head.data)
#     obj.head = obj.head.next
