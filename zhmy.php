<?php
echo <<<_END
<!DOCTYPE html>
<html lang='en'>
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    
    <title>Welcome!</title>
    <style>
.vertical-menu {
  width: 100%; /* Set a width if you like */
}

.vertical-menu a {
  background-color: #eee; /* Grey background color */
  color: black; /* Black text color */
  display: block; /* Make the links appear below each other */
  padding: 12px; /* Add some padding */
  text-decoration: none; /* Remove underline from links */
}

.vertical-menu a:hover {
  background-color: #ccc; /* Dark grey background on mouse-over */
}

.vertical-menu a.active {
  background-color: #f0d3d3; /* Add a pink color to the "active/current" link */
  color: white;
}
    </style>
    </head>
    <body>


<div class="vertical-menu">
  <a href="index.php">Novel page</a>
  <a href='zhmy.html' class='active'>召唤梦魇</a>
<a href='rezhmy.php'>Refresh</a>
<a href='delzhmy.php'>Remove</a>
</div></body></html>
_END;


//echo "<a href='gx.html'>归向</a>";
//echo "<a href='zhmy.html'>召唤梦魇</a>";
//echo "<a href='hxsj.html'>幻想世界大穿越</a>";


?>

