class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        cols = len(matrix)
        rows = len(matrix[0])

        min_i = 0
        max_i = (cols*rows)-1
        mid = (min_i+max_i)//2

        while min_i<=max_i:
            ret_arr =  self.calc_index(mid,rows)
            i,j = ret_arr[0],ret_arr[1]
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                min_i = mid +1
            else:
                max_i = mid-1

            mid = (min_i+max_i)//2

        return False



    def calc_index(self,idx,rows):
        div = idx//rows
        a = idx%rows
        return (div,a)

        
def main():
    matrix=[[1]]
    target=1
    obj = Solution()
    print(obj.searchMatrix(matrix, target))




if __name__ == "__main__":
    main()