
            if(d[i] != b.d[i]) return d[i] < b.d[i];
        return false;
    }
    bool operator >(const bign& b) const{return b < *this;}
    bool operator<=(const bign& b) const{return !(b < *this);}
    bool operator>=(const bign& b) const{return !(*this < b);}
    bool operator!=(const bign& b) const{return b < *this || *this < b;}
    bool operator==(const bign& b) const{return !(b < *this) && !(b > *this);}

    string str() const{
        char s[maxn]={};
        for(int i = 0; i < len; i++) s[len-1-i] = d[i]+'0';
        return s;
    }
};

istream& operator >> (istream& in, bign& x)
{
    string s;
    in >> s;
    x = s.c_str();
    return in;
}

ostream& operator << (ostream& out, const bign& x)
{
    out << x.str();
    return out;
}

bign f[17];
int n,d;

int main(){
    cin>>n>>d;
    if(n==1&&d==1) return cout<<0,0;
    if(d==0) return cout<<1,0;
    f[1]=1;
    for(int i=1;i<=d;i++) {
        bign tmp=1;
        for(int j=1;j<=n;j++) tmp=tmp*f[i-1];
        f[i]=f[i]+tmp+1;
    }
    bign ans=f[d]-f[d-1];
    cout<<ans;
}
