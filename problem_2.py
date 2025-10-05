# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        res = ListNode()
        head = res
        over = 0
        while True:
            adder0 = 0
            adder1 = 0
            if l1 and l2:
                adder0 = l1.val
                adder1 = l2.val
            elif l1 and not l2:
                adder0 = l1.val
                adder1 = 0 
            elif l2 and not l1:
                adder0 = 0
                adder1 = l2.val
            else:
                adder0 = 0
                adder1 = 0

            idx0 = 0
            idx1 = adder0+adder1+over
            if adder0+adder1+over>9:
                idx0 = int(str(adder0+adder1+over)[0])
                idx1 = int(str(adder0+adder1+over)[1])

            head.val = idx1
            over = idx0

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            if not l1 and not l2:
                break

            
            head.next = ListNode()
            head = head.next

        if over!=0:
            head.next = ListNode()
            head = head.next
            head.val =over
        return res


sol = Solution()
l1 = ListNode(9,
       ListNode(9,
       ListNode(9,
       ListNode(9,
       ListNode(9,
       ListNode(9,
       ListNode(9)))))))

l2 = ListNode(9,
       ListNode(9,
       ListNode(9,
       ListNode(9))))

sol.addTwoNumbers(l1,l2)