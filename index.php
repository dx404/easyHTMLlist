<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="author" content="Duo Zhao">
<link rel="stylesheet" type="text/css" href="style.css">
<base target="_blank">
</head>

<body>
	<!-- A Two-Column Table -->
<script src="https://wwwx.cs.unc.edu/~duozhao/frameworks/jquery-1.8.2"></script>
<script src="https://wwwx.cs.unc.edu/~duozhao/app/html-list/tag.js"></script>

	<div id="input-field">
		<h2>Nested List By Indentation</h2>
		<p>It is cumbersome to write nested list in HTML. while the plain text
			in indentation format is easy to read. So I coded a small parser that
			converts arbitrary nested level list to html tag format</p>
		<pre>
			<textarea id="source" name="source" rows="15" cols="80">
1 Please Paste or Type your nested list
	1.1 Hello, World!
	1.2 Standard I/O
		1.2.1 Standard Input
			1.2.1.1 ASCII Characters
			1.2.1.2 Unicode
		1.2.2 Standard Output
		1.2.3 Standard Error
2 Try Some Tree Structures 
	2.1 Binary Search Tree
		2.1.1 Red-Black Tree
		2.1.2 AVL Tree
		2.1.3 B-Tree
3 All about non-deterministic </textarea>
		</pre>
	</div>
	<table>
		<tr>
			<td>
				<button id="convert" type="button">Click to Convert</button>
			</td>
			<td><label><input type="radio" id="radio-ul" name="list-type"
					value="ul " checked>unordered list</label>
			</td>
			<td><label style="display: inline"><input type="radio" id="radio-ol"
					name="list-type" value="ol"> ordered list </label>
			</td>
			<td><label><input type="checkbox" id="data-attr" name="data-attr"
					checked> attach attributes </label>
			</td>
		</tr>
	</table>
	<div id="target" name="target"></div>

</body>