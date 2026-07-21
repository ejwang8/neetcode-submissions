class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramDict = defaultdict(list)
        for str in strs:
            anagramHash = self.getHash(str)
            anagramDict[anagramHash].append(str)
        retList = []
        for key in anagramDict:
            retList.append(anagramDict[key])
        return retList

    def getHash(self, strr: str) -> Tuple[str]:
        alphaHash = [0]*26
        for letter in strr:
            i = ord(letter) - ord('a')
            alphaHash[i] += 1
        return tuple(alphaHash)