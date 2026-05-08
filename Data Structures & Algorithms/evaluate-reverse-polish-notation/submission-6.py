class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ['+','-','*','/']
        for token in tokens:
            if token in operators:
                if len(stack) >= 2:
                    a = stack.pop()
                    b = stack.pop()
                    a = int(a)
                    b = int(b)
                    if token == operators[0]:
                        stack.append(a+b)
                    if token == operators[1]:
                        stack.append(b-a)
                    if token == operators[2]:
                        stack.append(a*b)
                    if token == operators[3]:
                        stack.append(int(b/a))
            else:
                token = int(token)
                stack.append(token)
        return stack[0]