class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        maxLength = 1

        for i in range(n):
            inc = 1
            for j in range(i + 1, n):
                if nums[j] > nums[j - 1]:
                    inc += 1
                else:
                    break

            dec = 1
            for j in range(i + 1, n):
                if nums[j] < nums[j - 1]:
                    dec += 1
                else:
                    break

            maxLength = max(maxLength, inc, dec)

        return maxLength
