<!DOCTYPE html>
<html>
    <head>
        <title>array2</title>
        <h1>City Array</h1>
    </head>
    <body>
    <?php
        $color = array("Tokyo", "Mexico City", "New York City", "Mumbai", "Seoul", "Shanghai", "Lagos",
        "Buenos Aires", "Cairo", "London");
        foreach ($color as $c)
        {
            echo "$c, ";
        }
            
            sort($color);
            echo "<ul>";
        foreach ($color as $y)
        {
            echo "<li>$y</li>";
        }
            echo "</ul>";
        
            array_push($color,"Los Angeles","Calcutta","Osaka","Beijing");
            
            sort($color);
            echo "<ul>";
        foreach ($color as $u)
        {
            echo "<li>$u</li>";
        }
            echo "</ul>";
    ?>
    </body>
</html>
 