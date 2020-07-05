tomSlices = int(input())
cheSlices = int(input())
# jumbo 4 1 small 2 1
jumbo = 0
small = cheSlices
tomSlices -= small * 2
if tomSlices % 2 == 1 or tomSlices < 0:
    print("[]")
else:
    jumbo = tomSlices//2
    small -= jumbo
    print("[", end="")
    print(jumbo, end=", ")
    print(small, end="]\n")
