const btn1 = document.getElementById('btn1');
const btn2 = document.getElementById('btn2');

btn1.addEventListener('click', function (e) {
  e.preventDefault();
  if (btn2.className.includes('visible')) {
    btn2.classList.remove('visible');
  } else {
    btn2.classList.add('visible');
  }
});

// hides the side button
const showBtn2 = () => {
  btn2.classList.add('visible');
};

// shows the side button
const hideBtn2 = () => {
  btn2.classList.remove('visible');
};

// get position of button 1
// https://developer.mozilla.org/en-US/docs/Web/API/Element/getBoundingClientRect
const getButton1Position = () => {
  return btn1.getBoundingClientRect();
};

window.addEventListener('scroll', function (e) {
  const btn1Position = getButton1Position();
  // console.log(btn1Position.bottom);
  if (btn1Position.bottom < 0) {
    showBtn2();
  } else {
    hideBtn2();
  }
});
