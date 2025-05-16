const box = document.getElementById('box');
let topPos = 200;
let leftPos = 200;
const step = 200;  

document.addEventListener('keydown', function(event) {
  if (event.key === 'ArrowUp') {
    topPos -= step;
  } else if (event.key === 'ArrowDown') {
    topPos += step;
  } else if (event.key === 'ArrowLeft') {
    leftPos -= step;
  } else if (event.key === 'ArrowRight') {
    leftPos += step;
  }


  box.style.top = topPos + 'px';
  box.style.left = leftPos + 'px';
});
const img = DocumentTimeline.getElementById("img");
const next = document.getElementById("next");
const prev = document.getElementById("prev");
let i = 0;
const images = ["./download.png", "./download (1).png", "./download (2).png"];
next addEventListener("click", function(){
    i++;
    if (i >= images.length){
        i = 0;

    }
    img.src = images[i];
})
prev addEventListener("click", function(){
    i++;
    if (i >= images.length){
        i = 0;

    }
    img.src = images[i];
})