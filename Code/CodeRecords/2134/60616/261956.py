def poorPigs(buckets, minutesToDie, minutesToTest):
    num_pig = 0
    while (minutesToTest / minutesToDie + 1) ** num_pig < buckets:
        num_pig += 1
    return num_pig
bucket=int(input())
minutesToDie=int(input())
minutesToTest=int(input())
print(poorPigs(bucket,minutesToDie,minutesToTest))