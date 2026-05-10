class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # # check each letter against other words
        # #return if fails
        # prefix = "" #keep track of prefix
        # strs = sorted(strs, key=len)
        # smallestWord = strs[0]# take the shortest word
        # for i in range (len(smallestWord)): #letter
        #     for j in range(len(strs)):
        #         if smallestWord[i] != strs[j][i]:
        #             return prefix
        #     prefix += smallestWord[i]
        # return prefix
        #### METHOD 2 #######
        
        strs.sort()
        prefix = ""

        for i in range(len(strs[0])):
            if strs[0][i] != strs[-1][i]:
                break
            prefix += strs[0][i]
        return prefix