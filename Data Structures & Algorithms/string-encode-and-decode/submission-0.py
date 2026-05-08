class Solution:
    
    def encode(self, strs: List[str]) -> str: #O(m)
        encodedString = ""
        for word in strs:
            for letter in word:
                encodedString += str(ord(letter))
                encodedString += "-"
            encodedString += "*"
        return encodedString

    def decode(self, s: str) -> List[str]:
        currentAscii = ""
        stringToAdd = ""
        finalOutput = []
        for number in s:
            if number == "-":
                stringToAdd += chr(int(currentAscii))
                currentAscii = ""
            elif number == "*":
                finalOutput.append(stringToAdd)
                stringToAdd = ""
            else:
                currentAscii += number
        return finalOutput
