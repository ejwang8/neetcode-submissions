class Solution:
    def isPalindrome(self, s: str) -> bool:
        # strip spaces, lowercase, remove non alphanum

        # l = 5
        # 5 // 2 = 2

        # 0-2; 3-5

        # 0 1 2 3 4
        # 0=4, 1=3

        # l = 5

        # 0->l//2-1 so range(0, l//2)

        # 5, 4 is just 5->(5-1 = l-l//2 = 5-2 = 3)
        # range(l, -1, l-l//2)

        st = "".join(ch.lower() for ch in s if ch.isalnum())

        for i in range(0, len(st)//2):
            # j = len(st) - 1 - i
            if st[i] != st[len(st) - 1 - i]:
                return False
        return True
        