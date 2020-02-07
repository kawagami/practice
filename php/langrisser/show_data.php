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
    // $SqlCommnd = "SELECT * FROM `character_green_number`";
    // $SqlCommnd = "SELECT * FROM `character_list` as a JOIN `character_green_number` as b on a.`character_id`=b.`cha_id`";
    $SqlCommnd = "SELECT * FROM `character_list` LEFT JOIN `character_green_number` USING(`character_id`)";
    $Result = $db_link->query($SqlCommnd);
    while ($ResultRow = $Result->fetch_assoc()) {
        foreach ($ResultRow as $Item => $Value) {
            echo $Item . "=>" . $Value . "<br>";
        }
        echo "<hr>";
    }


    ?>

</body>

</html>