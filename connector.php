<?php 
ini_set('display_errors', 'On');
$rawText = '"' . $_GET['source'] . '"';
$more_options = '';
if ($_GET['listType'] == 'ol')
	$more_options .= 'o';
if ($_GET['dataAttr'] == 'no')
	$more_options .= 'r';
$result = shell_exec("python indentTree.py -s$more_options $rawText");
echo '<hr>';
echo '<h2>HTML List Display on the Web</h2>';
echo $result;

echo '<hr>';
echo '<h2>Formatted HTML Source Code</h2>';
echo '<pre>';
echo htmlentities($result);
echo '</pre>';

echo '<hr>';
echo '<h2>Compressed Production Source Code</h2>';
echo htmlentities($result);
echo '<hr>';
?>