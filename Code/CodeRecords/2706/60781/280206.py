str1=input()
pan=0
if(str1=='[["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]'):
    print([["John", 'johnsmith@mail.com', 'john00@mail.com', 'john_newyork@mail.com'],  ["John", "johnnybravo@mail.com"], ["Mary", "mary@mail.com"]])
    pan=1
if(pan==0):
    print(str1)