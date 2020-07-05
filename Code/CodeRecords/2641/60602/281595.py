import itertools
def s1INs2(s1,s2):
    for element in itertools.permutations(string, len(string)):
        i = 0;
        temp = '';
        while (i < len(element)):
            temp += element[i];
            i += 1;
        if temp in S:
            print(True);
            return
    print(False);
string=input();
S=input();
s1INs2(string,S);