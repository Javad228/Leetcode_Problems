class Solution(object):
    def minimumOperationsToWriteY(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        hashy_y = {}
        hashy_y[0] = 0
        hashy_y[1] = 0
        hashy_y[2] = 0
        hashy_bin = {}
        hashy_bin[0] = 0
        hashy_bin[1] = 0
        hashy_bin[2] = 0
        last = len(grid)-1
        # 1st pass
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if y == x  and y<(last/2):
                    hashy_y[grid[y][x]] = hashy_y[grid[y][x]]+1
                elif y +x ==last and y<(last/2):
                    hashy_y[grid[y][x]] = hashy_y[grid[y][x]]+1
                elif y>=(last/2) and x==(last/2):
                    hashy_y[grid[y][x]] = hashy_y[grid[y][x]]+1
                else:
                    hashy_bin[grid[y][x]] = hashy_bin[grid[y][x]]+1
            
        y_keys_sorted = sorted(hashy_y, key = hashy_y.get, reverse=True)
        bin_keys_sorted = sorted(hashy_bin, key = hashy_bin.get, reverse=True)

        max_y= y_keys_sorted[0]
        max_bin= bin_keys_sorted[0]
        
        cost_y = {}
        cost_y[0] = hashy_y[1]+hashy_y[2]
        cost_y[1] = hashy_y[0]+hashy_y[2]
        cost_y[2] = hashy_y[0]+hashy_y[1]

        if max_bin == 0:
            cost_y[0] += hashy_bin[bin_keys_sorted[0]] +hashy_bin[bin_keys_sorted[2]]
            cost_y[1] += hashy_bin[bin_keys_sorted[1]] +hashy_bin[bin_keys_sorted[2]]
            cost_y[2] += hashy_bin[bin_keys_sorted[1]] +hashy_bin[bin_keys_sorted[2]]
        elif max_bin == 1:
            cost_y[0] += hashy_bin[bin_keys_sorted[1]] +hashy_bin[bin_keys_sorted[2]]
            cost_y[1] += hashy_bin[bin_keys_sorted[0]] +hashy_bin[bin_keys_sorted[2]]
            cost_y[2] += hashy_bin[bin_keys_sorted[1]] +hashy_bin[bin_keys_sorted[2]]
        elif max_bin == 2:
            cost_y[0] += hashy_bin[bin_keys_sorted[1]] +hashy_bin[bin_keys_sorted[2]]
            cost_y[1] += hashy_bin[bin_keys_sorted[1]] +hashy_bin[bin_keys_sorted[2]]
            cost_y[2] += hashy_bin[bin_keys_sorted[0]] +hashy_bin[bin_keys_sorted[2]]

        y_cost = sorted(cost_y, key = cost_y.get)
        return cost_y[y_cost[0]]