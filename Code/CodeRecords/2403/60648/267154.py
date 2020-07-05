class Solution:
    def distributeCandies(self, candies: int, num_people: int):
        ans = [0] * num_people
        i = 0
        while candies > i:
            ans[i % num_people] += i + 1
            candies -= i + 1
            i += 1
        ans[i % num_people] += candies
        return ans

if __name__=="__main__":
    a=int(input())
    b=int(input())
    x=Solution().distributeCandies(a,b)
    print(x)