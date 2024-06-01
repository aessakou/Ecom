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

if (user === 'AnonymousUser') {
	var cart = setCookieToBrowser();
}


var updateBtns = document.getElementsByClassName('update-cart');


for (let i = 0; i < updateBtns.length; i++)
{
	updateBtns[i].addEventListener('click', function(){
		let productID = this.dataset.product;
		let action = this.dataset.action;

		console.log('Update Cart...');
		
		if (user === 'AnonymousUser')
		{
			CookieItems(productID, action);
			
		} else {
			UpDateUserOrder(productID, action);
		}

	});
}

function CookieItems(productID, action)
{
	const csrftoken = getCookie('csrftoken');

	let url = '/update_item/';
	
	fetch(url, {
		method:'POST',
		headers: {
			'Content-Type': 'application/json',
			'X-CSRFToken': csrftoken,
		},
		body:JSON.stringify({'productID':productID, 'action': action, 'cart': cart})
	})
	.then((response)=>{
		return response.json();
	})
	.then((data)=>{
		cart = data;
		document.cookie = 'cart=' + JSON.stringify(cart) + ";domain=;path=/";
		location.reload()
	})
}


function UpDateUserOrder(productID, action) {
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
		location.reload()
	})

}


function setCookieToBrowser()
{
	let cart = JSON.parse(getCookie('cart'));
	if (cart == undefined)
	{
		cart = {}
		document.cookie = 'cart=' + JSON.stringify(cart) + ";domain=;path=/";
		location.reload();
	}
	return cart;
}
