<?php

$cmd = "rm -r fh.html gx.html zhmy.html hxsj.html";
exec($cmd, $output, $status);
echo "Done!";
$newURL = "index.php";
header('Location: '.$newURL);
?>
