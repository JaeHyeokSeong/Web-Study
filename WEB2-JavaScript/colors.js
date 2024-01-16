let Body = {
	setColor: function(target, color) {
		target.style.color = color;
	},

	setBackgroundColor(target, color) {
		target.style.backgroundColor = color;
	}
};

let ATags = {
	setColor: function(color) {
		let all_a_tags = document.querySelectorAll('a');
		for(let i = 0; i < all_a_tags.length; i++) {
			all_a_tags[i].style.color = color;
		}
	}
};

function nightDayHandler(self) {
	let target = document.querySelector('body');
	if(self.value === 'night') {
		Body.setBackgroundColor(target, 'black');	
		Body.setColor(target, 'white');
		ATags.setColor('white');
		self.value = 'day';
	} else {
		Body.setBackgroundColor(target, 'white');
		Body.setColor(target, 'black');
		ATags.setColor('blue');
		self.value = 'night';
	}
}
