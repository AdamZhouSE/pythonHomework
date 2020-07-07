## 题目描述
<p>给出集合&nbsp;<code>[1,2,3,…,<em>n</em>]</code>，其所有元素共有&nbsp;<em>n</em>! 种排列。</p>

<p>按大小顺序列出所有排列情况，并一一标记，当&nbsp;<em>n </em>= 3 时, 所有排列如下：</p>

<ol>
	<li><code>"123"</code></li>
	<li><code>"132"</code></li>
	<li><code>"213"</code></li>
	<li><code>"231"</code></li>
	<li><code>"312"</code></li>
	<li><code>"321"</code></li>
</ol>

<p>给定&nbsp;<em>n</em> 和&nbsp;<em>k</em>，返回第&nbsp;<em>k</em>&nbsp;个排列。</p>

<p><strong>说明：</strong></p>

<ul>
	<li>给定<em> n</em>&nbsp;的范围是 [1, 9]。</li>
	<li>给定 <em>k&nbsp;</em>的范围是[1, &nbsp;<em>n</em>!]。</li>
</ul>

<p><strong>示例&nbsp;1:</strong></p>

<pre><strong>输入:</strong> n = 3, k = 3
<strong>输出:</strong> "213"
</pre>

<p><strong>示例&nbsp;2:</strong></p>

<pre><strong>输入:</strong> n = 4, k = 9
<strong>输出:</strong> "2314"
</pre>