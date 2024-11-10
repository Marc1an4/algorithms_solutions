class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strings, result = {}, []
        for i in strs:
            if ''.join(sorted(i)) in strings:
                strings[''.join(sorted(i))].append(i)
            else: 
                strings[''.join(sorted(i))] = [i]

        for i in strings:
            result.append(strings[i])
        return result