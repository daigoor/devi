var camera_controls = {
	state : "black",
	init: function () {
		//Key released 
		$(document).keyup(function(e){
			if(camera_controls.state != "black") {
				camera_controls.state = "black";
				camera_controls.setArrowColor(e.which, camera_controls.state, false);
			}
		});
		
		//Key pressed
		$(document).keydown(function(e){
			if(camera_controls.state != "red") {
				camera_controls.state = "red";
				camera_controls.setArrowColor(e.which, camera_controls.state, true);
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
			camera_controls.clickedArrow(this.className, true);
		});
			
	}, 
	setArrowColor: function (arrowKey, color, movement) {
		switch (arrowKey) {
			case 65:
				//left arrow key
				$(".cam_left_arrow").css("color", color);
				camera_controls.clickedArrow("cam_left_arrow", movement);
				break;
			case 87:    //up arrow key
				$(".cam_up_arrow").css("color", color);
				camera_controls.clickedArrow("cam_up_arrow", movement);
				break;
			case 68:    //right arrow key
				$(".cam_right_arrow").css("color", color);
				camera_controls.clickedArrow("cam_right_arrow", movement);
				break;
			case 88:    //bottom arrow key
				$(".cam_down_arrow").css("color", color);
				camera_controls.clickedArrow("cam_down_arrow", movement);
				break;
			default:
				//console.log("There was an error in the key code: " + arrowKey + ", color: " + color);
				break;
		}
	},
	clickedArrow: function (elementName, movement) {
		camera_controls.emitEvent(elementName.replace("hover", ""), movement);
	},
	emitEvent: function (param, movement) {
		$.ajax({
			url: "camera?direction=" + param.split("_")[1] + "&movement=true",
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
					camera_controls.emitEvent("none", false);
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
    camera_controls.init();
});
