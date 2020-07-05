class Solution {
public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        
        std::queue<string> qu;
        qu.push(beginWord);
        std::map<string,int> costInfo;
        costInfo[beginWord] = 1;
        
        set<string> wordSet;
        std::copy( wordList.begin(), wordList.end(), std::inserter( wordSet, wordSet.end() ) );

        
        while(!qu.empty())
        {
            string cur = qu.front();
            qu.pop();
            
            int cost = costInfo[cur];
            for(int i=0;i<cur.size();++i)
            {
                string tmp = cur;
                for(char c = ‘a‘;c <= ‘z‘;++c)
                {
                    if(tmp[i] == c)
                    {
                        continue;
                    }
                    tmp[i] = c;
                    auto it = wordSet.find(tmp);
                    if(it != wordSet.end())
                    {
                        wordSet.erase(it);
                        costInfo[tmp] = cost + 1;
                        qu.push(tmp);
                        
                        if(tmp == endWord)
                        {
                            return cost + 1;
                        }
                    }     
                }
            }
        }
        
        return 0;
    }
};