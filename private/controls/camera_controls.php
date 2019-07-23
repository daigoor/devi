
﻿<?php

require 'common.php';

/////////////////////////////////////////////////////////////////////
//				    	Camera Controls						   //
/////////////////////////////////////////////////////////////////////

//PARAMS
$directionCommand = $_GET["direction"];
$movementTrigger = $_GET["movement"];

//LOGIC
$res = new Response();
$res->movement = $movementTrigger;
$res->direction = $directionCommand;

$output = execute_process("commands/crc/rotateCam.sh " . $directionCommand);

// temp class till we return real results! 
class Response {
	var $direction;
	var $movement;
}

echo json_encode($output);


?>

