import java.lang.StringBuilder;

/**
 * Find out longest same part of two strings.
 *
 * Examples:
 *      input: 3 (length of first string), 4 (length of second string), ads (first string), adds (second string)
 *      output: ad
 */

public class LongestSameSubstr{
    public static String engine(int m, int n, String text1, String text2) {
        // initialize
        String[][] stage = new String[m][n];
        String[][] dp = new String[m][n];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                stage[i][j] = "";
                dp[i][j] = "";
            }
        }

        // cope with edges
        for (int i = 0; i < m; i++) {
            if(text1.charAt(i) == text2.charAt(0)){
                for (int j = i; j < m; j++) {
                    if(j==i){
                        stage[j][0] = Character.toString(text2.charAt(0));
                    }
                    StringBuilder sb2 = new StringBuilder(Character.toString(text2.charAt(0)));
                    dp[j][0] = sb2.toString();
                }
                break;
            }
        }
        for (int i = 0; i < n; i++) {
            if(text2.charAt(i) == text1.charAt(0)){
                for (int j = i; j < n; j++) {
                    if(j==i){
                        stage[0][j] = Character.toString(text1.charAt(0));
                    }
                    StringBuilder sb1 = new StringBuilder(Character.toString(text1.charAt(0)));
                    dp[0][j] = sb1.toString();
                }
                break;
            }
        }
        
        // 1-dimension sample
        if(m==1 || n==1){
            return dp[m-1][n-1];
        }

        // dynamic routine
        for (int i = 1; i < m; i++) {
            char c1 = text1.charAt(i);
            for (int j = 1; j < n; j++) {
                char c2 = text2.charAt(j);
                // core codes --------------------------------------------------------------
                if (c1 == c2) {
                    // generate stage first
                    StringBuilder sb = new StringBuilder(stage[i-1][j-1]);
                    sb.append(c1);
                    stage[i][j] = sb.toString();

                    // cooperate stage and dp
                    if(dp[i-1][j-1].length() < stage[i][j].length()){
                        dp[i][j] = stage[i][j];
                        continue;
                    }
                }
                dp[i][j] = (dp[i - 1][j].length() >=  dp[i][j - 1].length()) ? dp[i - 1][j] : dp[i][j - 1];
                //----------------------------------------------------------------------------
            }
        }
        return dp[m-1][n-1];
    }
}