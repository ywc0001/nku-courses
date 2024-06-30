>**2024春期末考题回忆**
>- 程序题：矩阵快速幂；斐波那契数列的记忆化搜索解法；一个数列中第K小的数，要求时间复杂度为O（n）
>- 简答题：主定理公式以及各个参数意义，$log_b a$和d进行比较的意义；a的n次幂的前K项和的递推（要求时间复杂度为$n^3\log {n}$）。
>- 选择题：当代计算机一秒内执行$10^8$条基本语句；双向广度优先搜索是哪个级别的优化（算法）；快速排序有多少种输入，达到$n^2$复杂度的输入有几种；状态变量可以是？；在开关灯游戏中，多少种状态？
---

**一些概念**
（理解，不用背）

>  - 当代计算机一秒内可执行$10^8$条基本语句。
>    
>  - 算法的时间复杂度是一个函数，修饰一段代码或算法，由问题的输入规模确定，也即执行的基本语句数。（输入规模为问题自变量，从严谨的角度来看，问题的输入规模由输入数据的内存规模来定义，而非由一个值来定义）
> O：关注重要部分；保留增长最快的部分。（O是时间复杂度记号）   
> 常见的大O运行时间：
>  O($log n$)，对数时间，如二分查找
> O(n)，线性时间，如简单查找 
> O($n*log n$)，如快速排序 
> O($n^2$)，如选择排序 O(n!)，如旅行商问题
> 
> - 算法的判定问题：判断一个问题的解是否存在；优化问题：找到问题的最优解。面对一个问题，先判断是判别问题还是优化问题，然后找到解空间：什么是可行解，最优解？
> 
> - 状态是对可计算问题的一种建模；状态转移是状态通过操作变成另一个状态；状态变量是状态变化的不同取值表示；价值函数，用以衡量当前状态的一个状态到值的映射，该值会伴随着状态转移而更新，该值可以是：布尔值、整数、实数等。
> 状态空间是一个图，不是由点和边组成，是由状态和状态转移组成。
> 
> - 解决问题的四个层次——问题，模型，算法，代码。时间复杂度与问题规模与基本语句有关，是修饰算法级别的量。 
> 快速傅里叶变换优化了哪个环节？是问题级别的优化。 
> 快速排序的时间复杂度：O($n\log {n}$)；快速排序是原位排序，不会占用额外内存。
> 
> - 为什么二分代码要用左闭右开区间？因为闭区间在判断空集时有弊端；而开区间在区间拼接时有弊端；因此半开半闭区间有优势——因此对于二分代码，要用左闭右开区间
> - 动态规划：在给定约束条件下找到最优解，在问题可分解为彼此独立且离散的子问题时，可使用动态规划解决。每种动态规划解决方案都涉及网格，单元格中的值通常就是要优化的值，每个单元格都是一个子问题。

练习题（看网站提供的题解思路）：
https://www.luogu.com.cn/contest/166636#problems；https://www.luogu.com.cn/contest/175291


**!!!很可能会考的：二分，矩阵快速幂，DFS,BFS**

## 矩阵快速幂算法
通常用于解决斐波那契数列等递归关系问题，核心思想是将幂次分解为二进制形式，通过平方和乘法快速计算结果。（这个要能手写下来）

