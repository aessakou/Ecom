

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