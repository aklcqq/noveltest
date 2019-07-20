<?php

$cmd = "rm -r hxsj.html";
exec($cmd, $output, $status);
echo "Done!";
$newURL = "index.php";
header('Location: '.$newURL);
?>
