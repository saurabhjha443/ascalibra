<html>
    <head>

    </head>
    <body>
        <?php
           
            
            if(isset($_POST['submit'])) 
            {
                $city=$_POST['city'];
            
                if( !empty($city)  )
                {    $country=array("Tokyo"=>" Japan", "Mexico City"=> "Mexico", "New York City"=> "USA", "Mumbai"=>"India", "Seoul"=>"Korea","Shanghai"=>"China", "Lagos"=>"Nigeria",
                    "Buenos Aires"=> "Argentina", "Cairo"=> "Egypt", "London" => "England");
                    foreach($country as $x=>$xvalue)
                    {
                        if($x==$city)
                        {
                            echo $city." is in ".$xvalue ;
                        }
                    }
                                  
                }
            }
        ?>
    </body>
</html>