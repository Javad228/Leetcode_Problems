class MyCircularQueue(object):
    queue = []
    head = 0
    tail = 0
    total = 0

    # [ , , ] h=0, t =0
    # [1, , ] h=0, t=1
    # [1,2, ] h=0, t=2
    # [1,2,3] h=0, t=3
    # [ ,2,3] h=1, t=3


    def __init__(self, k):
        """
        :type k: int
        """
        self.queue = k*[None]
        self.head= 0
        self.tail= k -1
        self.total = 0
        

    def enQueue(self, value):
        """
        :type value: int
        :rtype: bool
        """
        tail = self.tail
        head = self.head
        total = self.total

        # print("enqueue")
        if self.isFull():
            # print(self.queue)
            return False
        
        self.total+=1

        if tail == len(self.queue)-1: #if last index
            self.queue[0] = value
            tail = 0
        else:
            self.queue[tail+1] = value
            tail = tail+1

        self.tail = tail

        # print(self.queue)
        # print("head " + str(self.head))
        # print("tail" + str(self.tail))
        return True

        

    def deQueue(self):
        """
        :rtype: bool
        """
        tail = self.tail
        head = self.head
        total = self.total

        # print("dequeue")
        if self.isEmpty():
            # print(self.queue)
            return False

        self.total-=1

        if head == len(self.queue)-1: #if last index
            self.queue[len(self.queue)-1] = None
            head = 0
        else:
            self.queue[head] = None
            head = head+1

        self.head = head

        # print(self.queue)
        # print("head " + str(self.head))
        # print("tail" + str(self.tail))
        return True

    def Front(self):
        """
        :rtype: int
        """
        # print("front")
        if self.isEmpty():
            return -1
        return self.queue[self.head]

    def Rear(self):
        """
        :rtype: int
        """
        # print("rear")
        if self.isEmpty():
            return -1
        return self.queue[self.tail]

    def isEmpty(self):
        """
        :rtype: bool
        """
        if self.total ==0:
            return True
        return False
        

    def isFull(self):
        """
        :rtype: bool
        """
        if self.total == len(self.queue):
            return True
        return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()