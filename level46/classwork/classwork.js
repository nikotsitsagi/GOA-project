const button1 = document.getElementById('button1');
const button2 = document.getElementById('button2');
const button3 = document.getElementById('button3');

function changeButtonContent(event) {
    event.target.style.backgroundColor = 'lightblue';
    event.target.textContent = 'Clicked!';
}

button1.addEventListener('click', changeButtonContent);
button2.addEventListener('click', changeButtonContent);
button3.addEventListener('click', changeButtonContent);

function changeTextAndStyle(button) {
    const buttonId = button.id;
    button.innerHTML = "Clicked " + buttonId;
    button.style.fontSize = "20px";
}

let fruits = ["banana", "grape", "apple", "orange"];
fruits.unshift("hazelnut");
console.log(fruits);

let cars = ["toyota", "honda", "volkswagen", "bmw"];
cars[cars.length - 1] = "mercedes";
console.log(cars);

let anyList = [1, 2, 3, 4, 5];
anyList.shift();
anyList.pop();
console.log(anyList);
