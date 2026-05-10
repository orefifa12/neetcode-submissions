class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #create a set of nums unique
        #turn set into tuple
        #create a dict set : occurrance
        # for everything in set store count
        #sort dict vals and return 2 highset
        numDict = {}
        
        for number in nums:
            if number in numDict:
                numDict[number] += 1
            else:
                numDict[number] = 1

        newDict = dict(sorted(numDict.items(), key=lambda x:x[1], reverse = True))
       
        return (list(newDict.keys())[0:k])
