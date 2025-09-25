class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        st = 0
        e = len(s)-1
        while st<e:
            temp = s[st]
            s[st] = s[e]
            s[e] = temp
            st+=1
            e-=1
        return s

        
def main():
    sol = Solution()
    print(sol.reverseString(["h","e","l","l","o"]))


if __name__ == "__main__":
    main()