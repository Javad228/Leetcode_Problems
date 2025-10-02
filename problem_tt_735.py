class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []
        asteroids.reverse()
        stack.append(asteroids[0])
        for i in range(1,len(asteroids)):
            stack.append(asteroids[i])
            stack =self.checkStack(stack)
        

        stack.reverse()
        return stack

    def checkStack(self,stack):
        while len(stack)>1 and stack[-1] *stack[-2] <0:
            if stack[-1]>0: #positive incoming, negative existing, dont ignore
                if abs(stack[-1]) > abs(stack[-2]):
                    remember = stack.pop()
                    stack.pop()
                    stack.append(remember)
                elif abs(stack[-1]) < abs(stack[-2]):
                    stack.pop()
                else:
                    stack.pop()
                    stack.pop()
            else:
                return stack
        
        return stack







sol = Solution()
print(sol.asteroidCollision([-2,-1,1,2]))
# print(sol.asteroidCollision([5,10,-5]))
# print(sol.asteroidCollision([10,2,-5]))
# print(sol.asteroidCollision([-2,-2,1,-1]))

