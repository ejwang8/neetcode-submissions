class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # build a dict count for each item
        counts = defaultdict(int)       
        n = len(nums)
        for num in nums:
            counts[num] += 1
        ranked_nums = [[] for i in range(n+1)]
        for num in counts:
            count = counts[num]
            ranked_nums[count].append(num)
            # ranked_nums = [[], [1], [2], [3], [], []]
        top_nums = []
        j = 1
        while len(top_nums) < k:
            num = None
            while len(ranked_nums[-j])==0:
                j += 1
            for num in ranked_nums[-j]:
                top_nums.append(num)
            j += 1
        return top_nums
