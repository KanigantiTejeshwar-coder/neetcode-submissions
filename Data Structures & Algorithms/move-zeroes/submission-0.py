class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        result = []
        count = 0
        
        for i in nums:
            if i != 0:
                result.append(i)
            else:
                count += 1
                
        for i in range(count):
            result.append(0)
            
        nums[:] = result
