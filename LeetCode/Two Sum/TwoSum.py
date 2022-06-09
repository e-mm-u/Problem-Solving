class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        l = len(nums)
        ans = []
        for i in range(l):
            compliment = target - nums[i];           
            if compliment in nums:
                x = nums.index(compliment)
                if x!=i:               
                    ans.extend((i,x))
                    break;
        return ans
