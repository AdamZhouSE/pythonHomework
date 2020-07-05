import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    public static void findSubNode(Node root) {

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
        int t = Integer.parseInt(br.readLine());
        if (arr1[t][0] == 0 && arr1[t][1] == 0){
            System.out.println(0);
        } else if(arr1[t][0] != 0){
            System.out.println(arr1[t][0] );
        }else {
            System.out.println(arr1[t][1] );
        }
//        createTree(head1, arr1);
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


