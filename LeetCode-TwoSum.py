class Solution(object):
    """
    put the values of the list nums into the dict as indices
    and the indices of the former into the dict as values
    """
    def twoSum(self, nums, target):
        self.nums = nums
        self.target = target
        dict = {}
        for i in range(len(self.nums)):
            dif = target - self.nums[i]
            if dif in dict.keys(): # = if dif in dict
                return (dict[dif], i) # return the value of dict[i]
            dict[self.nums[i]] = i

print(Solution().twoSum([3, 5, 5, 9], 10))
