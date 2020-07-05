import java.util.Scanner;
import java.util.PriorityQueue;

public class Main {

    public static void main(String[] args){
        Scanner in = new Scanner(System.in);
        while(in.hasNext()){
            int n = in.nextInt();
            PriorityQueue<Integer> q = new PriorityQueue<Integer>();
            for(int i=0;i<n;i++){
                q.add(in.nextInt());
            }
            int ans = 0;
            while(q.size()>1){
                int first = q.poll();
                int sec = q.poll();
                ans += (first + sec);
                q.add(first+sec);
            }
            System.out.println(ans);
        }
    }
}
