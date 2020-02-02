<!DOCTYPE html>

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
    <?php
    if (isset($_POST["n"])) {
    }
    echo "<form method=\"POST\" action=\"\">";
    echo "請輸入正整數：<input type=\"text\" name=\"n\" />";
    echo "<input type=\"submit\" value=\"確定\" />";
    echo "</form>";

    function Fibonacci($n)
    {
        $fibon = array();
        $fibon[0] = 0;
        $fibon[1] = 1;
        for ($i = 0; $i < $n; $i++) {
            $fibon[$i + 2] = $fibon[$i + 1] + $fibon[$i];
        }
        return $fibon[$n];
    }

    if (isset($_POST["n"])) {
        $FibonacciNumber = Fibonacci($_POST["n"]);
        echo "第" . $_POST["n"] . "項費氏數列的值為" . $FibonacciNumber;
    }




    ?>
</body>

</html>