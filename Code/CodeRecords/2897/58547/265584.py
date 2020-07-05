def is_intersection_zero(word0, word1):
    return len(set(list(word0)).intersection(set(list(word1)))) == 0


def func():
    words = input()[2:-2].split("\",\"")
    i = 0
    max_product = 0
    while i < len(words):
        j = i
        while j < len(words):
            if is_intersection_zero(words[i], words[j]) and len(words[i]) * len(words[j]) > max_product:
                max_product = len(words[i]) * len(words[j])
            j += 1
        i += 1

    print(max_product)


func()
