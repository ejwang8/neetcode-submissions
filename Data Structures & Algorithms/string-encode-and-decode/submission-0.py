class Solution:
    def encode(self, strs: List[str]) -> str:
        l_to_join = []
        for s in strs:
            l_to_join.append(str(len(s)) + '#' + s)
        encoded = ''.join(l_to_join)
        return encoded

    def decode(self, s: str) -> List[str]:
        lisss = []
        i = 0
        j = 0
        while i < len(s):
            while s[j] != '#':
                # move it to right
                j += 1
            # and capture num
            print(i, j)
            l = int(s[i:j])
            # then move i and j
            i = j+1
            j = i+l
            uno_s = s[i:j]
            print(uno_s)
            # then append to string list
            lisss.append(uno_s)
            i=j
        return lisss

