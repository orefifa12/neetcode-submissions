class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #Create a Dict Anagram:[strs words]
        anagramDict = {}
        finalList = []
        #for every word in strs
        for i in range(len(strs)):
            sortedWord = "".join(sorted(strs[i]))#create sorted version of word
            if sortedWord in anagramDict: #check if in dict, if so add it to the LLVal
                anagramDict[sortedWord].append(strs[i])
            else: #if not make a new k:v pair
                anagramDict[sortedWord] = [strs[i]]
        for k,v in anagramDict.items(): #return all values of dict
            finalList.append(v)
        
        return finalList