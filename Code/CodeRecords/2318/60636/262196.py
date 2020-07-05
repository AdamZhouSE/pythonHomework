



    private int min;
    private int max;
    private int size;

    static class Node {
        int val;
        Node left;
        Node right;

        Node(int val){
            this.val = val;
        }
    }


    public Node biggestSubTree(Node root){
        return dfs(root);
    }

    private Node dfs(Node root){
        if(root==null){
            min = 0;
            max = 0 ;
            size = 0;
            return null;
        }else{
            Node lNode = dfs(root.left);
            int lMin = min;
            int lMax = max;
            int lSize = size;
            Node rNode = dfs(root.right);
            int rMin = min;
            int rMax = max;
            int rSize = size;
            if(lNode == null && rNode==null){
                size = 1;
                min = root.val;
                max = root.val;
                return root;
            }else if (lNode == root.left && rNode == root.right
                    && root.val >= lMax && root.val <= rMin) {
                size = lSize + rSize + 1;
                min = lMin;
                max = rMax;
                return root;
            } else {
                min = lMin;
                min = Math.min(min,root.val);
                min = Math.min(min,rMin);
                max = lMax;
                max = Math.max(max,root.val);
                max = Math.max(max,rMax);
                size = lSize>rSize?lSize:rSize;
                return lSize>rSize?lNode:rNode;
            }
        }
    }
 