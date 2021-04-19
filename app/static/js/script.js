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
	document.getElementById("waiting").style.display ='inline';
    postFormData("/view", new FormData(form))
    .then(response => {
		document.getElementById("waiting").style.display ='none';
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
	const user = document.createElement("p");
	user.id = "messageUser";
	user.classList.add("messageUser");
	parent.appendChild(user);
	let messageUser = user;
	messageUser.innerHTML = submit
}

function displayMessageRobo(mess) {
	const parent = document.querySelector("ul");
	const robo = document.createElement("p");
	robo.id = "messageRobo";
	robo.classList.add("messageRobo");
	parent.appendChild(robo);
	let messageRobo = robo;
	messageRobo.innerHTML = mess
}

function displayWiki(extract) {
	const parent = document.querySelector("ul");
	const wikextract = document.createElement("p");
	wikextract.id = "wiki";
	wikextract.classList.add("wiki");
	parent.appendChild(wikextract);
	let wiki = wikextract;
	wiki.innerHTML = extract
}

function displayMap(loc) {
	const parent = document.querySelector("ul");
	const maploc = document.createElement("div");
	maploc.id = "map";
	maploc.classList.add("map");
	parent.appendChild(maploc);
	const map = new google.maps.Map(maploc, {
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

