import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;
public class Main {
    // 根节点
    private static TireNode root = new TireNode();

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int opNum = in.nextInt();
        while (opNum-- > 0) {
            int op = in.nextInt();
            String str = in.next();
            switch (op) {
                case 1:
                    addNode(str);
                    break;
                case 2:
                    delNode(str);
                    break;
                case 3:
                    System.out.println(ifExitNode(str) ? "YES" : "NO");
                    break;
                case 4:
                    System.out.println(getSubNodeCnt(str));
            }
        }
    }

    private static int getSubNodeCnt(String prefix) {
        TireNode node = root;
        for (char c : prefix.toCharArray()) {
            if (!node.subNode.containsKey(c)) {
                return 0;
            }
            node = node.subNode.get(c);
        }
        return node.cnt;
    }

    private static boolean ifExitNode(String str) {
        TireNode node = root;
        for (char c : str.toCharArray()) {
            if (!node.subNode.containsKey(c)) {
                return false;
            }
            node = node.subNode.get(c);
        }
        return node.end != 0;
    }


    // 删除node的时候 每次只能删一个 即使重复了好几个 每次也只能删一个
    private static void delNode(String str) {
        TireNode node = root;
        for (char c : str.toCharArray()) {
            node = node.subNode.get(c);
            node.cnt--;
        }
        node.end--;
        if (node.cnt == 0) {
            node.subNode = new HashMap<>();
        }
    }

    // 可以重复添加的node
    private static void addNode(String str) {
        TireNode node = root;
        for (char c : str.toCharArray()) {
            if (!node.subNode.containsKey(c)) {
                node.subNode.put(c, new TireNode());
            }
            node = node.subNode.get(c);
            node.cnt++;
        }
        node.end++;
    }




    static class TireNode {
        // 其实可以换成数组
        public Map<Character, TireNode> subNode = new HashMap<>();
        // 多少个单词路过这个节点
        public int cnt = 0;
        // 这个节点是多少个单词的结尾
        // 这点可以重复添加，这是最骚的
        public int end = 0;
    }
}
