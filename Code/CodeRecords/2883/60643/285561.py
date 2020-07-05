def solution(data):
    rows=[]
    for i in range(len(data)):
        if "B" in data[i]:
            rows.append(i)
    row_id=(rows[0]+rows[-1])//2
    row=data[row_id]
    cols=[]
    for i in range(len(row)):
        if row[i]=="B":
            cols.append(i)
    col_id=(cols[0]+cols[-1])//2
    return row_id,col_id

if __name__=="__main__":
    n,m=input().split()
    n=int(n)
    m=int(m)
    data = []
    for i in range(n):
        data.append(input())
    row_id,col_id= solution(data)
    print(row_id+1,end=" ")
    print(col_id+1)