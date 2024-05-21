function image_height(){
	console.log('hello');
	const productImgs = document.querySelectorAll('.summary-img');
	productImgs.forEach(item=>{
			let width = item.offsetWidth;
			let height = (9 * width) / 16;
			item.style.height = height + 'px';
			item.style.width = width + 'px';
			console.log(height);
		});

}


// image_height();

// window.addEventListener('resize', image_height);