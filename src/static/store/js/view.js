

addEventListener('DOMContentLoaded', function() {
	console.log('This is view js...');


	const baseImg = this.document.getElementById('baseimage-Win');
	const imgContainer = this.document.querySelector('.img-window');
	const silder = this.document.querySelector('.silder-imgs .silder');
	const silderimgs = this.document.querySelectorAll('.silder-imgs .silder img');
	const silderPrev = this.document.querySelector('.silder-imgs .silder-prev');
	const silderNext = this.document.querySelector('.silder-imgs .silder-next');
	let zoomedIn = false;
	var CurrentImgIndex = 0;
	var OldImgIndex = 0;
	var itemsliding = 3;
	var itemWidth = ((silder.scrollWidth) / (silderimgs.length));
	var slideDistance = itemWidth;
	// zoomedIn = 'none';
	
	
	baseImg.addEventListener('mousemove', (e)=>{
		e.preventDefault();
		const rect = imgContainer.getBoundingClientRect();
		const x = e.clientX - rect.left; // x position within the element
		const y = e.clientY - rect.top;  // y position within the element
	
		const xPercent = x / rect.width * 100;
		const yPercent = y / rect.height * 100;
		
		baseImg.style.transformOrigin = `${xPercent}% ${yPercent}%`;
		baseImg.style.transform = 'scale(2)'; // adjust the scale as needed
	});
	baseImg.addEventListener('mouseleave', (ev)=> {
		ev.preventDefault();
	
		baseImg.style.transform = 'scale(1)';
		baseImg.style.transformOrigin = 'center center';
	});
	
	silderimgs.forEach((item, index)=>{
		item.addEventListener('mouseover', function(){
			baseImg.src = item.src;
			silderimgs[OldImgIndex].style.border = 'none';
			item.style.border = '2px solid black';
			OldImgIndex = index;
		});
	});

	silderNext.addEventListener('click', function(){
		if (CurrentImgIndex < (silderimgs.length - 5) - itemsliding) {
			CurrentImgIndex += itemsliding;
			updateSliderPosition();
		}
		else if (CurrentImgIndex < silderimgs.length - 5) {
			CurrentImgIndex = silderimgs.length - 5;
			updateSliderPosition();
		}
	});
	
	silderPrev.addEventListener('click', function(){
		if (CurrentImgIndex > itemsliding - 1) {
			CurrentImgIndex -= itemsliding;
			updateSliderPosition();
		}
		else if (CurrentImgIndex > 0) {
			CurrentImgIndex = 0;
			updateSliderPosition();
		}
	});

	function updateSliderPosition() {
        silder.style.transform = `translateX(-${CurrentImgIndex * slideDistance}px)`;
		if (CurrentImgIndex <= 0){
			silderPrev.classList.add('silder-disable');
		}
		else {
			silderPrev.classList.remove('silder-disable');
		}
		if (CurrentImgIndex >= silderimgs.length - 5) {
			silderNext.classList.add('silder-disable');
		}
		else {
			silderNext.classList.remove('silder-disable');
		}
    }
	if (silderimgs.length <= 5){
		silderNext.classList.add('silder-disable');
	}
});