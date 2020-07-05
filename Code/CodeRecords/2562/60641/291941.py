def main():
    n = int(input())
    for i in range(0, n):
        num_of_emails, num_of_instructions = map(int, input().split(" "))
        instructions = list(map(int, input().split(" ")))
        UNREAD = list(range(1, num_of_emails + 1))
        READ = []
        TRASH = []
        while len(instructions) > 0:
            if instructions[0] == 1:
                READ.append(instructions[1])
                UNREAD.remove(instructions[1])
            elif instructions[0] == 2:
                TRASH.append(instructions[1])
                READ.remove(instructions[1])
            elif instructions[0] == 3:
                TRASH.append(instructions[1])
                UNREAD.remove(instructions[1])
            elif instructions[0] == 4:
                READ.append(instructions[1])
                TRASH.remove(instructions[1])
            del instructions[0]
            del instructions[0]
        UNREAD = list(map(str, UNREAD))
        READ = list(map(str, READ))
        TRASH = list(map(str, TRASH))
        result = []
        if len(UNREAD) > 0:
            result.append(" ".join(UNREAD) + " ")
        else:
            result.append("EMPTY")
        if len(READ) > 0:
            result.append(" ".join(READ) + " ")
        else:
            result.append("EMPTY")
        if len(TRASH) > 0:
            result.append(" ".join(TRASH) + " ")
        else:
            result.append("EMPTY")
        print("\n".join(result))


if __name__ == '__main__':
    main()
