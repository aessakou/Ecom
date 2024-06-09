

addEventListener('DOMContentLoaded', (e)=>{
	const listImgs = document.querySelectorAll('.product-list img');
	if (listImgs) {
		listImgs.forEach((item, index)=>{
			item.addEventListener('mouseover', (ev)=>{
			});
		});
	}

	const addProduct = document.getElementById('add-product-id');
	
	if (addProduct) {
		addProduct.addEventListener('click', function(){
			console.log('ADD PRODUCT');
		});
	}

	const uploadBaseImg = document.querySelector('.create-product-box .baseimg');

	if (uploadBaseImg) {
		const baseImg = document.querySelector('.create-product-box .baseimg img');
		const fileInput = document.getElementById('base-img-id');
		uploadBaseImg.addEventListener('click', function(){
			console.log('Uplaod base image');
			fileInput.click();
		});

		fileInput.addEventListener('change', function (event) {
			const file = event.target.files[0];
			if (file) {
				const reader = new FileReader();
				reader.onload = function (e) {
					baseImg.src = e.target.result;
					const styleElement = document.createElement('style');
					styleElement.textContent = `
						.create-product-box .baseimg:hover a::before {
							content: "Change the image";
							min-width: 125px;
							left: -127px;
						}
					`;
					document.head.appendChild(styleElement);
				}
				reader.readAsDataURL(file);
			}
		});
	}

	const isDigital = document.getElementById('is_digital');

	if (isDigital) {
		isDigital.addEventListener('change', function(e){
			e.preventDefault();
			const productForm = document.getElementById('createpro-form-id');
			if (productForm.digital.value == 'false') {
				productForm.shprice.classList.remove('d-none');
				productForm.shcities.classList.remove('d-none');
			}
			else {
				productForm.shprice.classList.add('d-none');
				productForm.shcities.classList.add('d-none');
			}
		});
	}
});