from typing import List
class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        return [restaurants[i][0] for i in sorted(range(len(restaurants)),key=lambda i:(restaurants[i][1],restaurants[i][0]),reverse=True)if restaurants[i][3]<=maxPrice and restaurants[i][4]<=maxDistance and (not veganFriendly or restaurants[i][2])]
        

if __name__=="__main__":
    
    l1=eval(input())
    #l2=eval(input())
    a=int(input())
    b=int(input())
    c=int(input())
    x=Solution().filterRestaurants(l1,a,b,c)
    print(x)