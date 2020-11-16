let form = document.querySelector("#user-text-form");

function postFormData(url, data) {
	return fetch("/robot", {
		method: "POST",
		body: data
	})
	.then(response => response.json())
	.catch(error => console.log(error));
}

form.addEventListener("submit", function (event) {
	event.preventDefault();
    postFormData("/view", new FormData(form))
    .then(response => {
    	const submit = response[0];
    	displayMessage(submit);
    	const loc = response[1];
    	console.log(loc)
    	displayMap(loc);
    	const extract = response[2]
    	displayWiki(extract);
    })
})

function displayMessage(submit) {
	const parent = document.querySelector("ul");
	const child = document.createElement("p");
	child.id = "message";
	child.classList.add("message");
	parent.appendChild(child);
	let message = child;
	message.innerHTML = submit
}

function displayWiki(extract) {
	const parent = document.querySelector("ul");
	const child = document.createElement("p");
	child.id = "wiki";
	child.classList.add("wiki");
	parent.appendChild(child);
	let wiki = child;
	wiki.innerHTML = extract
}

function displayMap(loc) {
	const parent = document.querySelector("ul");
	const child = document.createElement("div");
	child.id = "map";
	child.classList.add("map");
	parent.appendChild(child);
	const map = new google.maps.Map(child, {
		  zoom: 14,
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
