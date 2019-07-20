<?php

$cmd = "rm -rf `ls *\.html`";
exec($cmd, $output, $status);
echo "Done!";
$newURL = "index.php";
header('Location: '.$newURL);
?>
