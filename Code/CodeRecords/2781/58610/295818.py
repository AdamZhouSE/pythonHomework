try:
    index = 0
    while True:
        index += 1
        s = []
        temps = input()
        while temps != '9':
            s.append(temps)
            temps = input()

        def sol():
            for i in range(len(s)):
                for j in range(i + 1, len(s)):
                    if s[i].startswith(s[j]) or s[j].startswith(s[i]):
                        return "Set " + str(index) + " is not immediately decodable"
            return "Set " + str(index) + " is immediately decodable"

        print(sol())
except Exception:
    pass