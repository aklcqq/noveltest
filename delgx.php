<?php

$cmd = "rm -r gx.html";
exec($cmd, $output, $status);
echo "Done!";
$newURL = "index.php";
header('Location: '.$newURL);
?>
