class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        glob_visited = set()
        count = 0
        def find_neighbors(graph,node):
            neighbors = []
            length = len(graph)
            dirs = [(-1,0),(0,-1),(1,0),(0,1)]
            for i in dirs:
                if node[0]+i[0] < len(graph) and node[0]+i[0]>= 0 and node[1]+i[1]< len(graph[0]) and node[1]+i[1]>=0:
                    if graph[node[0]+i[0]][node[1]+i[1]] == "X":
                        neighbors.append((node[0]+i[0],node[1]+i[1]))

            return neighbors



        def dfs_recursion(graph, node, visited = None):
            if visited is None:
                visited = set()

            if node in visited:
                return

            visited.add(node)

            for neighbor in find_neighbors(graph, node):
                dfs_recursion(graph, neighbor, visited)

            return visited
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] =='X' and (i,j) not in glob_visited:
                    new_visited = dfs_recursion(board, (i,j))
                    count+=1
                    glob_visited.update(new_visited)
        
        return count

        
        