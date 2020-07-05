def func():
    try:
        unique_id = 1
        while True:
            arr = []

            while True:
                now = input()
                if now == "9":
                    break
                arr.append(now)
            bf = False

            i = 0
            while i < len(arr):
                j = 0
                while j < len(arr):
                    if j != i and arr[j].startswith(arr[i]):
                        bf = True
                        break
                    j += 1
                if bf:
                    break
                i += 1

            if bf:
                print("Set " + str(unique_id) + " is not immediately decodable")
            else:
                print("Set " + str(unique_id) + " is immediately decodable")

            unique_id += 1
    except EOFError:
        return


func()
