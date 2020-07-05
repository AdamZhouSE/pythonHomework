import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        if(n<3){
            System.out.println(n);
        }else{
            int[] height = new int [n];
            int[] binary = new int[n];
            height[0] = 1;
            int max = 0;
            for(int i = 0;i<n-1;i++){
                int parent = in.nextInt();
                int child = in.nextInt();
                binary[parent] += 1;
                if(binary[parent] < 3) {
                    height[child] = height[parent] + 1;
                }
                max = Math.max(max, height[child]);
            }
            System.out.println(max);
        }
    }
}
