def main():
    num_of_examples = int(input())
    for i in range(0, num_of_examples):
        result = 0
        N, X, Y = map(int, input().strip().split(" "))
        A = list(map(int, input().strip().split(" ")))
        B = list(map(int, input().strip().split(" ")))
        ine_tips = list(zip(A, B))
        e_tips = []
        for tip in ine_tips:
            if tip[0] == tip[1]:
                e_tips.append(tip[0])
                ine_tips.remove(tip)
        while len(ine_tips) > 0:
            a = 0
            b = 0
            tip_a = [0, 0]
            tip_b = [0, 0]
            if X > 0:
                tip_a = list(reversed(sorted(ine_tips, key=lambda x: x[0])))[0]
            if Y > 0:
                tip_b = list(reversed(sorted(ine_tips, key=lambda x: x[1])))[0]
            a = tip_a[0]
            b = tip_b[1]
            if a >= b:
                result += a
                ine_tips.remove(tip_a)
                X -= 1
            else:
                result += b
                ine_tips.remove(tip_b)
                Y -= 1
        result += sum(e_tips)
        print(result)


if __name__ == "__main__":
    main()
