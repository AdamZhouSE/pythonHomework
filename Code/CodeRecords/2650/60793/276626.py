feed_times = list(map(int, input().split()))[-1]
dogs = list(map(int, input().split()))
for feed in range(0, feed_times):
    temp_ls = list(map(int, input().split()))
    dog_slice = sorted(dogs[temp_ls[0] - 1:temp_ls[1]])
    print(dog_slice[temp_ls[-1] - 1])