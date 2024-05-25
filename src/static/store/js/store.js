// function image_height(){
// 	console.log('hello');
// 	const productImgs = document.querySelectorAll('.summary-img');
// 	productImgs.forEach(item=>{
// 			let width = item.offsetWidth;
// 			let height = (9 * width) / 16;
// 			item.style.height = height + 'px';
// 			item.style.width = width + 'px';
// 			if (width < item.parentElement.offsetWidth - 5)
// 			{
// 				item.style.height = item.parentElement.offsetHeight + 'px';
// 				item.style.width = item.parentElement.offsetWidth + 'px';
// 			}

// 		});

// }


// image_height();

// window.addEventListener('resize', image_height);


// const orderitemQuantity = document.querySelectorAll('.orderitem-quantity');
// const arrowUpQuantity = document.querySelectorAll('.arrow-up-quantity');
// const arrowDownQuantity = document.querySelectorAll('.arrow-down-quantity');

// var ids_num = 1;
// orderitemQuantity.forEach(item=>{
// 	item.id = 'orderitem-quantity' + ids_num;
// 	ids_num++;
// });

// ids_num = 1;
// arrowUpQuantity.forEach(item=>{
// 	item.id = ids_num + 'arrow-up-quantity';
// 	ids_num++;
// 	item.addEventListener('click', (e)=>{
// 		let idnum = item.id ;
// 		let quantityid = 'orderitem-quantity' + idnum[0];
// 		let quantityElem = document.getElementById(quantityid);
// 		let quantity = quantityElem.textContent;
// 		quantity++;
// 		quantityElem.innerText = quantity;
// 	})
// });

// ids_num = 1;
// arrowDownQuantity.forEach(item=>{
// 	item.id = ids_num + 'arrow-down-quantity';
// 	ids_num++;
// 	item.addEventListener('click', (e)=>{
// 		let idnum = item.id ;
// 		let quantityid = 'orderitem-quantity' + idnum[0];
// 		let quantityElem = document.getElementById(quantityid);
// 		let quantity = quantityElem.textContent;
// 		quantity--;
// 		if (quantity < 1)
// 			quantity = 1;
// 		quantityElem.innerText = quantity;
// 	})
// });
	