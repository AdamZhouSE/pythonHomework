"""
你得到了六根木棍，木棍的长度不全相同，你很无聊，所以决定把这六根木棍摆成熊或者大象：
四根长度一样的木棍代表动物的腿,剩下两根木棍用来代表动物的头和身体
表示熊的头的木棍长度必须短于身体，而大象的鼻子很长，因此表示大象头部和身体的木棍必须一样长
"""

arr=[int(k) for k in str(input()).split(" ")]
arr.sort()

if arr[0]<arr[5] and arr[1]==arr[2]==arr[3]==arr[4] and arr[4]<=arr[5]:
    print("Bear")
elif arr[0]==arr[1]==arr[2]==arr[3] and arr[3]<arr[4] and arr[4]==arr[5]:
    print("Elephant")
else:
    print("Alien")