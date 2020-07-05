def type(param, text, op_stack):
    op_stack.append(["T", param])
    text.append(param)


def undo(param, text, op_stack):
    to_undo_op = op_stack[-int(param)]
    op_stack.pop(-int(param))
    op_stack.append(["U", [to_undo_op[0], to_undo_op[1]]])
    if to_undo_op[0] == "T":
        text.pop(-int(param))
    elif to_undo_op[0] == "U":
        operate(to_undo_op[1][0], to_undo_op[1][1], text, op_stack)


def query(param, text, op_stack):
    print(text[int(param)-1])


def operate(op_code, param, text, op_stack):
    if op_code == "T":
        type(param, text, op_stack)
    elif op_code == "U":
        undo(param, text, op_stack)
    elif op_code == "Q":
        query(param, text, op_stack)


def func():
    op_num = int(input())
    i = 0
    text = []
    op_stack = []
    while i < op_num:
        op_code, param = input().split()
        operate(op_code, param, text, op_stack)
        i += 1


func()
