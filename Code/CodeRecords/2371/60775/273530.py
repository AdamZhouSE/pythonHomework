def do(string:str):
    string = string.upper()
    striped = []
    for x in string:
        if ord('A') <= ord(x) <= ord('Z') or ord('0') <= ord(x) <= ord('9'):
            striped.append(x)
    if len(striped) % 2 == 0:
        half = (len(striped)-1) // 2
        part1 = striped[0:half+1]
        part2 = striped[half+1:]
        part2.reverse()
        if part2 == part1:
            return 'YES'
    else:
        half = (len(striped)) // 2
        half1 = striped[0:half+1]
        half2 = striped[half:]
        half2.reverse()
        if half2 == half1:
            return 'YES'
    return 'NO'



test = int(input())
for t in range(test):
    string = input()
    print(do(string))