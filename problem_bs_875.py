import math


class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        min_k = int(math.ceil(float(sum(piles))/h))
        max_k = max(piles)
        k =(max_k+min_k)//2

        while min_k<max_k:
            res = self.simulate(piles, k)

            if res <= h:
                max_k = k
            else:
                min_k = k+1
            
            k =(max_k+min_k)//2

        return min_k

    def simulate(self, piles, k):
        h = 0
        for i in range(len(piles)):
            h += math.ceil(float(piles[i])/k)
        return h

def main():
    piles = [3,6,7,11]
    h = 8
    obj = Solution()
    print(obj.minEatingSpeed(piles, h))




if __name__ == "__main__":
    main()