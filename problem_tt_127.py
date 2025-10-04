from collections import deque
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList:
            return 0
        
        visited = set()
        queue = deque([(beginWord,[beginWord])])
        def checkCharDiff(s1,s2):
            count = 0
            s2 = list(s2)
            for i in range(len(s1)):
                if s1[i]!=s2[i]:
                    count+=1
            if count!=1:
                return False
            return True


        while queue:
            node,path = queue.popleft()
            if node == endWord:
                return len(path)
            if node not in visited:
                visited.add(node)
                for word in wordList:
                    if word not in visited:
                        if checkCharDiff(word,node):
                            queue.append((word,path+[word]))
                
        return 0

sol = Solution()
print(sol.ladderLength("hit","cog",["hot","dot","dog","lot","log","cog"]))