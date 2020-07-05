def main():
    nums = sorted(list(map(str, eval(input()))), reverse=True)
    result = "".join(nums)
    print(result)


if __name__ == "__main__":
    main()
