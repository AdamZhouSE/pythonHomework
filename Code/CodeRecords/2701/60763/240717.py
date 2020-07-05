class Solution {
public:
    int judge(const vector<vector<int>> &c) {
        for (int x = 0; x <= 1; x++) {
            for (int i = 0; i < 3; i++) {
                bool flag = true;
                for (int j = 0; j < 3; j++)
                    if (c[i][j] != x) {
                        flag = false;
                        break;
                    }
                if (flag)
                    return x;
            }

            for (int j = 0; j < 3; j++) {
                bool flag = true;
                for (int i = 0; i < 3; i++)
                    if (c[i][j] != x) {
                        flag = false;
                        break;
                    }
                if (flag)
                    return x;
            }

            if (c[0][0] == x && c[1][1] == x && c[2][2] == x)
                return x;
            if (c[2][0] == x && c[1][1] == x && c[0][2] == x)
                return x;
        }

        for (int i = 0; i < 3; i++)
            for (int j = 0; j < 3; j++)
                if (c[i][j] == -1)
                    return -1;

        return 2;
    }

    string tictactoe(vector<vector<int>>& moves) {
        vector<vector<int>> c(3, vector<int>(3, -1));

        bool turn = true;
        for (const auto &m : moves) {
            if (turn) {
                c[m[0]][m[1]] = 0;
                turn = false;
            } else {
                c[m[0]][m[1]] = 1;
                turn = true;
            }

            int t = judge(c);
            if (t == 0)
                return "A";
            else if (t == 1)
                return "B";
        }

        int t = judge(c);
        if (t == 2)
            return "Draw";

        return "Pending";
    }
};