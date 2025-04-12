
document.getElementById("changeTextBtn").onclick = function() {
    document.getElementById("text").textContent = "ტექსტი შეიცვალა!";
};


document.getElementById("increaseFontBtn").onclick = function() {
    let currentSize = window.getComputedStyle(document.getElementById("text")).fontSize;
    let newSize = parseFloat(currentSize) + 2;
    document.getElementById("text").style.fontSize = newSize + "px";
};


const myArray = [10, 20, 30, 40, 50];
console.log("First Element:", myArray[0]);
console.log("Last Element:", myArray[myArray.length - 1]);

document.getElementById("changePageBtn").onclick = function() {
    window.location.href = "newPage.html"; 
};

//-DOM არის HTML დოკუმენტის სტრუქტურა, ხოლო document არის ობიექტი, რომლითაც JavaScript-ი მართავს დოკუმენტს.