class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
            elif len(stack) > 0:
                if char == ')':
                    if stack.pop() != "(":
                        return False
                elif char == '}':
                    if stack.pop() != "{":
                        return False
                elif char == ']':
                    if stack.pop() != "[":
                        return False
            else:
                return False
            

        return len(stack) == 0
