

addEventListener('DOMContentLoaded', function() {
	console.log('This is view js...');


	const baseImg = this.document.getElementById('baseimage-Win');
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
	zoomedIn = 'none';
	
	
	baseImg.addEventListener('mouseover', (e)=>{
		e.preventDefault();
		if (zoomedIn == false) {
			baseImg.style.width = (baseImg.offsetWidth * 2) + 'px';
			baseImg.style.height = (baseImg.offsetHeight * 2) + 'px';
			zoomedIn = true;
		}
	});
	baseImg.addEventListener('mouseout', (ev)=> {
		ev.preventDefault();
		if (zoomedIn == true) {
			baseImg.style.width = (baseImg.offsetWidth / 2) + 'px';
			baseImg.style.height = (baseImg.offsetHeight / 2) + 'px';
			zoomedIn = false;
		}
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