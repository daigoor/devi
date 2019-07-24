var robot_controls = {
	state : "black",
	init: function () {
		//Key released 
		$(document).keyup(function(e){
			if(robot_controls.state != "black") {
				robot_controls.state = "black";
				robot_controls.setArrowColor(e.which, robot_controls.state, false);
			}
		});
		
		//Key pressed
		$(document).keydown(function(e){
			if(robot_controls.state != "red") {
				robot_controls.state = "red";
				robot_controls.setArrowColor(e.which, robot_controls.state, true);
			}
		});
		
		$(".div_box span").hover(
		  function() {
			if(this.className == "center_box") { 
				return; 
			}
			$( this ).attr("style", "color: red;");
			$( this ).addClass( "hover" );
		  }, function() {
			$( this ).removeClass( "hover" );
			$( this ).attr("style", "color: black;");
		  }
		);
		
		$(".div_box span").click(function() {
			robot_controls.clickedArrow(this.className, true);
		});
			
	}, 
	setArrowColor: function (arrowKey, color, movement) {
		switch (arrowKey) {
			case 37:
				//left arrow key
				$(".ro_left_arrow").css("color", color);
				robot_controls.clickedArrow("ro_left_arrow", movement);
				break;
			case 38:    //up arrow key
				$(".ro_up_arrow").css("color", color);
				robot_controls.clickedArrow("ro_up_arrow", movement);
				break;
			case 39:    //right arrow key
				$(".ro_right_arrow").css("color", color);
				robot_controls.clickedArrow("ro_right_arrow", movement);
				break;
			case 40:    //bottom arrow key
				$(".ro_down_arrow").css("color", color);
				robot_controls.clickedArrow("ro_down_arrow", movement);
				break;
			default:
				//console.log("There was an error in the key code: " + arrowKey + ", color: " + color);
				break;
		}
	},
	clickedArrow: function (elementName, movement) {
		robot_controls.emitEvent(elementName.replace("hover", ""), movement);
	},
	emitEvent: function (param, movement) {
		$.ajax({
			url: "robot?direction=" + param.split("_")[1] + "&movement=" + movement,
			type: "GET",
			data: "key=" + param,
			success: function(data){
				console.log("AJAX success:");
                    //TODO: remove this return!!
                    return;
				var result = JSON.parse(data);
				if(result.stderr.length > 0) {
					console.log("PANIC -> ROBOT movement error:");
					console.log(result.stderr);
					console.log("=============== Sending STOP action !!!");
					robot_controls.emitEvent("none", false);
				} else {
					console.log(data);
				}
			},
			error: function(info){
				console.log("AJAX error:");
				console.log(info);
			}
		});
	}
}

// A $( document ).ready() block.
$( document ).ready(function() {
    robot_controls.init();
});
