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
    	const loc = response[0];
    	displayMap(loc);
    	const extract = response[1]
    	displayWiki(extract);
    })

})

function displayMap(loc) {
	const map = new google.maps.Map(document.getElementById("map"), {
		  zoom: 10,
		  center: loc
	});
	const image =
	    "https://developers.google.com/maps/documentation/javascript/examples/full/images/beachflag.png";
	const beachMarker = new google.maps.Marker({
	    position: loc,
	    map,
	    icon: "https://maps.gstatic.com/mapfiles/api-3/images/spotlight-poi.png"
	});
}

function displayWiki(extract) {
	let wiki = document.getElementById("wiki");
	wiki.innerHTML = extract
	document.getElementById("wiki").style.fontSize="14px"
}