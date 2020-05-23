

setInterval(update_sensor, 1000);

function update_sensor() {
    $.ajax({
        url: "/sensors",
        method: "GET",
	success: function(data) {
	    document.getElementById("sensor_value").innerHTML = data;
	}
    })
};
