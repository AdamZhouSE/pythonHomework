# 自定义函数之字符串拷贝
def strcmp(total_len, string, sub_len):
    sub_str = string[sub_len-1:total_len]
    return sub_str


length = int(input())
s = input()
s_length = int(input())
print(strcmp(length, s, s_length))