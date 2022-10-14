package tuling;

/**
 * Networks -- provide a connection network with 0 and 1.
 *      Output how many communities it has.
 */

public class ProNum {
    private static int getProNum(int[][] gra){
        int len = gra.length;
        boolean[] isVisited = new boolean[len];
        int res = 0;

        for (int i = 0; i < len; i++) {
            if(!isVisited[i]){
                dfs(isVisited, gra, len, i);
                res++;
            }
        }

        return res;
    }

    private static void dfs(boolean[] isVisited, int[][] gra, int len, int i) {
        for (int j = 0; j < len; j++) {
            if(gra[i][j]==1 && !isVisited[j]){
                isVisited[j] = true;
                // Find out deeper layer first... (i--j--?--?)
                dfs(isVisited, gra, len, j);
            }
        }
    }
}
