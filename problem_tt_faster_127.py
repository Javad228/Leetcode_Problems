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
        wordList = set(wordList)
        visited = set()
        queue = deque([(beginWord,[beginWord])])
        while queue:
            node,path = queue.popleft()
            if node == endWord:
                return len(path)
            if node not in visited:
                visited.add(node)
                # generate neighbors instead
                L= len(node)
                for i in range(L):
                    last = node[i+1:]
                    first = node[:i]
                    for j in 'qwertyuiopasdfghjklzxcvbnm':
                        word= first+j+last
                        if word in wordList:
                            queue.append((word,path+[word]))
                
        return 0

sol = Solution()
print(sol.ladderLength("hit","cog",["hot","dot","dog","lot","log","cog"]))