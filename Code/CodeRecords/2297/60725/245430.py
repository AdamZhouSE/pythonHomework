import java.util.Scanner;
import java.util.LinkedList;
import java.util.ArrayList;
class TreeNode
{
    int data;
    int level;
    TreeNode left;
    TreeNode right;
    TreeNode(int data)
    {
        this.data = data;
    }
}

public class Main
{
    static ArrayList<Integer> list1 = new ArrayList<Integer>();
    public static void main(String args[])
    {
        Scanner sc =new Scanner(System.in);
        LinkedList<TreeNode> list = new LinkedList<TreeNode>();
       
        while(sc.hasNext())
        {
            int n = sc.nextInt();
            int a[] = new int[n];
            for(int i=0;i<n;i++)
            {
                a[i] = sc.nextInt();
            }
            TreeNode root = new TreeNode(a[0]);
            root.level = 1;
            list.add(root);
            for(int i=1;i<n;i++)
            {
                insert(root,list,a[i]);
            }
             list.clear();//要及时清除内容，否则后面有continue就结束循环了。
            int l = sc.nextInt();
             preorder(root,l);
            if(list1.size()==0)
            {
                System.out.println("EMPTY");
                continue;                
            }    
            else
            {
                for(int i=0;i<list1.size()-1;i++)
                {
                    System.out.print(list1.get(i)+" ");
                }
                System.out.println(list1.get(list1.size()-1));
              
            }
            list1.clear();
           
        }
    }
    public static void insert(TreeNode root,LinkedList<TreeNode> list,int data)
    {
        TreeNode tmp ;
        int max = 0;
        if(!list.isEmpty())
        {
            tmp = list.removeFirst();
            if(tmp.left==null)
            {
                tmp.left = new TreeNode(data);
                tmp.left.level = tmp.level+1; 
                max = tmp.level+1;
                list.addLast(tmp.left);
            }    
            else if(tmp.right==null)
            {
                tmp.right = new TreeNode(data);
                tmp.right.level = tmp.level+1;
                max = tmp.level+1;
                list.addLast(tmp.right);
            }
            if(tmp.left==null||tmp.right==null)
            {
                list.addFirst(tmp);
            }
        }
    }
    
    public static void preorder(TreeNode root,int l)
    {
    	if(root==null)
    		return ;
        if(root.level==l)
            list1.add(root.data);
        preorder(root.left,l);
        preorder(root.right,l);
    }