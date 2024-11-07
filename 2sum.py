class Solution(object):
    def twoSum(self, nums, target):
        no={}
        for i,n in enumerate(nums):
            sub=target-n
            if sub in no:
                return [no[sub],i]
            no[n]=i
        return []
