"""
Iterative
UNDERSTAND
I: Given a string S
O: find length of longest substring without duplciate
EC: if string len < 1 ret len(string)
    substring is consecutive chars
MATCH
Sliding window because we want to see how long we can get, document the curr longest and match against global

PLAN
var max_leng

set Seen
loop through s

if in seen
 check cur len against global
reset seen
reset currlen

else inc currentlen
add curr char to seen

return max

EVALUATE
O(N) time complex because going through string
O(N) space because of set
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        seen = set()
        max_length = 0
        l = 0

        for i in range(len(s)): #i is technically r
            letter = s[i]
            while letter in seen:
                seen.remove(s[l])
                l += 1
            seen.add(letter)
            max_length = max((i-l)+1, max_length)
                
        return max_length