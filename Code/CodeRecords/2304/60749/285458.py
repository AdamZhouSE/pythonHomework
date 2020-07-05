
//二叉树的按层打印与ZigZag打印

import java.util.*;

public class ZigzagPrint{

	

	//二叉树节点的定义

	public static class Node

	{

 

		public int value;

 

		public Node left;

 

		public Node right;

 

		public Node(int data)

		{

			this.value=data;

		}

	}

   

   //二叉树按照层打印(运用队列的方式打印)

	public static void LayerPrint(Node head)

    {

        if(head==null)

        {

        	return;

        }

     

       /**

       //运用栈的方式不正确

        Stack<Node>stack=new Stack<Node>();

        stack.push(head);

        while(!stack.isEmpty())

        {

        	head=stack.pop();

        	System.out.print(head.value);



        	if(head.right!=null)

        	{

	          stack.push(head.right);

        	}

        	if(head.left!=null)

        	{

	          stack.push(head.left);

        	}

	

        }

       */

        //运用队列的方式存储

        Queue<Node>queue=new LinkedList<Node>();

        int level=1;

        Node last=head; //当前行的最后节点

        Node nlast=null; //下一行的最后节点

        queue.offer(head);

        System.out.print("Level"+(level++)+":");

        while(!queue.isEmpty())

        {

             head=queue.poll();

             System.out.print(head.value+" ");

             if(head.left!=null)

             {

             	//左节点压入队列

             	queue.offer(head.left);

             	nlast=head.left;

             }

             if(head.right!=null)

             {

             	//右节点压入队列

             	queue.offer(head.right);

             	nlast=head.right;

             }

             //换到下一行打印

             if(head==last&&!queue.isEmpty())

             {

             	System.out.print("\nlevel"+(level++)+":");

             	last=nlast;  //换到下一行的最后一个元素

             }

 

        } 

        

          System.out.println();   

 

    }

 

    //二叉树按照Ziazag打印(利用双端队列)

   public static void ZigzagPrint(Node head)

   {

       if(head==null)

        {

        	return;

        }

        /**

        System.out.print(head.value);



        if(head.right!=null)

        {

        System.out.print(head.right.value);        	

        }

        if(head.left!=null)

        {

          System.out.print(head.left.value);

        }

        */

         //运用双端队列的方式存储(基数行左->右,偶数行右->左)

        Deque<Node>dq=new LinkedList<Node>();  //双端队列

        int level=1;

        boolean lr=true;  //记录打印的方向

        Node last=head; //当前行的最后节点

        Node nlast=null; //下一行的最后节点

        dq.offerFirst(head);

        printLevelAndOrientation(level++,lr);

        while(!dq.isEmpty())

        {

             if(lr) //奇数行(尾进头出)

             {

             	head=dq.pollFirst();

             	if(head.left!=null)

             	{

             		nlast=nlast==null?head.left:nlast;

             		dq.offerLast(head.left);

             	}

             	if(head.right!=null)

             	{

             		nlast=nlast==null?head.right:nlast;

             		dq.offerLast(head.right);

             	}

 

             }else //偶数行(头进尾出)

             {

             	head=dq.pollLast();

             	if(head.right!=null)

             	{

             		nlast=nlast==null?head.right:nlast;

             		dq.offerFirst(head.right);

             	}

             	if(head.left!=null)

             	{

             		nlast=nlast==null?head.left:nlast;

             		dq.offerFirst(head.left);

             	}

             }

             System.out.print(head.value+" ");

 

             if(head==last&&!dq.isEmpty())

             {

             	lr=!lr; //进行换行的操作

             	last=nlast;

             	nlast=null;

             	System.out.println();

             	printLevelAndOrientation(level++,lr);

             }

 

        }

        System.out.println();

 

   }

 

   //显示打印的方向

   public static void printLevelAndOrientation(int level,boolean lr)

   {

   	   System.out.print("Level"+level+" from ");

   	   System.out.print(lr?"left to right ":"right to left: ");

   }

  

 

	public static void  main(String []args)

	{

 

       Node node=new Node(1);

       node.left=new Node(2);

       node.right=new Node(3);

       node.left.left=new Node(4);

       node.right.left=new Node(5);

       node.right.right=new Node(6);

       node.right.left.left=new Node(7);

       node.right.left.right=new Node(8);

 

       System.out.println("按照层遍历:");

       LayerPrint(node);

       System.out.println("按照Zigzag遍历:");

       ZigzagPrint(node);

 

 

	}

}


