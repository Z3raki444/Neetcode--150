class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        HashResult = {}
        for word in strs:
            key = tuple(sorted(word))     

            if key in HashResult:
                HashResult[key].append(word)
            else:
                HashResult[key] = [word]

        return list(HashResult.values())
