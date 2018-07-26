dragula([document.getElementById('team')]);
var angle = 0;
function galleryspin(sign) {
let spinner = document.querySelector("#spinner");
/* To change the number of slides {angle = angle + (360 / number of slides)} */
if (!sign) { angle = angle + 72; } else { angle = angle - 72; }
spinner.setAttribute(`style`,`-webkit-transform: rotateY(${angle}deg); -moz-transform: rotateY(${angle}deg); transform: rotateY(${angle}deg);`);
}

