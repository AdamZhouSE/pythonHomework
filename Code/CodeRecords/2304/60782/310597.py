 1 class Solution
 2 {
 3 public:
 4     vector<vector<int> > zigzagLevelOrder(TreeNode *root)
 5     {
 6         vector<vector<int> > vvi;
 7         
 8         if(root == NULL)
 9             return vvi;
10         
11         queue<TreeNode *> q;
12         q.push(root);
13         bool zigzag = false;
14         while(!q.empty())
15         {
16             vector<int> vi;
17             for(int i = 0, n = q.size(); i < n; ++ i)
18             {
19                 TreeNode *temp = q.front();
20                 q.pop();
21                 if(temp -> left != NULL)
22                     q.push(temp -> left);
23                 if(temp -> right != NULL)
24                     q.push(temp -> right);
25                 vi.push_back(temp -> val);
26             }
27             if(zigzag)
28                 reverse(vi.begin(), vi.end());
29             vvi.push_back(vi);
30             zigzag = !zigzag;
31         }
32         
33         return vvi;
34     }
35 };

