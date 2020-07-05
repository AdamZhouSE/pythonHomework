def search(list,Target):
    try:
        print(list.index(Target));
    except Exception as e:
        print(-1);

list=eval(input());
Target=int(input());
search(list,Target);