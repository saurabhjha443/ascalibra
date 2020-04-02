<html>
    <body>
    <?php
             if(isset($_POST['Calculate'])) 
            {
                $first1=$_POST['first'];
                
                $second1=$_POST['second'];
            
                if( !empty($first1) && !empty($second1)   )
                {
                    $operation=$_POST['oper'];
                   
                    switch($operation)
                    {
                        case "plus":$value= $first1+$second1;
                                    echo $first1 ."+".$second1."=".$value;
                                    break;
                        case "minus":$value= $first1-$second1;
                                    echo $first1 ."-".$second1."=".$value;
                                    break;          
                        case "mul":$value= $first1*$second1;
                                    echo $first1 ."x".$second1."=".$value;
                                    break;
                        case "divide": $value=$first1/$second1;
                                    echo $first1 ."/".$second1."=".$value;
                                    break;
                    }                
                }
            }
        ?>        
    </body>

</html>