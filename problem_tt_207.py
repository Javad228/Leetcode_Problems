class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        hashy = {}
        path = set()
        flag = [0]


        for i in prerequisites:
            if i[1] not in hashy:
                hashy[i[1]] = []
            hashy[i[1]].append(i[0])
        
        def run_dfs(hashy, node,visited = None):
            if visited==None:
                visited=set()
            
            if node in path:
                print("cycle")
                flag[0] = 1
            if node in visited:
                return
            
            visited.add(node)

            path.add(node)
            for neighbor in hashy.get(node, []):
                run_dfs(hashy, neighbor, visited)
            path.remove(node)
            return visited

        for key in hashy:
            run_dfs(hashy,key)
            path = set()
            if flag[0] == 1:
                return False

        return True

        
sol = Solution()
print(sol.canFinish(2,[[1,4],[2,4],[3,1],[3,2]]))
print(sol.canFinish(2,[[1,0],[0,1]]))

