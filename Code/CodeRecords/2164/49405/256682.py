import numpy as np

T = int(input())
for t in range(T):
    s = input()
    t = np.unique(list(s))
    print(len(s) - len(t))