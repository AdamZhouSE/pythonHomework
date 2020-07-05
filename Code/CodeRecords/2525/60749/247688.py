class Solution {    public int jobScheduling(int[] startTime, int[] endTime, int[] profit) {        int n=startTime.length,m=0;    	Map<Integer,Integer> map=new HashMap<>();        Map<Integer,List<Integer>> map2=new HashMap<>();        int[] dp=new int[n*2];        Set<Integer> set=new HashSet<>();        for(int i=0;i<n;i++) set.add(startTime[i]);        for(int i=0;i<n;i++) set.add(endTime[i]);        Iterator it=set.iterator();        int[] kp=new int[set.size()];        while(it.hasNext()) kp[m++]=(int)it.next();        Arrays.parallelSort(kp);        for(int i=0;i<m;i++) map.put(kp[i], i+1);        for(int i=0;i<n;i++){        	if(map2.containsKey(endTime[i]))        		map2.get(endTime[i]).add(i);        	else{        		map2.put(endTime[i], new ArrayList<>());        		map2.get(endTime[i]).add(i);        	}        }        for(int i=1;i<=m;i++){        	dp[i]=dp[i-1];        	List<Integer> tmp=map2.getOrDefault(kp[i-1], new ArrayList<>());        	for(int id=0;id<tmp.size();id++)        		dp[i]=Math.max(dp[i], dp[map.get(startTime[tmp.get(id)])]+profit[tmp.get(id)]);        }        return dp[m];    }}
public static void main(){
    
int[] startTime=input()
int[] endTime=input()
int[] profit=input()
Solution solution=new Solution() 
System.out.print(solution.jobScheduling(startTime, endTime, profit))}