let form = document.querySelector("#user-text-form");

function postFormData(url, data) {
	return fetch("/map", {
		method: "POST",
		body: data
	})
	.then(response => response.json())
	.catch(error => console.log(error));
}


form.addEventListener("submit", function (event) {
	event.preventDefault();
	console.log("message envoyer")

    postFormData("/map", new FormData(form))
    .then(response => {
    	const lat = response[0]['geometry']["location"]["lat"];
    	const lng = response[0]['geometry']["location"]["lng"];
    	console.log(lat, lng)
    })
})


function initMap() {
	const map = new google.maps.Map(document.getElementById("map"), {
		  zoom: 8,
		  center: {
			  lat: 48.856614,
			  lng: 2.3522219
		    }
	});
	const image =
	    "https://developers.google.com/maps/documentation/javascript/examples/full/images/beachflag.png";
	const beachMarker = new google.maps.Marker({
	    position: {
		  lat: 48.856614,
		  lng: 2.3522219
	    },
	    map,
	    icon: "https://maps.gstatic.com/mapfiles/api-3/images/spotlight-poi.png"
	});
}
