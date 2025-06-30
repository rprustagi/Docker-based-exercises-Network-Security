<?php
  $csp = "Content-Security-Policy: frame-ancestors attacker.cj.internal";;
  header("$csp");
  echo "<h1>".$csp."</h1>";
?>
