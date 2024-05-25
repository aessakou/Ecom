function getCookie(name) {
	let cookieValue = null;
	if (document.cookie && document.cookie !== '') {
		const cookies = document.cookie.split(';');
		for (let i = 0; i < cookies.length; i++) {
			const cookie = cookies[i].trim();
			if (cookie.substring(0, name.length + 1) === (name + '=')) {
				cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
				break;
			}
		}
	}
	return cookieValue;
}


var updateBtns = document.getElementsByClassName('update-cart');


for (let i = 0; i < updateBtns.length; i++)
{
	updateBtns[i].addEventListener('click', function(){
		let productID = this.dataset.product;
		let action = this.dataset.action;

		
		if (user === 'AnonymousUser')
		{
			console.log('USER is not logged in.');
			
		} else {
			UpDateUserOrder(productID, action);
		}

	});
}


function UpDateUserOrder(productID, action) {
	console.log("ProductID = ", productID, "action = ", action);
	const csrftoken = getCookie('csrftoken');


	let url = '/update_item/';

	fetch(url, {
		method:'POST',
		headers: {
			'Content-Type': 'application/json',
			'X-CSRFToken': csrftoken,
		},
		body:JSON.stringify({'productID':productID, 'action': action})
	})
	.then((response)=>{
		return response.json();
	})
	.then((data)=>{
		console.log('date:', data);
		location.reload()
	})

}