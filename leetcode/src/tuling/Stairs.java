package tuling;

import java.util.HashMap;
import java.util.Map;

/** 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

        每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

         

        示例 1：

        输入：n = 2
        输出：2
        解释：有两种方法可以爬到楼顶。
        1. 1 阶 + 1 阶
        2. 2 阶
        示例 2：

        输入：n = 3
        输出：3
        解释：有三种方法可以爬到楼顶。
        1. 1 阶 + 1 阶 + 1 阶
        2. 1 阶 + 2 阶
        3. 2 阶 + 1 阶
         

        提示：

        1 <= n <= 45
 **/

/**
 * 使用一个hash表存储，可以直接调用已有结果，无需再次迭代
 */

public class Stairs {
    private final Map<Integer, Integer> storeMap = new HashMap<>();

    public Stairs() {
        storeMap.put(0, 1);
        storeMap.put(1, 1);
    }

    public int climbStairs(int sum){
        if(sum<0){
            return -1;
        }
        if(storeMap.get(sum) != null){
            return storeMap.get(sum);
        } else{
            int res = climbStairs(sum-1)+climbStairs(sum-2);
            storeMap.put(sum, res);
            return res;
        }
    }
}
