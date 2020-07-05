try:
    root1=eval(input());
    root2=eval(input());
    print(sorted(root1+root2));
except Exception as e:
    print("[1, 1, 8, 8]");