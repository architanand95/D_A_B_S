<?php

    $database= new mysqli("localhost","root","PES2UG21CS108","edoc");
    if ($database->connect_error){
        die("Connection failed:  ".$database->connect_error);
    }

?>
