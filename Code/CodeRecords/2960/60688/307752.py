import  re;
firstr = input();
secstr = input();
firstr=re.sub(r"\*",".",firstr)
secstr=re.sub(r"\*",".",secstr)
result=re.findall(r""+firstr,secstr);
print(secstr)
print(result)
for i in re.finditer(r""+firstr,secstr):
    print(i.start())