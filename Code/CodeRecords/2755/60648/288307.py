long long power(long long a, long long b, long long c) {     
    if (b==0)     {         return 1;     }      
    if (b % 2 == 0)     
    {long long w = power(a, b/2, c);   
                         return (w*w) % c;     }     
    else     {         int w = power(a, b-1, c);         return (a*w) % c;     } }