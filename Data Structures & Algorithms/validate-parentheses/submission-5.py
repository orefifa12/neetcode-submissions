class Solution:
    def isValid(self, s: str) -> bool:
        # leftPointer = 0
        # rightPointer = len(s)-1

        # while leftPointer < rightPointer:
        #     if s[leftPointer] == '(':
        #         if s[rightPointer] == ')':
        #             leftPointer += 1
        #             rightPointer -= 1
        #         else:
        #             return False
        #     elif s[leftPointer] == '{':
        #         if s[rightPointer] == '}':
        #             leftPointer += 1
        #             rightPointer -= 1
        #         else:
        #             return False
        #     elif s[leftPointer] == '[':
        #         if s[rightPointer] == ']':
        #             leftPointer += 1
        #             rightPointer -= 1
        #         else:
        #             return False
        
        #inefficient solution
        # return True

        stack = []
        
        sLen = len(s)
        for i in range (sLen):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                stack.append(s[i])
            elif s[i] == ')':
                if stack and '(' == stack[-1]:
                    stack.pop()
                else:
                    return False
            elif s[i] == '}':
                if stack and '{' == stack[-1]:
                    stack.pop()
                else:
                    return False
            elif s[i] == ']':
                if stack and '[' == stack[-1]:
                    stack.pop()
                else:
                    return False

        return not bool(stack)


            
            
