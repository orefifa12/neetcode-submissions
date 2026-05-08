class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # sort alphabetically check if the same
        # s = sorted(s)
        # t = sorted(t)
        # return s == t
        #Hashmap solution
        countT = {}
        countS = {}
        if len(s) != len(t): return False
        
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        
        return countT == countS
 
