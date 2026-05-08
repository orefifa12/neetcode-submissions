class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        splitS = []
        splitT = []
        for char in s:
            splitS.append(char)
        for char in t:
            splitT.append(char)
        splitS = sorted(splitS)
        splitT = sorted(splitT)
        if len(splitS) != len(splitT):
            return False
        for char in splitS:
            if char in splitT:
                splitT.remove(char)
                continue
            else:
                return False
        
        return True