<?php
$ck1_name = "a_course";
$ck1_value = "Network";
$ck2_name = "a_Subject";
$ck2_value = "Comp. Sc";
$ck3_name = "a_Instructor";
$ck3_value = "Prof. Ram Rustagi";

$domain = "workshops.myweb.local";
$secure = true;
$httponly = true;

$path1 = "/";
$path2 = "/workshops";
$path3 = "/workshops/programs";

setcookie($ck1_name, $ck1_value, time() + (60), $path1); 
setcookie($ck2_name, $ck2_value, time() + (600), $path2);
setcookie($ck3_name, $ck3_value, time() + (86400), $path3);

?>
<html>
<body>

<?php
if(count($_COOKIE) > 0) {
    echo "Cookies are <br>";
    print_r($_COOKIE);
} else {
    echo "No cookies are set";
}

?>

</body>
</html>
