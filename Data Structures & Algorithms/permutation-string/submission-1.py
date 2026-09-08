class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2): return False
        # define counts dicts... for now use array (hash of anagram, later try hash too)
        # shorter = s1
        counts_s1, counts_s2 = [0] * 26, [0] * 26

        # generate it for s1 lenght in both strings
        # get counts_s1
        for i in range(len(s1)):
            # index = ord(s[i])-ord('a')
            counts_s1[ord(s1[i])-ord('a')] += 1
            counts_s2[ord(s2[i])-ord('a')] += 1

        # calculate matches
        matches = 0
        for i in range(26):
            matches += (1 if (counts_s1[i] == counts_s2[i]) else 0)
        print(matches)

        # loop through rest of s2, check matches...
        l = 0
        for r in range(len(s1), len(s2)):
            if matches==26: return True

            # otherwise update counts and matches
            r_i = ord(s2[r]) - ord('a')
            counts_s2[r_i] += 1
            if counts_s2[r_i] == counts_s1[r_i] + 1:
                matches -= 1
            elif counts_s2[r_i] == counts_s1[r_i]:
                matches += 1

            l_i = ord(s2[l]) - ord('a')
            counts_s2[l_i] -= 1
            if counts_s2[l_i] == counts_s1[l_i] - 1:
                matches -= 1
            elif counts_s2[l_i] == counts_s1[l_i]:
                matches += 1
            l += 1

        return matches == 26


