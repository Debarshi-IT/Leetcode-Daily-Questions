class Solution:
    def minMoves(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        for num in nums:
            count += abs(nums[-1] - num)
        return count
        return count