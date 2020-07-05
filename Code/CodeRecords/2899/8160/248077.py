num = input()
print( "true" if num in [1<<i for i in range(0, 32, 2)] else "false")