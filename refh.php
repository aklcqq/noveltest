<?php

$cmd1 = "python3 fh.py";
//$cmd2 = "python3 gx.py";
//$cmd3 = "python3 zhmy.py";
//$cmd4 = "python3 hxsj.py";

exec($cmd1, $output, $status);
//exec($cmd2, $output, $status);
//exec($cmd3, $output, $status);
//exec($cmd4, $output, $status);

$newURL = "fh.php";
header('Location: '.$newURL);

?>
