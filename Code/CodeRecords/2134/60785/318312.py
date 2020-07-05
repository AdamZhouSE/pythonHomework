def poorPigs( buckets, minutesToDie, minutesToTest):
    num_pig = 0
    while (minutesToTest / minutesToDie + 1) ** num_pig < buckets:
        num_pig += 1
    return num_pig
buckets=int(input())
minutesToDie=int(input())
minutesToTest=int(input())
print(poorPigs(buckets,minutesToDie,minutesToTest))