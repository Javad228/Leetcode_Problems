from collections import defaultdict

class TimeMap(object):
    hashy = defaultdict(list)

    def __init__(self):
        self.hashy = defaultdict(list)

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        self.hashy[key].append((timestamp, value))
        

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        timestamp_ret = self.b_search(self.hashy[key],timestamp)
        if timestamp_ret == -1:
            return ""
        else:
            return(self.hashy[key][timestamp_ret][1])
    
    def b_search(self, arr, timestamp):
        ans = -1
        min_i = 0
        max_i = len(arr)-1
        mid = (min_i+max_i)//2

        while min_i<=max_i:
            if arr[mid][0]<=timestamp:
                ans = mid
                min_i = mid+1
            else:
                max_i = mid-1

            mid = (min_i+max_i)//2

        return ans
            
            
def main():
    timeMap = TimeMap()
    timeMap.set("love", "high", 10)
    timeMap.set("love", "low", 20)
    print(timeMap.get("love", 5))    # ""
    print(timeMap.get("love", 10))   # "high"
    print(timeMap.get("love", 15))   # "high"
    print(timeMap.get("love", 20))   # "low"
    print(timeMap.get("love", 25))   # "low"

if __name__ == "__main__":
    main()
