class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        visited = set()
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1" and (i,j) not in visited:
                    # run dfs
                    count+=1
                    visited.update(self.dfs_iterative(grid, (i,j)))
        return count

    def dfs_iterative(self,graph, start):
        stack=[start]
        result = []
        visited = set()
        def check_node(graph, node):
            if node[0] < len(graph) and node[0] >= 0 and node[1]>=0 and node[1] < len(graph[node[0]]) and node not in visited:
                som = graph[node[0]][node[1]]
                if graph[node[0]][node[1]] and graph[node[0]][node[1]] == '1':
                    return True
            return False

        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                result.append(node)
                dir1= (node[0]-1,node[1])
                dir2 = (node[0],node[1]-1)
                dir3 = (node[0],node[1]+1)
                dir4 = (node[0]+1,node[1])

                if check_node(graph, dir1):
                    stack.append(dir1)
                if check_node(graph, dir2):
                    stack.append(dir2)
                if check_node(graph, dir3):
                    stack.append(dir3)
                if check_node(graph, dir4):
                    stack.append(dir4)
        
        return visited



sol = Solution()
sol.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]])