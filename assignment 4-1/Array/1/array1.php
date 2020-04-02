<!DOCTYPE html>
<html>
<body>

<?php
$delete_item = 'march';
// list of array
$months = array('jan', 'august', 'march', 'april', 'may','october');

var_dump($months);
echo "<br>";
echo "Delete march from array<br>";
if (($key = array_search($delete_item, $months)) != false) 
{
    unset($months[$key]);
}
 
// print Array
var_dump($months);
?>

</body>
</html>
