public TreeNode biggestSubBST(TreeNode head) {
    int[] record = new int[3];

    return posOrder(head, record);
}

//整体过程是后序遍历
public TreeNode posOrder(TreeNode head, int[] record) {
    if (head == null) {
        record[0] = 0;
        record[1] = Integer.MAX_VALUE;
        record[2] = Integer.MIN_VALUE;

        return null;
    }

    int value = head.value;
    TreeNode left = head.left;
    TreeNode right = head.right;

    TreeNode lBST = posOrder(left, record); //左子树上最大搜索二叉树的头节点
    int lSize = record[0];
    int lMin = record[1];
    int lMax = record[2];

    TreeNode rBST = posOrder(right, record); //右子树上最大搜索二叉树的头节点
    int rSize = record[0];
    int rMin = record[1];
    int rMax = record[2];

    record[1] = Math.min(lMin, value); //最小值
    record[2] = Math.max(rMax, value); //最大值

    //以node为头的整棵树都为搜索二叉树
    if (left == lBST && right == rBST && lMax < value && value < rMin) {
        record[0] = lSize + rSize + 1; //节点数

        return head;
    }

    //以node的左子树或者右子树为头的子树为搜索二叉树
    record[0] = Math.max(lSize, rSize); //节点数

    return lSize > rSize ? lBST : rBST;
}

