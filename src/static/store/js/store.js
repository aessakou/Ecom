

const logout_id = document.getElementById('logout-id');

if (logout_id) {

	logout_id.addEventListener('click', function() {
		const overlay = document.createElement('div');
	
		console.log('div')
		overlay.classList.add('logoutwin')
		const modal = document.createElement('div');
		modal.classList.add('modal');
		modal.innerHTML = '<h2>Modal Title</h2><p>This is a modal window.</p><button id="closeModalBtn">Close</button>';
		modal.innerHTML = `<h1>logout</h1>
							<p>Are you sure you want to log out?</p>
							<a href="`+ logouthref +`">Yes!</a>
							`;
	
		overlay.appendChild(modal);
		
	
	
	
		document.body.appendChild(overlay);
	});
}


const SearchBar = document.getElementById('search-bar-input');
const SearchBtn = document.getElementById('search-bar-btn');



if (SearchBar) {
	SearchBar.addEventListener('submit', function(e){
		e.preventDefault();
		handleSearchBar();
	});
	if (SearchBtn) {
		SearchBtn.addEventListener('click', function(){
			handleSearchBar();
		});
	}
}



function handleSearchBar(){
	const contentTosearch = SearchBar.search.value;
	console.log('Search bar content:', contentTosearch);
	if (contentTosearch == '') {
		location.reload();
	}

	if (window.location.pathname != '/') {
		alert("Please go to the home page");
		return;
	}

	const csrftoken = getCookie('csrftoken');

	console.log('token=',csrftoken);

	let url = '/search_handle/';

	fetch(url, {
		method:'POST',
		headers: {
			'Content-Type': 'application/json',
			'Content-Type': 'text/html',
			'X-CSRFToken': csrftoken,
		},
		body:JSON.stringify({'content':contentTosearch})
	})
	.then((response)=> response.json())
	.then((data)=>{
		console.log("Rendering the page...");
		document.getElementById('search_results').innerHTML = data.rendered_html;
		reloadJS();
	})

	console.log('FINISH');
}



function reloadJS(){
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
			// document.getElementById('cartitems-num').innerHTML = ;
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
	
}