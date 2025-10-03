class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        left = 0
        arr = list(str(x))
        right = len(arr)-1
        while left<right:
            if arr[left] != arr[right]:
                return False

            left+=1
            right-=1
            
        return True