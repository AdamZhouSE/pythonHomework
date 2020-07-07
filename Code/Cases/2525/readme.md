### 题目描述

你打算利用空闲时间来做兼职工作赚些零花钱。

这里有 n 份兼职工作，每份工作预计从 startTime[i] 开始到 endTime[i] 结束，报酬为 profit[i]。

给你一份兼职工作表，包含开始时间 startTime，结束时间 endTime 和预计报酬 profit 三个数组，请你计算并返回可以获得的最大报酬。

注意，时间上出现重叠的 2 份工作不能同时进行。

如果你选择的工作在时间 X 结束，那么你可以立刻进行在时间 X 开始的下一份工作。

1 <= startTime.length == endTime.length == profit.length <= 5 * 10^4

1 <= startTime[i] < endTime[i] <= 10^9

1 <= profit[i] <= 10^4

### 输入描述

```
三个数组分布在三行，开始时间 startTime，结束时间 endTime 和预计报酬 profit
```
### 输出描述

```
返回可以获得的最大报酬。
```

### 测试样例
#### 样例1: 输入-输出-解释
```
[1,2,3,3]
[3,4,5,6]
[50,10,40,70]
```
```
120
```
```
我们选出第 1 份和第 4 份工作， 
时间范围是 [1-3]+[3-6]，共获得报酬 120 = 50 + 70。
```
<p align="">
	<img src="http://mooctest-code.oss-cn-shanghai.aliyuncs.com/static/media/%E8%A7%84%E5%88%92%E5%85%BC%E8%81%8C%E5%B7%A5%E4%BD%9C.png" alt="Sample"  width="350" height="140">
</p>

### 题目来源  
`LeetCode`