# [Maximum of Minimum Values in All Subarrays][title]

## Description

给你一个长度为 `n` 的整数数组 `nums` ，你需要处理 `n` 个查询。

对于第 `i` （`0 <= i < n`）个查询：

  1. 你需要先找出 `nums` 的所有长度为 `i + 1` 的子数组中的 **最小值** 。
  2. 在这些最小值中找出 **最大值** 作为答案。

返回一个 **下标从 0 开始** 的长度为 `n` 的整数数组 `ans` ，`ans[i]` 代表第 `i` 个查询的答案。



**示例 1：**
            **输入:** nums = [0,1,2,4]    **输出:** [4,2,1,0]    **解释:**    i = 0:    - 大小为 1 的子数组为 [0], [1], [2], [4]    - 有最大的最小值的子数组是 [4], 它的最小值是 4    i = 1:    - 大小为 2 的子数组为 [0,1], [1,2], [2,4]    - 有最大的最小值的子数组是 [2,4], 它的最小值是 2    i = 2:    - 大小为 3 的子数组为 [0,1,2], [1,2,4]    - 有最大的最小值的子数组是 [1,2,4], 它的最小值是 1    i = 3:    - 大小为 4 的子数组为 [0,1,2,4]    - 有最大的最小值的子数组是 [0,1,2,4], 它的最小值是 0

**示例 2：**
            **输入:** nums = [10,20,50,10]    **输出:** [50,20,10,10]    **解释:**    i = 0:     - 大小为 1 的子数组为 [10], [20], [50], [10]    - 有最大的最小值的子数组是 [50], 它的最小值是 50    i = 1:     - 大小为 2 的子数组为 [10,20], [20,50], [50,10]    - 有最大的最小值的子数组是 [20,50], 它的最小值是 20    i = 2:     - 大小为 3 的子数组为 [10,20,50], [20,50,10]    - 有最大的最小值的子数组是 [10,20,50], 它的最小值是 10    i = 3:     - 大小为 4 的子数组为 [10,20,50,10]    - 有最大的最小值的子数组是 [10,20,50,10], 它的最小值是 10



**提示：**

  * `n == nums.length`
  * `1 <= n <= 105`
  * `0 <= nums[i] <= 109`


**Tags:** Stack, Array, Monotonic Stack

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/maximum-of-minimum-values-in-all-subarrays
