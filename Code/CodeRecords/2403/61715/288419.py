class Solution:

    def distributeCandies(self) :
        candies = int(input())
        num_people = int(input())
        ans = [0 for _ in range(num_people)]
        now_candies = 1
        while candies > 0 :
            for i in range(num_people) :
                if candies > now_candies :
                    ans[i] += now_candies
                    candies -= now_candies
                else :
                    ans[i] += candies
                    candies = 0;
                now_candies += 1
        print(ans)
        return ans
    distributeCandies(1)