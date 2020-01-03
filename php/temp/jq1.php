<html>

<head>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
    <script type="text/javascript">
        $(document).ready(function() {
            $(".btn1").click(function() {
                $("p").wrap("<div></div>");
            });
        });
    </script>
    <style type="text/css">
        div {
            background-color: yellow;
        }
    </style>
</head>

<body>
    <p>This is a paragraph.</p>
    <p>This is another paragraph.</p>
    <button class="btn1">用 div 包裹每個段落</button>
</body>

</html>