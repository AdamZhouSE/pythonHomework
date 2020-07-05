import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
public class Main {
    public static void printByLevel(Node root) {
        if (root == null) {
            return;
        }
        Queue<Node> queue = new LinkedList<>();
        queue.offer(root);
        int level = 1;
        Node last = root;
        Node nlast = null;
        System.out.print("Level " + level++ + " : ");
        while (!queue.isEmpty()) {
            root = queue.poll();
            if (root == last){
                System.out.print(root.value);
            }else System.out.print(root.value + " ");
            if (root.left != null) {
                queue.offer(root.left);
                nlast = root.left;
            }
            if (root.right != null) {
                queue.offer(root.right);
                nlast = root.right;
            }
            if (root == last && ! queue.isEmpty()) {
                System.out.println();
                System.out.print("Level " + level++ +" : ");
                last = nlast;
            }
        }
    }


    public static void printZigZag(Node root) {
        if (root == null) {
            return;
        }
        Queue<Node> queue = new LinkedList<>();
        queue.offer(root);
        int level = 1;
        Node last = root;
        Node nlast = null;
        boolean judge = false;
        ArrayList<Node> arrayList = new ArrayList<>();
        System.out.print("Level " + level++ + " from left to right: ");
        while (!queue.isEmpty()) {
            root = queue.poll();
            arrayList.add(root);
            if (root.left != null) {
                queue.offer(root.left);
                nlast = root.left;
            }
            if (root.right != null) {
                queue.offer(root.right);
                nlast = root.right;
            }
            if (root == last && !queue.isEmpty()) {
                if (judge) {
                    for (int i = arrayList.size() - 1; i >= 1; i--) {
                        System.out.print(arrayList.get(i).value + " ");
                    }
                    System.out.print(arrayList.get(0).value);
                } else {
                    for (int i = 0; i <= arrayList.size() - 2; i++) {
                        System.out.print(arrayList.get(i).value + " ");
                    }
                    System.out.print(arrayList.get(arrayList.size() - 1).value);
                }
                arrayList.clear();
                judge = !judge;
                System.out.println();
                if (judge) {
                    System.out.print("Level " + level++ + " from right to left: ");
                }else {
                    System.out.print("Level " + level++ + " from left to right: ");
                }
                last = nlast;
            }
        }
        if (judge){
            for (int i = arrayList.size() - 1; i >= 1; i--) {
                System.out.print(arrayList.get(i).value + " ");
            }
            System.out.print(arrayList.get(0).value);
        } else {
            for (int i = 0; i <= arrayList.size() - 2; i++) {
                System.out.print(arrayList.get(i).value + " ");
            }
            System.out.print(arrayList.get(arrayList.size() - 1).value);
        }
    }

    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] strings = br.readLine().split(" ");
        int n = Integer.parseInt(strings[0]);
        int root = Integer.parseInt(strings[1]);
        Node head1 = new Node(root);
        int[][] arr1 = new int[100 + 1][2];
        for (int i = 0; i < n; i++) {
            strings = br.readLine().split(" ");
            arr1[Integer.parseInt(strings[0])][0] = Integer.parseInt(strings[1]);
            arr1[Integer.parseInt(strings[0])][1] = Integer.parseInt(strings[2]);
        }
        createTree(head1, arr1);
        printByLevel(head1);
        System.out.println();
        printZigZag(head1);
        System.out.println();
    }

    public static void createTree(Node head, int[][] arr) {
        if (head == null) {
            return;
        }
        if (arr[head.value][0] != 0) {
            head.left = new Node(arr[head.value][0]);
            createTree(head.left, arr);
        }
        if (arr[head.value][1] != 0) {
            head.right = new Node(arr[head.value][1]);
            createTree(head.right, arr);
        }
    }
}

class Node {
    public int value;
    public Node left;
    public Node right;

    public Node(int data){
        this.value = data;
    }
}