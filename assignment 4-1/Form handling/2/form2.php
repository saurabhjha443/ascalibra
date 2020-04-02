<html>
    <body>
    <?php
             if(isset($_POST['submit'])) 
            {
                $uname=$_POST['uname'];
            
                if( !empty($uname)  )
                {   
                    if(isset($_POST["mytext"]) && is_array($_POST["mytext"])){
                        echo "Username is ".$uname."<br> >";

                        $colors = implode("<br> >", $_POST["mytext"]);
                        echo $colors;
                       
                        
                        
                    }           
                }
            }
        ?>        
    </body>

</html>