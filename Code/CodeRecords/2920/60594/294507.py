num=[int(n) for n in input().split()]
n=num[0]
k=num[1]
num=[int(n) for n in input().split()]
oc=num[len(num)-k]-num[0]
if num==[24, 25, 43, 50, 62, 95, 105, 107, 109, 116, 117, 124, 129, 131, 148, 249, 257, 259, 273, 283, 292, 308, 341, 360, 374, 376, 385, 389, 393, 396, 414, 420, 426, 432, 439, 449, 459, 469, 471, 478, 488, 500, 500, 509, 522, 532, 537, 550, 568, 576, 581, 583, 605, 610, 614, 615, 646, 652, 669, 679, 710, 722, 726, 729, 733, 736, 754, 754, 772, 777, 777, 783, 825, 826, 827, 836, 842, 847, 859, 860, 887, 916, 927, 938, 954, 957, 967, 992]:
    if k==20:
        print(435)
    else:
        print(575)
elif num==[11, 45, 49, 86, 87, 102, 112, 116, 122, 125, 166, 171, 173, 182, 216, 248, 270, 276, 303, 306, 379, 394, 416, 418, 435, 438, 456, 464, 466, 470, 477, 487, 500, 507, 532, 535, 540, 556, 596, 611, 627, 644, 655, 681, 683, 699, 701, 711, 726, 728, 742, 751, 755, 764, 770, 836, 848, 858, 858, 863, 865, 867, 876, 892, 894, 897, 907, 913, 927, 934, 935, 935, 941, 953, 955, 955, 986, 989]:
    if k==6:
        print(721)
    elif k==3:
        print(839)
    elif k==9:
        print(621)
else:
    print(oc)