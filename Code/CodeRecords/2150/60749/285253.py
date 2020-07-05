
#include<iostream>

#include<stdio.h>

#include<string.h>

using namespace std;

char a[3000050];

char b[1000050];

int nex[3000050];

int lena,lenb;

void set_naxt()//子串的nex数组

{

    int i=0,j=-1;

    nex[0]=-1;

    while(i<lenb)

    {

        if(j==-1||b[i]==b[j])

        {

            i++; j++;

            nex[i]=j;

        }

        else

        j=nex[j];

    }

}

int kmp()

{

    int i=0,j=0;

    set_naxt();

    while(i<lena)

    {

        if(j==-1||a[i]==b[j])

        {

            i++;j++;

        }

        else

        j=nex[j];

        if(j==lenb)

        return 1;

    }

    return 0;

}

int main()

{

    int n;

    while(~scanf("%d",&n))

    {

        int ans=0;

        scanf("%s",b);

        lenb=strlen(b);

        for(int jinzhi=2;jinzhi<=16;jinzhi++)

        {

            lena=0;

            for(int i=1;i<=n;i++)

            {

                int cnt=0;

                int tmp=i;

                int num[100];

                while(tmp)

                {

                    num[cnt++]=tmp%jinzhi;

                    tmp/=jinzhi;

                }

                for(int j=cnt-1;j>=0;j--)

                {

                    if(num[j]<10)

                    a[lena++]=num[j]+'0';

                    else a[lena++]=num[j]-10+'A';

                }

            }

            ans=max(ans,kmp());

            if(ans>0)break;

        }

        if(ans>0)printf("yes\n");

        else printf("no\n");

    }

}
