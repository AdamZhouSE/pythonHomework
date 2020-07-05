import java.util.*;
public class Main {
	
	public static void main(String args[]){		
		isSameTree();
	}	
	public static void isSameTree(){		
		Scanner s= new Scanner(System.in);
		//判断个数
		int num = Integer.valueOf(s.nextLine());
		//第一个序列
		String firstTreeStr = s.nextLine();
		//得到第一个序列的两个子串，第一个子串全部小于串中第一个数字，第二个子串全部大于第一个数字，顺序和原串相同		
		String subFirstTreeStrSmall = devideTree( firstTreeStr,1);
		String subFirstTreeStrBig = devideTree( firstTreeStr,2);	
//		System.out.println(subFirstTreeStrSmall);
//		System.out.println(subFirstTreeStrBig);
		String treeStr = s.nextLine();
		String subTreeStrSmall = devideTree( treeStr,1);
		String subTreeStrBig = devideTree( treeStr,2);
		
		ArrayList res = new ArrayList();
		
		while(!treeStr.equals("0")){
			
			if(subTreeStrSmall.equals(subFirstTreeStrSmall)&&subTreeStrBig.equals(subFirstTreeStrBig))
				 res.add("YES");
				 //System.out.println("YES");
			 else res.add("NO");//System.out.println("NO");
			
			
			 treeStr = s.nextLine();
			 subTreeStrSmall = devideTree( treeStr,1);
			 subTreeStrBig = devideTree( treeStr,2);
		}
		
		for(int i=0;i<num;i++){
			
			System.out.println(res.get(i));			
		}
		
	}	
	//分隔串函数，int i 代表，子串大于或小于第一个数字i小于，2大于
	public static String  devideTree(String treeStr,int i){		
		String subStr = "";
		int length = treeStr.length();		
		int firstStr = Integer.valueOf(treeStr.charAt(0)+"");
		if(i==1){			
			for(int x = 1;x<length;x++){				
				int nextStr = Integer.valueOf(treeStr.charAt(x)+"");
				if(nextStr<firstStr)
					subStr+=nextStr;				
			}			
		}else if(i==2){
			for(int x = 1;x<length;x++){				
				int nextStr = Integer.valueOf(treeStr.charAt(x)+"");
				if(nextStr>firstStr)
					subStr+=nextStr;				
			}
		}		
		return subStr;		
	}
}