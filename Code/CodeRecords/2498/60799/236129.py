nums = [int(i) for i in input().strip('[|]').split(',')]
List0 = [i for i in nums if i % 2 == 0]
List1 = [i for i in nums if i % 2 == 1]
List01 = list(zip(List0, List1))
print([i for j in List01 for i in j])