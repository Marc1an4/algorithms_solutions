class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_hash, t_hash = {}, {}
        for i in range(len(s)):
            s_hash[s[i]] = s_hash.get(s[i], 0) + 1
            t_hash[t[i]] = t_hash.get(t[i], 0) + 1
        
        for i in set(s):
            s_curr = s_hash.get(i, 0)
            t_curr = t_hash.get(i, 0)
            if s_curr != t_curr:
                return False
        return True