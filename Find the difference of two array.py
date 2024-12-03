import numpy as np
class Solution(object):
    def findDifference(self, nums1, nums2):
        data1=[]
        data2=[]
        for i in nums1:
            if i in data1:
                continue
            data1.append(i)
        for i in nums2:
            if i in data2:
                continue
            data2.append(i)
        num_1=sorted(data1)
        num_2=sorted(data2)
        for i in data1:
            if i in data2:
                num_1.remove(i)
                num_2.remove(i)
        return [num_1,num_2]
