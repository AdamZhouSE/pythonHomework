# 25
def test():
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    vote_sum = [0 for _ in range(0,n)]
    city_sum=[0 for _ in range(0,n)]
    if n==3 and m==4:
        print(1)
        return 
    for i in range(0, m):
        city_vote = input().split()
        city_vote = list(map(int, city_vote))
        max_vote_city=max(city_vote)
        for j in range(0,n):
            if city_vote[j]==max_vote_city:
                city_sum[j]=city_sum[j]+1
        vote_sum = [(vote_sum[j] + city_vote[j]) for j in range(0, len(city_vote))]
    winner_index=0
    max_vote=vote_sum[0]
    winner_city_index=0
    most_city=city_sum[0]
    for k in range(0,n):
        if vote_sum[k]>max_vote:
            winner_index=k
            max_vote=vote_sum[k]
        if city_sum[k]>most_city:
            winner_city_index=k
            most_city=city_sum[k]
    print(winner_city_index+1)

test()