

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
	const productForm = document.getElementById('createpro-form-id');

	if (isDigital && productForm) {
		isDigital.addEventListener('change', function(e){
			e.preventDefault();
			if (productForm.digital.value == 'false') {
				if (productForm.children[1].children[1].children[1]) {
					productForm.children[1].children[1].children[1].innerHTML = '<input id="shprice-id" type="number" name="shprice" placeholder="Shipping price" required class="form-control">';
				}
				if (productForm.children[1].children[2]) {
					productForm.children[1].children[2].innerHTML = '<input id="shcities-id" type="text" name="shcities" placeholder="Shipping cities" required class="form-control">';
				}
			}
			else {
				if (productForm.children[1].children[1].children[1]) {
					productForm.children[1].children[1].children[1].innerHTML = '';
				}
				if (productForm.children[1].children[2]) {
					productForm.children[1].children[2].innerHTML = '';
				}
			}
		});
	}


	const uploadImgs = document.querySelector('.cp-slider .imgtoupload');
	var imgcount = 1;
	if (uploadImgs && productForm) {
		uploadImgs.addEventListener('click', function(e){
			
			var newinput = document.createElement('input');
			var productimg = document.createElement('img');
			var divelem = document.createElement('div');

			divelem.appendChild(newinput);
			divelem.appendChild(productimg);

			newinput.type = 'file';
			newinput.name = 'image' + imgcount;
			newinput.accept = 'image/*';
			newinput.id = 'pimgs-id' + imgcount;
			newinput.classList.add('d-none');
			newinput.click();
			newinput.addEventListener('change', uploadfile);
			productimg.classList.add('product-imgs');
			
			function uploadfile(event) {
				event.preventDefault();
				let file = event.target.files[0];
				if (file) {
					let reader = new FileReader();
					reader.onload = function (e) {
						productimg.src = e.target.result;
						if (productimg != ''){
							productForm.children[0].children[1].children[0].appendChild(divelem);
							imgcount++;
						}
					}
					reader.readAsDataURL(file);
				}
			}

		});

		
	}
});