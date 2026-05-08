class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        #Old answer
        finalArray = [] #Most repeated #
        frequencies = {} #holds key = number val = frequency of num
        
        for number in nums: #O(n)
            if number in frequencies: # if the number is already in
                frequencies[number] += 1 
            else: #First time number is appearing
                frequencies[number] = 1 

        sortedKeys = sorted(frequencies, key=frequencies.get, reverse = True) #O(n log n)
        
        for i in range (k): # for the # of elements needed to return O(k)
           finalArray.append(sortedKeys[i])
        return finalArray

