class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # sort alphabetically check if the same
        s = sorted(s)
        t = sorted(t)
        return s == t
        