可将斐波那契数列的时间复杂度降为O（$\log {n}$）
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/392c068901b9447fa3266d36c63350f4.png)
[求矩阵幂前K项和的思路](https://nankai.feishu.cn/docx/Dlc2drGNRouHIKxeDlqcT7LHnqH?from=from_copylink)

代码
```cpp

Matrix QuickPow(Matrix A, int n){
    if(n==1) return A;
    Matrix half = QuickPow(A, n/2);
    if(n%2 == 1) return A * half * half;
    else return half * half;
}

```
## 记忆化搜索
原理：将函数调用的结果存储起来，适用于递归算法
```cpp
//计算斐波那契数列
int f(int n){
    if(a[n]>0)
        return a[n];
    if(n<=2)
        return 1;
    return a[n] = f(n-1)+f(n-2);

}
```
## 快速排序
原理：通过选择一个基准元素，将数组分为两部分，一部分小于基准，另一部分大于基准，然后对这两部分递归进行排序。

```cpp
 //zjy版  
// 快速排序函数  
void quicksort(vector<int>& a, int l, int r) {   
    if (r - l <= 0) { // 如果区间内没有元素或只有一个元素，则无需排序  
        return;  
    }  
    int pivot = a[l]; // 选择第一个元素作为基准值  
    int s = 0; // 用于记录小于基准值的元素数量  
    for (int i = l + 1; i < r; i++) {  
        if (a[i] < pivot) {  
            s++;  
        }  
    }  
    int p = l + s; // p是小于基准值的元素应该放置的位置  
    swap(a[l], a[p]); // 将基准值放到正确的位置  
  
    // 三路划分，但在这个实现中只使用了两路划分  
    int i = l, j = p + 1;  
    while (i < p && j < r) {  
        while (i < p && a[i] < pivot) i++;   
        while (j < r && a[j] >= pivot) j++;  
        if (i < p && j < r) {  
            swap(a[i], a[j]);  
        }  
    }  
  
    // 递归对基准值左右两侧的子数组进行排序  
    quicksort(a, l, p);  
    quicksort(a, p + 1, r);  
}  
  
int main() {  
    int n;  
    while (cin >> n) { // 读取要排序的整数数量  
        vector<int> a(n);  
        for (int i = 0; i < n; i++) {  
            cin >> a[i]; // 读取整数并存储到vector中  
        }  
  
        // 调用快速排序函数  
        quicksort(a, 0, n); // 注意：这里应该是n-1，因为数组索引是从0到n-1  
  
        // 输出排序后的数组  
        for (int i = 0; i < n; i++) {  
            cout << a[i] << " ";  
        }  
        cout << endl;  
    }  
    return 0;   
}  
   
```



## 归并排序
原理：将数组分成两半，分别进行排序，然后合并这两部分。这个过程递归进行，直到每部分的长度为1，最后进行合并。


例题:https://www.luogu.com.cn/problem/P1908




## 二分查找
!!! 二分是必考
原理：每次比较时，将搜索范围减半，直到找到元素或范围为空。

```cpp
//zjy的版本
  
// 定义一个常量maxn，用于数组的大小，这里假设最多有1e5+5个元素  
const int maxn = 1e5+5;  
// 定义一个全局数组a，用于存储输入的整数  
int a[maxn];  
// 定义全局变量n和k，分别用于存储数组a的长度和需要达到的目标值  
int n, k;  
// 定义全局变量maxL，用于存储数组a中的最大值  
int maxL;  
  
// 定义函数cut，用于计算数组a中所有元素除以L后的和  
int cut(int L) {  
    int s = 0; // 初始化和s为0  
    for(int i = 0; i < n; i ++) { // 遍历数组a  
        s += a[i] / L; // 累加每个元素除以L的商  
    }  
    return s; // 返回累加和s  
}  
  
// 定义函数bs，用于通过二分查找找到满足cut(L) >= v的最小L值  
int bs(int v) {  
    int l = 1, r = maxL + 1; // 定义二分查找的左右边界  
    while(l < r) { // 当左边界小于右边界时继续查找  
        int mid = l + (r-l)/2; // 计算中间值mid  
        //if(-cut(mid) <= -v) { // 原代码中的比较逻辑是多余的，因为cut函数返回的是非负整数  
        if(cut(mid) >= v) { // 如果cut(mid)的值大于等于目标值v  
            l = mid+1; // 更新左边界为mid+1，继续向右查找  
        } else {  
            r = mid; // 否则更新右边界为mid，向左查找  
        }  
    }  
    return l - 1; // 返回最终查找到的最小L值（注意需要减去1，因为最后l会超出目标值）  
}  
  
int main() {  
    ios::sync_with_stdio(false); // 关闭C++标准库与C标准库的同步，加速输入输出  
    cin >> n >> k; // 读取数组长度n和目标值k  
    maxL = 0; // 初始化maxL为0  
    for(int i = 0; i < n; i ++) { // 遍历数组a  
        cin >> a[i]; // 读取每个元素的值  
        maxL = max(a[i], maxL); // 更新maxL为当前元素和maxL中的较大值  
    }  
    cout << bs(k) << endl; // 调用bs函数，输出满足cut(L) >= k的最小L值  
    return 0; 
}
```
二分查找的写法很多，以这道题为例
[搜索插入位置](https://leetcode.cn/problems/search-insert-position/description/)

>给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

```cpp
//解法一
public class Solution {

    public int searchInsert(int[] nums, int target) {
        // 不用判断数组为空，因为题目最后给出的数据范围说数组不为空
        int len = nums.length;
        // 特殊判断
        if (nums[len - 1] < target) {
            return len;
        }

        // 程序走到这里一定有 nums[len - 1] >= target，插入位置在区间 [0..len - 1]
        int left = 0;
        int right = len - 1;
        // 在区间 nums[left..right] 里查找第 1 个大于等于 target 的元素的下标
        while (left < right) {
            int mid = (left + right) / 2;
            if (nums[mid] < target){
                // 下一轮搜索的区间是 [mid + 1..right]
                left = mid + 1;
            } else {
                // 下一轮搜索的区间是 [left..mid]
                right = mid;
            }
        }
        return left;
    }
}

//解法二
public class Solution {

    public int searchInsert(int[] nums, int target) {
        int len = nums.length;
        int left = 0;
        int right = len;
        // 在区间 nums[left..right] 里查找第 1 个大于等于 target 的元素的下标
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] < target){
                // 下一轮搜索的区间是 [mid + 1..right]
                left = mid + 1;
            } else {
                // 下一轮搜索的区间是 [left..mid]
                right = mid;
            }
        }
        return left;
    }
}

//解法三
class Solution {
    public int searchInsert(int[] nums, int target) {
        int n = nums.length;
        int left = 0, right = n - 1, ans = n;
        while (left <= right) {
            int mid = ((right - left) >> 1) + left;
            if (target <= nums[mid]) {
                ans = mid;
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        return ans;
    }
}

//解法四
class Solution {
    public int searchInsert(int[] nums, int target) {
        int left = 0, right = nums.length - 1;
        while(left <= right) {
            int mid = (left + right) / 2;
            if(nums[mid] == target) {
                return mid;
            } else if(nums[mid] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return left;
    }
}


```


一些例子
题目：https://www.luogu.com.cn/problem/P2678
```cpp
//二分，贪心
bool canAchieveMinJump(const vector<int>& distances, int N, int M, int minJump){
    int removeCount = 0;
    int lastPos = 0;

    for(int i = 1; i<=N;++i){
        if(distances[i] -lastPos< minJump){
            removeCount++;
            if(removeCount > M) return false;
        } else {
            lastPos = distances[i];
        }
    }
    return true;
}
int findMaxMinJumpDistance(const vector<int>& distances, int N, int M, int L){
    int left = 1;
    int right = L;
    int result = 0;

    while(left <= right){
        int  mid = left + (right-left) / 2;
        if(canAchieveMinJump(distances, N, M, mid)){
            result = mid;
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }

    return result;
}
int main() {
    int L, N, M;
    cin >> L >> N >> M;

    vector<int> distanceToStart(N+2);
    distanceToStart[0] = 0;
    distanceToStart[N+1] = L;

    for(int i = 1; i <= N;++i){
        cin >> distanceToStart[i];
    }

    sort(distanceToStart.begin(), distanceToStart.end());
    int maxMinJump = findMaxMinJumpDistance(distanceToStart, N, M, L);
    cout << maxMinJump << endl;
    return 0;
}
```
题目：https://www.luogu.com.cn/problem/P2370
```cpp
//二分
#include <bits/stdc++.h>
using namespace std;

class USB{
public:
    int p;//最小价值
    int S;//U盘大小
    USB(int _p, int _S): p(_p), S(_S){}
};

class File{
public:
    int w;//文件大小
    int v;//文件价值
};

void findMinConnecterSize(vector<File>& files, USB& usb, int n){
    int maxV = 0;
    for(auto f:files){
        maxV += f.v;
    }
    if(maxV < usb.p) {
        cout << "No Solution!" << endl;
        return;
    }

   int left = 1, right = 1e9, result = -1;
    while(left <= right){
        int mid = left + (right - left) / 2;

        vector<int> dp(usb.S+1, 0);
        for(int i = 0; i < n; ++i){
            if(files[i].w <= mid){
                //j代表当前u盘剩余容量,dp[j]表示当前剩余容量 j 下的最大价值
                for(int j = usb.S; j >= files[i].w; --j){
                    dp[j] = max(dp[j], dp[j-files[i].w] + files[i].v);
                }
            }
        }

        bool found = false;
        for(int j = 0; j<=usb.S; ++j){
            if(dp[j] >= usb.p){
                found = true;
                break;
            }
        }

        if(found){
            result = mid;
            right = mid - 1;
        } else {
            left = mid + 1;
        }
    }
    
    if(result == -1){
        cout << "No Solution!" << endl;
    } else {
        cout << result << endl;
    }
}


int main() {
    int n;
    int p, S;

    cin >> n >> p >> S;
    USB usb = USB(p, S);

    vector<File> files(n);
    for (int i = 0; i < n; ++i) {
        cin >> files[i].w >> files[i].v;
    }

    findMinConnecterSize(files, usb, n);

    return 0;
}
```

## 分治算法

原理：将一个复杂的问题分解为较小的子问题，递归地解决这些子问题（如果子问题足够小，则直接解决），最后合并其结果得到最终解.

归并排序，快速傅里叶变换采用的就是分治算法

## 背包问题
有一个容量为V的背包，还有n个物体，只要背包的剩余容量大于等于物体体积，那就可以装进背包里。每个物体都有两个属性，即体积w和价值v。
如何向背包装物体才能使背包中物体的总价值最大？
```cpp
#include <bits/stdc++.h>
using namespace std;
int main() {
    vector<int> w, v;//重量，价值
    vector<int> f;

    int V,n;//容量，物体数
    while(cin >> V >> n){
        w.push_back(0);
        v.push_back(0);
        for(int i = 1; i <= n; i++){
            cin >> w[i] >> v[i];
        }

        f = vector<int>(V+1, 0);
        for(int i = 1; i <= n; i++){
            for(int j = V; j>=w[i];j--){
                f[j] = max(f[j], f[j-w[i]]+v[i]);
            }
        }
        	//输出答案
		int ans = f[V];
		cout << ans << endl;
    }
    return 0;
}
```


