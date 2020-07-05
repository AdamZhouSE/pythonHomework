import java.util.HashMap;
import java.util.Scanner;
public class Main {
    static int max_length = 0;

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String [] first = in.nextLine().split(" ");
        int n = Integer.parseInt(first[0]);
        int root = Integer.parseInt(first[1]);
        int [][] nodes = new int[n][4];
        for(int i = 0;i < n;i ++) {
            String[] str = in.nextLine().split(" ");
            int row = Integer.parseInt(str[0]);
            for(int j = 0;j < 4;j++){
                nodes[row-1][j] = Integer.parseInt(str[j]);
                //使用数组来存放节点，每行第一个数-1确定节点所在的行。
                // 该行第一个元素代表根节点，第二个元素是其左子树，第三个元素是右子树，第四个是val
            }
        }
        int target = Integer.parseInt(in.nextLine());
        HashMap<Integer, Integer> map = new HashMap<>();
        ////key代表出现过的累加和，value代表这个累加和上次在哪一层出现的
        map.put(0, 0);   //一定要有，代表累加和为0的最早在0层就出现
        maxLength(nodes, root, target, map, 0,1);
        System.out.println(max_length);
    }


    public static void maxLength(int[][] nodes, int root, int target, HashMap<Integer, Integer> map, int preSum, int level){
        if(root == 0)
            return;
        int curSum = preSum + nodes[root-1][3];
        //当之前还没有出现过累加和为curSum的时候，加入map
        if(!map.containsKey(curSum)){
            map.put(curSum, level);
        }
        //比如说level为5时，curSum = 13,target = 5，那么就要看之前有没有和为8的出现
        //发现了level为2时，累加和为8
        //那么这里的max_length就可以试着更新为5-2 = 3.
        //之所以这么说，是因为有个关系一直存在，target = curSum - preSum.这是我们追求的
        //我们往map里加的都是preSum,所以就找curSum - target，使得追求的东西被实现
        if(map.containsKey(curSum - target)){
            max_length = Math.max(max_length, level - map.get(curSum - target));
        }
        //继续查找左右子树
        maxLength(nodes, nodes[root-1][1], target, map, curSum, level+1);
        maxLength(nodes, nodes[root-1][2], target, map, curSum, level+1);
        //我们在map中存放的是上层所有的和，以及他们对应的level，
// 而如果在map中发现了curSum，且它的level不是上层，而且是当前这一层，那么说明curSum这个累加和的记录是在遍历到cur的时候加上去的
////那么就需要将这个记录删除掉，免得后面使用它。因为它并不是代表的上层的多少个数的和值。
        if(map.get(curSum) == level)
            map.remove(curSum);
    }
}
