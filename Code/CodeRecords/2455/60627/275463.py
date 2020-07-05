import java.util.*;
import java.util.List;
import java.util.ArrayList;
public class Main {
	public static List<Integer> list[]=new List[26000];
	public static long num[]=new long [26000];
	public static long vis[]=new long [26000];
	public static long dfs(int now,int fa) {
		long ans=num[now];
		for(int i=0;i<list[now].size();i++) {
			if(list[now].get(i)==fa) {
				continue;
			}
			ans+=Math.max(0, dfs(list[now].get(i),now));  //ans为当前节点now出发寻找的最大权值（找子树）
		}
		return vis[now]=Math.max(0,ans);  //更新vis[ans]
		
	}
    public static void main(String[] args) {
    	Scanner sc =new Scanner(System.in);
    	int n=sc.nextInt();
    	for(int i=1;i<=n;i++) {
    		num[i]=sc.nextLong();
    		list[i]=new ArrayList<Integer>();
    	}
    	for(int i=1;i<=n-1;i++) {
    	    int x,y;
    	    x=sc.nextInt();
    	    y=sc.nextInt();
    	    list[x].add(y);
    	    list[y].add(x);
    	}
    	dfs(1,0);
    	long MAXX=0;
    	for(int i=1;i<=n;i++) {
    		MAXX=Math.max(MAXX, vis[i]);
    	}
    	System.out.print(MAXX);
	}
   
}

