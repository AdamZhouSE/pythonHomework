def poorPigs(buckets, minutesToDie, minutesToTest):
    num_pig = 0
    while (minutesToTest/minutesToDie+1)**num_pig < buckets:
        num_pig += 1
    return num_pig
print(poorPigs(int(input()),int(input()),int(input())))










