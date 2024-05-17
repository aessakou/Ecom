const allSidebar = document.querySelectorAll('#side-bar .first-menu ul li a');

allSidebar.forEach(item=> {
	const li = item.parentElement;

	item.addEventListener('click', function () {
		allSidebar.forEach(it=> {
			it.parentElement.classList.remove('active');
		})
		li.classList.add('active');
	})
});




const SwitchMode = document.getElementById('switch-mode');
const ModeMessage = document.getElementById('mode-message');
if (SwitchMode) {
	SwitchMode.addEventListener('change', function(){
		if (this.checked)
		{
			document.body.classList.add('darkmode');
			if (ModeMessage){
				ModeMessage.innerHTML = 'Dark';
			}
		}
		else
		{
			document.body.classList.remove('darkmode');
			if (ModeMessage){
				ModeMessage.innerHTML = 'Light';
			}
		}
	});
}