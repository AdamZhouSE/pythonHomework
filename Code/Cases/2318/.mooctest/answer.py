import java.util.*; 
import java.io.*;
public class Main{
    public static void main(String[] args)throws IOException{
        BufferedReader bufr = new BufferedReader(new InputStreamReader(System.in));
        String[] nm = bufr.readLine().split(" ");
        int n  = Integer.valueOf(nm[0]);
        int m = Integer.valueOf(nm[1]);
        Node tree = buildTree(bufr);
        System.out.println(process(tree).maxBSTSize);
    }
    public static Node buildTree(BufferedReader bufr)throws IOException{
         int left ,right,data;
        String[] datas = bufr.readLine().split(" ");
        data = Integer.valueOf(datas[0]);
        right = Integer.valueOf(datas[2]);
        left = Integer.valueOf(datas[1]);
        Node head = new Node(data);
        if(left!=0){
            head.left = buildTree(bufr);
        }
        if(right!=0){
            head.right = buildTree(bufr);
        }
        return head;
    }                                                           
    public static ReturnType process(Node x){                                     //树形dp四个步骤
        if(x==null){
            return new ReturnType(null,0,Integer.MAX_VALUE,Integer.MIN_VALUE);   //第一步： 边界情况
        }
        ReturnType lData = process(x.left);                 //第二步：     //默认得到左树全部信息
        ReturnType rData = process(x.right);                              //默认得到右树全部信息
                                                            //第三步：信息整合
        int min = Math.min(x.data,Math.min(lData.min,rData.min));
        int max  = Math.max(x.data,Math.max(lData.max,rData.max));
        int maxBSTSize = Math.max(lData.maxBSTSize,rData.maxBSTSize);
        Node maxBSTHead = lData.maxBSTSize>=rData.maxBSTSize?lData.maxBSTHead:rData.maxBSTHead;
        if(lData.maxBSTHead == x.left&&rData.maxBSTHead==x.right&&x.data>lData.max&&x.data<rData.min){
            maxBSTSize = lData.maxBSTSize+rData.maxBSTSize+1;
            maxBSTHead  = x;
        }
        return new ReturnType(maxBSTHead,maxBSTSize,min,max);   //第四步：返回
    }
}
class Node{
    int data;
    Node right;
    Node left;
    Node(int data){
        this.data = data;
    }
}
class ReturnType{
    public Node maxBSTHead;
    public int maxBSTSize;
    public int min;
    public int max;
    public ReturnType(Node maxBSTHead,int maxBSTSize,int min,int max){
        this.maxBSTHead = maxBSTHead;
        this.maxBSTSize = maxBSTSize;
        this.min = min;
        this.max = max;
    }
}