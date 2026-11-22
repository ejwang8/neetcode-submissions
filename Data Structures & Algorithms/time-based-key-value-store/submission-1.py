class TimeMap:

    # set is O(1)
    # get is O(logn)
    # my first thought was set within a set for o(1) get and set. but because the key might not exist, do need to search so get is o(logn)

    def __init__(self):
        self.structure = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.structure:
            self.structure[key] = []
        self.structure[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        values = self.structure.get(key, [])

        # binary search
        l, r = 0, len(values)-1
        res = ""

        while l <= r:
            m = (l + r) // 2
            if values[m][1] == timestamp:
                return values[m][0]
            elif values[m][1] < timestamp:
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1
        return res
                
        
