<!DOCTYPE html>
<?php
include("connect_db.php");

?>

<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
    <form action="character_insert02.php" method="post">
        <p>角色名稱：<input type="text" name="CharacterName"></p>
        <p>武器%數：<input type="text" name="WeaponPercent"></p>
        <p>武器綠字：<input type="text" name="WeaponGreenNumber"></p>
        <input type="submit" value="確定">
    </form>
</body>

</html>