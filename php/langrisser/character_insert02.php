<!DOCTYPE html>
<?php
include("connect_db.php");

?>

<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
    <?php
    if (isset($_POST["CharacterName"])) {
        echo "角色名字" . $_POST["CharacterName"] . "<br>";
        echo "武器%數" . $_POST["WeaponPercent"] . "<br>";
        echo "武器非%數值" . $_POST["WeaponGreenNumber"] . "<br>";
    }
    ?>

</body>

</html>