import java.util.Arrays;
class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        int min_speed=1;
        int max_speed=Arrays.stream(piles).max().getAsInt();
        while(min_speed<max_speed){
            int mid=(min_speed+max_speed)/2;
            int hour=0;
            for(int pile:piles){
                hour += (pile+mid-1)/mid;
            }
            if(hour<=h){
                max_speed=mid;
            }
            else{
                min_speed=mid+1;
            }
        }
        return min_speed;
    }
}
