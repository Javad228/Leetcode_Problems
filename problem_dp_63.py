class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        row_f =0
        col_f =0
        if  obstacleGrid[0][0] == 1:
            return 0

        for i in range(rows):
            for j in range(cols):
                if obstacleGrid[i][j] == 1:
                    if i == 0:
                        row_f = 1
                    if j == 0:
                        col_f = 1
                    obstacleGrid[i][j] = 0
                elif i == 0 :
                    if row_f ==0:
                        obstacleGrid[i][j] = 1
                    else:
                        obstacleGrid[i][j] = 0
                elif j == 0:
                    if col_f ==0:
                        obstacleGrid[i][j] = 1
                    else:
                        obstacleGrid[i][j] = 0
                else:
                    obstacleGrid[i][j] =  obstacleGrid[i][j-1]+ obstacleGrid[i-1][j]

        return obstacleGrid[rows-1][cols-1]
                
                    
        
def main():
    sol = Solution()
    print(sol.uniquePathsWithObstacles([[0,1,0]]))




if __name__ == "__main__":
    main()