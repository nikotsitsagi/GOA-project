function sayHello() {
    console.log("Hello World");
  }
  
  sayHello();



function sumThreeNumbers(a, b, c) {
    let sum = a + b + c;
    console.log(sum);
  }
  
  sumThreeNumbers(3, 5, 7);

function greet(name = "friend", age = 20) {
    console.log(name + " age: " + age);
  }
  
  greet(); 
  greet("george", 30);
  
    