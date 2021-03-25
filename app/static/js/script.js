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
		if(response[3]) {
			const submit = response[0]
			displayMessageUser(submit);
			const mess = response[1]
			displayMessageRobo(mess);	
			const loc = response[2];
			displayMap(loc);
			const extract = response[3]
			displayWiki(extract);
	    }
	    else {
			const submit = response[0]
			displayMessageUser(submit);
			const mess = response[1]
			displayMessageRobo(mess);
	    }
    })
})

function displayMessageUser(submit) {
	const parent = document.querySelector("ul");
	const child = document.createElement("p");
	child.id = "messageUser";
	child.classList.add("messageUser");
	parent.appendChild(child);
	let messageUser = child;
	messageUser.innerHTML = submit
}

function displayMessageRobo(mess) {
	const parent = document.querySelector("ul");
	const child = document.createElement("p");
	child.id = "messageRobo";
	child.classList.add("messageRobo");
	parent.appendChild(child);
	let messageRobo = child;
	messageRobo.innerHTML = mess
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
