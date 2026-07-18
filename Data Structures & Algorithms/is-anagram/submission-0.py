class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        s_dic = {}
        t_dic = {}
        for char in s:
            if char not in s_dic:
                s_dic[char] = 0
            s_dic[char] += 1
        for char in t:
            if char not in t_dic:
                t_dic[char] = 0
            t_dic[char] += 1
        return s_dic == t_dic