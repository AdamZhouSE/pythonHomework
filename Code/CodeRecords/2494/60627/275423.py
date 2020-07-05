class Solution {
    public int reversePairs(int[] nums) {
        //给定数组，求符合条件的逆序对
        //思路:同剑指offer的类似，但是每次合并需要从头开始合并，同时排序
        if(nums==null||nums.length==0) return 0;
        return reversePairsCore(nums,0,nums.length-1);
    }
    public int reversePairsCore(int [] nums,int start,int end){
        if(start>=end){
            return 0;
        }else{
            int mid=start+(end-start)/2;
            int left=reversePairsCore(nums,start,mid);
            int right=reversePairsCore(nums,mid+1,end);

            int [] copy=new int[end-start+1];
            int i=start,t=start;
            int j=mid+1;
            int curIndex=0;
            int count=0;

            for(;j<=end;j++,curIndex++){
                //查找满足条件的
                while(i<=mid&&nums[i]<=2*(long)nums[j]){
                    i++;
                }
                //排序
                while(t<=mid&&nums[t]<nums[j]){
                    copy[curIndex++]=nums[t++];
                }

                //将j放入
                copy[curIndex]=nums[j];
                count+=mid-i+1;
            }

            //防止还有后面大的元素
            while(t<=mid){
                copy[curIndex++]=nums[t++];
            }
            //将数组赋值给nums
            System.arraycopy(copy,0,nums,start,end-start+1);

            return left+count+right;

        }
    }
}