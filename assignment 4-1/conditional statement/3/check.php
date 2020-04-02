<html>
    <body>
    <?php
             if(isset($_POST['check'])) 
            {
                $number=$_POST['number'];
                
            
                if( !empty($number) )
                {
                    
                    $number=$_POST['number'];
                    
                    if($number > 0)
                    {
                        echo "Number is positive";
                    }
                    
                    elseif($number < 0)
                    {
                        echo "Number is negative";
                    }           
                }
                
                else
                {
                    echo "Its a zero";
                }   
            }
        ?>        
    </body>

</html>