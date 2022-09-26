import java.util.Scanner;
import tuling.*;

public class Main{

    public static void main(String[] args) {
//        // Longest substring
//        Scanner sc = new Scanner(System.in);
//        int m = sc.nextInt();
//        int n = sc.nextInt();
//        String text1 = sc.next();
//        String text2 = sc.next();
//        sc.close();
//        System.out.println(LongestSameSubstr.engine(m, n, text1, text2));

        Scanner sc = new Scanner(System.in);
        int sum = sc.nextInt();
        sc.close();
        Stairs stairs = new Stairs();
        System.out.println(stairs.climbStairs(sum));
    }
}
