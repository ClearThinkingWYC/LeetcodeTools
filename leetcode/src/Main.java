import LongestSameSubstr;

public class Main{

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int m = sc.nextInt();
        int n = sc.nextInt();
        String text1 = sc.next();
        String text2 = sc.next();
        sc.close();
        LongestSameSubstr.engine(m, n, text1, text2);
    }
}
