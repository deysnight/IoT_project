

setInterval(update_sensor, 1000);

function update_sensor() {
    $.ajax({
        url: "/sensors",
        method: "GET",
	contentType: "application/json",
	success: function(data) {
	    var ret = JSON.parse(data)
	    document.getElementById("sensor_value").innerHTML = ret.ana + " V";
	    document.getElementById("sensor_state").innerHTML = ret.dig;
		document.getElementById("sensor_percent").innerHTML = ret.per + " %";
	}
    })
};
