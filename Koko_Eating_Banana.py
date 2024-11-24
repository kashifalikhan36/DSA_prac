class Solution(object):
    def minEatingSpeed(self, piles, h):
        min_speed=1
        max_speed=max(piles)
        while(min_speed<max_speed):
            mid=(min_speed+max_speed)//2
            hour=0
            for i in piles:
                hour+=(i+mid-1)//mid
            if hour<=h:
                max_speed=mid
            else:
                min_speed=mid+1
        return min_speed
