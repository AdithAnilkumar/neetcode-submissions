class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        rep = []
        for i in nums:
            if i in rep:
                return True
            else:
                rep.append(i)
        return False