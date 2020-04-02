<html>
    <head>
        <title>
            Count display
        </title>
        Count display from 5 to 15
    </head>
    <body>
        <?php
        $add=0;
        for ($i=5; $i <=15 ; $i++) { 
            echo "<br>The number is: $i";
            $add+=$i;
        }
        echo "<br><br>Addition is $add"
        ?>
    </body>
</html>