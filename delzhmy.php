<?php

$cmd = "rm -r zhmy.html";
exec($cmd, $output, $status);
echo "Done!";
$newURL = "index.php";
header('Location: '.$newURL);
?>
