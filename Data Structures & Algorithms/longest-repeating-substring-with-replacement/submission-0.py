"""
UNDERSTAND
I: string with uppercase char, int k (can replace k letters)
O: longest sub string with only one distinct letter
MATCH
Sliding window because we want 
PLAN
l = 0
replaced_counter = 0
max_length
loop through s with var i
if valid subsequence
    check with max
if not valid
while k > 


1)window state
    Same uppercase english letter with <= k replaced
EVAL
"""

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}
        max_length = 0
        max_freq = 0
        l = 0

        for r in range(len(s)):
            right = s[r]
            if right in counts: # if this is a letter we already saw
                counts[right] += 1 
            else: #this letter has not been seen
                counts[right] = 1
            max_freq = max(max_freq, counts[right]) # check if the old freq, or the current
            #window has a letter that has higher freq

            while (r-l+1) - max_freq > k: #when it become invalid window
                counts[s[l]] -= 1 # remove that letter as a possible candiate of most appearing letter
                l += 1 # move the window left
           
            max_length = max(r-l+1,max_length) # max between prev max_length or current window which 
            
        return max_length