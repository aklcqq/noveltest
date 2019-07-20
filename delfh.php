<?php

$cmd = "rm -r fh.html";
exec($cmd, $output, $status);
echo "Done!";
$newURL = "index.php";
header('Location: '.$newURL);
?>
