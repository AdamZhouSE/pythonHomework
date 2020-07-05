int movesToChessboard(vector<vector<int>>& board) 
    {
        int n = board.size();
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<n;j++)
            {
                if((board[0][0]^board[0][j]^board[i][0]^board[i][j])==1)
                    return -1;
            }
        }
        int row=0,col=0;
        int cntrow=0,cntcol=0;
        for(int i=0;i<n;i++)
        {
            row+=board[0][i];
            col+=board[i][0];
            if(board[0][i]!=i%2) cntrow++; //01010...
            if(board[i][0]!=i%2) cntcol++; //01010...
        }
        if(row<n/2 || row>(n+1)/2) return -1;
        if(col<n/2 || col>(n+1)/2) return -1;
        int res=0;
        if(n%2==0)
        {
            res+=min(cntrow,n-cntrow);
            res+=min(cntcol,n-cntcol);
        }
        else
        {
            if(cntrow%2==1)
                cntrow = n-cntrow;
            if(cntcol%2==1)
                cntcol = n-cntcol;
            res=cntrow+cntcol;
        }
        return res/2;
    }

n=int(input())
data2D = []
i=0
while i<n:
    i+=1
    userInput = input() # 输入数组，用空格隔开即可
    info = re.split(r'[\D]',userInput)#正则表达式分割
    data = []# 定义一维数组
    try:
        for number in info:
            data+=[int(number)] # 一维数组加入数字
        data2D+=[data] #一维数组加入到二维中去
    except:
        break;
movesToChessboard（data2D）