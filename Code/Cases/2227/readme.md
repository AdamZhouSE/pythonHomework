## 题目描述
<p>有一个需要密码才能打开的保险箱。密码是&nbsp;<code>n</code> 位数, 密码的每一位是&nbsp;<code>k</code>&nbsp;位序列&nbsp;<code>0, 1, ..., k-1</code>&nbsp;中的一个 。</p>

<p>你可以随意输入密码，保险箱会自动记住最后&nbsp;<code>n</code>&nbsp;位输入，如果匹配，则能够打开保险箱。</p>

<p>举个例子，假设密码是&nbsp;<code>"345"</code>，你可以输入&nbsp;<code>"012345"</code>&nbsp;来打开它，只是你输入了 6&nbsp;个字符.</p>

<p>请返回一个能打开保险箱的最短字符串。</p>

<p>&nbsp;</p>

<p><strong>示例1:</strong></p>

<pre><strong>输入:</strong> n = 1, k = 2
<strong>输出:</strong> "01"
<strong>说明:</strong> "10"也可以打开保险箱。
</pre>

<p>&nbsp;</p>

<p><strong>示例2:</strong></p>

<pre><strong>输入:</strong> n = 2, k = 2
<strong>输出:</strong> "00110"
<strong>说明: </strong>"01100", "10011", "11001" 也能打开保险箱。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li><code>n</code> 的范围是&nbsp;<code>[1, 4]</code>。</li>
	<li><code>k</code> 的范围是&nbsp;<code>[1, 10]</code>。</li>
	<li><code>k^n</code> 最大可能为&nbsp;<code>4096</code>。</li>
</ol>

<p>&nbsp;</p>