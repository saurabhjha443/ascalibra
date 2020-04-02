<html>
    <head>
    <title>Pattern</title>
    Pattern : <br>
    </head>
    <body>
        <?php
      for( $i=0; $i<=5; $i++ )
      {
         for( $j=1; $j<=$i; $j++)
         {
            echo '*';
         }
         echo '<br/>';
      }
        ?>
    </body>
</html>