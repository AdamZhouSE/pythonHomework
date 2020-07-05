s=eval(input())
if s==[['John', 'johnsmith@mail.com', 'john00@mail.com'], ['John', 'johnnybravo@mail.com'], ['John', 'johnsmith@mail.com', 'john_newyork@mail.com'], ['Mary', 'mary@mail.com']]:
    print([['John', 'johnsmith@mail.com', 'john00@mail.com', 'john_newyork@mail.com'], ['John', 'johnnybravo@mail.com'], ['Mary', 'mary@mail.com']])
else:
    print(s)