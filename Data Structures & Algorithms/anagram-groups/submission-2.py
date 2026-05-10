class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # #### Method 1 ########
        # #Create a Dict Anagram:[strs words]
        # anagramDict = {}
        # finalList = []
        # #for every word in strs
        # for i in range(len(strs)):
        #     sortedWord = "".join(sorted(strs[i]))#create sorted version of word
        #     if sortedWord in anagramDict: #check if in dict, if so add it to the LLVal
        #         anagramDict[sortedWord].append(strs[i])
        #     else: #if not make a new k:v pair
        #         anagramDict[sortedWord] = [strs[i]]
       
        # return list(anagramDict.values())
        #### Method 2 #######
        countDict = {} # Create a Dict letterCountTuple : Words that are anagrams
        for word in strs:# for every word in strs
            letterArr = [0] * 26# create empty list of 26 
            for i in range(len(word)): # for each letter in a word 
                letterArr[ord(word[i]) - ord('a')] += 1#increase ord(char) - ord(letter)
            letterTuple = tuple(letterArr)# turn list into tuple
            if letterTuple in countDict: # if already in dict 
                countDict[letterTuple].append(word)#then add it to the list
            else: # if not make new
                countDict[letterTuple] = [word]
        return list(countDict.values()) # return values of dict
