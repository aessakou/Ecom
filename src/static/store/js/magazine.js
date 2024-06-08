

addEventListener('DOMContentLoaded', (e)=>{
	const listImgs = document.querySelectorAll('.product-list img');
	listImgs.forEach((item, index)=>{
		item.addEventListener('mouseover', (ev)=>{
		});
	});

	const addProduct = document.getElementById('add-product-id');
	
	addProduct.addEventListener('click', function(){
		console.log('ADD PRODUCT');
	});
});