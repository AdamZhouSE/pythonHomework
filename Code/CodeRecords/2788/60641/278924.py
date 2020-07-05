def main():
    num_of_boys = int(input())
    skill_of_boys = sorted(list(map(int, input().split(" "))))
    num_of_girls = int(input())
    skill_of_girls = sorted(list(map(int, input().split(" "))))
    result = 0
    while num_of_boys > 0 and num_of_girls > 0:
        if abs(skill_of_boys[0] - skill_of_girls[0]) <= 1:
            result += 1
            num_of_boys -= 1
            num_of_girls -= 1
            del skill_of_boys[0]
            del skill_of_girls[0]
        else:
            if skill_of_boys[0] > skill_of_girls[0]:
                num_of_girls -= 1
                del skill_of_girls[0]
            else:
                num_of_boys -= 1
                del skill_of_boys[0]
    print(result)


if __name__ == "__main__":
    main()
