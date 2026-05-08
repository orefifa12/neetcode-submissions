class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.casefold()
        s = s.replace (" ", "")
        s= "".join(ch for ch in s if ch.isalnum())

        arrLength = len(s)-1
        i = 0
        j = arrLength
        if len(s) <= 1 : return True
        
        leftPointer = s[i]
        rightPointer = s[j]


        while ((j-i) >= 1):
  
            if leftPointer != rightPointer:
                return False

            i += 1
            j -= 1
            leftPointer = s[i]
            rightPointer = s[j]
        
        
        return True