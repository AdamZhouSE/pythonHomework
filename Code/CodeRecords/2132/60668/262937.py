import collections


def nums_20_Nums(Str):
    count = collections.Counter(Str)
    out = {}
    out["0"] = count["z"]
    out["2"] = count["w"]
    out["4"] = count["u"]
    out["6"] = count["x"]
    out["8"] = count["g"]
    out["3"] = count["h"] - out["8"]
    out["5"] = count["f"] - out["4"]
    out["7"] = count["s"] - out["6"]
    out["9"] = count["i"] - out["5"] - out["6"] - out["8"]
    out["1"] = count["n"] - out["7"] - 2*out["9"]
    output = [key  * out[key] for key in sorted(out.keys())]
    print("".join(output))
if __name__=='__main__':
    Str = input()
    nums_20_Nums(Str)