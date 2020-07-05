//完全二叉树
    public static boolean isCBT(Node head){
        if(head==null){
            return true;
        }
        Queue<Node> queue=new LinkedList<Node>();
        boolean leaf=false;
        Node l=null;
        Node r=null;
        queue.offer(head);
        //boolean offer(E e)
        //Inserts the specified element into this queue if it is possible to do so immediately without violating capacity restrictions
        //E poll() 
        //return the head of this queue, or null if this queue is empty
        while(!queue.isEmpty()){
            head=queue.poll();
            l=head.left;
            r=head.right;
            if((leaf&&(l!=null||r!=null)) || (l==null&&r!=null)){
                //当前节点并不是左右孩子都有，那之后的节点必须都为叶节点，否则false
                //有右孩子没有左孩子 false
                return false;
            }
            if(l!=null){
                queue.offer(l);
            }
            if(r!=null){
                queue.offer(r);
            }else{//无右孩子，则后面的节点都为叶节点了
                leaf=true;
            }
        }
        return true;
    }