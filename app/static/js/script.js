let form = document.querySelector("#user-text-form");




function postFormData(url, data) {
	return fetch("/ajax", {
		method: "POST",
		body: data
	})
	.then(response => response.json())
	.catch(error => console.log(error));
}


form.addEventListener("submit", function (event) {
	event.preventDefault();
	console.log("message envoyer")

    postFormData("/ajax", new FormData(form))
    .then(response => {
    	console.log(response);
    })
})