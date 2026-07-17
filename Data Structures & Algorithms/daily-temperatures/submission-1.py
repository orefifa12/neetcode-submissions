class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        results = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                results[stack[-1]] = (i - stack[-1])
                stack.pop()
            stack.append(i)
    
        return results
                    
        """
        UNDERSTAND
        I: array of type int
        O: array type int
        EC: 1 temp return 0

        We need to return an array that for each element i in results, 
        results[i] is the amount of days unitl we see a higher temp
        than temperatures[i]

        MATCH 
        Stack

        Plan
        stack
        loop through temp
        if stack empty
            add current temp index to stack
        else
            check if next temp > index of temp on stack
            if so
                while
                update the results arr

            else:
                add next temp to stack
        
        return results arr

        """