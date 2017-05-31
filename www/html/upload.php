<?php
$a1=$_POST['1'];
$a2=$_POST['2'];
$a3=$_POST['3'];
if(isset($_POST['submit'])) {
// start uploading if user submit
  if(!empty($_FILES['file']['name'])) { 
   
       if ($_FILES["file"]["error"] > 0) {
       //check for errors
            echo "Error: " . $_FILES["file"]["error"] . "<br />";
            // if any errors encountered we are printing here
         }
        else {
        // if uploading process success , execute this area
         echo "Upload: " . $_FILES["file"]["name"] . "<br />";
         // print file name
         echo "Type: " . $_FILES["file"]["type"] . "<br />";
         // print type
         echo "Size: " . ($_FILES["file"]["size"] / 1024) . " Kb<br />";
         //print size
         move_uploaded_file($_FILES["file"]["tmp_name"],"/var/www/html/upload/" . $_FILES["file"]["name"]);
	$loc = '/var/www/html/upload/'. $_FILES["file"]["name"];
	echo $loc;
	echo $a1;
	echo $a2;
	$f=fopen("loc","w");
	fwrite($f,$loc);
	fwrite($f,"\n");
	fwrite($f,$a1);
	fwrite($f,"\n");
	fwrite($f,$a2);
	fwrite($f,"\n");
	fwrite($f,$a3);
	fclose($f);
	header("Location:/cgi-bin/uploadfinal.py");
	
         // Here we are moving uploaded file to upload folder with move_uploaded file function
	#echo exec(''ssh root@'+pi+' hadoop fs -put '+a0+' ' +a00');
               }
    } 

   else {
         echo 'plz select file'; //input filed empty return this error message
   }
	
	 
}


?>
