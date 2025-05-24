const slides = document.getElementById('slideContainer');
const slideImages = slides.children;
const slideCount = slideImages.length;
const slideWidth = 500;
let index = 0;

// Set container width based on number of images
slides.style.width = `${slideCount * slideWidth}px`;

function showSlide(i) {
  index = (i + slideCount) % slideCount;
  slides.style.transform = `translateX(-${index * slideWidth}px)`;
}

document.getElementById('nextBtn').onclick = () => showSlide(index + 1);
document.getElementById('prevBtn').onclick = () => showSlide(index - 1);

document.getElementById('myForm').addEventListener('submit', e => {
  e.preventDefault();
  alert('Form submitted!');
});
