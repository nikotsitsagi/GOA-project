class Car {
    constructor(name, model, year) {
      this.name = name;
      this.model = model;
      this.year = year;
    }
  }
  let car1 = new Car('Toyota', 'Corolla', 2020);
  let car2 = new Car('Honda', 'Civic', 2022);
  let car3 = new Car('Ford', 'Mustang', 2021);
  
  console.log(car1);
  console.log(car2);
  console.log(car3);
  

class Car {
    constructor(name, model, year, hp) {
      this.name = make;
      this.model = model;
      this.year = year;
      this.hp = hp;
    }

    increasehp() {
      this.horsePower += 50;  
    }
  }
  
  
  let car11 = new Car('Toyota', 'Corolla', 2020, 150);
  let car22 = new Car('Honda', 'Civic', 2022, 180);
  let car33 = new Car('Ford', 'Mustang', 2021, 450);
  
  
  car11.increaseHorsePower();
  car22.increaseHorsePower();
  car33.increaseHorsePower();
  
  console.log(car11);
  console.log(car22);
  console.log(car33);
  
//3
  let arr1 = [1, 2, 3, 4, 5];

//4
  let arr2 = new Array(1, 2, 3, 4, 5);

//5
  for (let i = 0; i < arr1.length; i++) {
    console.log(arr1[i]);
  }
  

  for (let i = 0; i < arr2.length; i++) {
    console.log(arr2[i]);
  }
  

//6
console.log(arr1[2]); //index
console.log(arr1.slice(1, 4));//slice
//7
//associative array არის array სადაც ელემენტებს აქვთ გასაღები-დაფასების წყვილები. არ უნდა გამოვიყენოთ რადგან JavaScript-ში array-ებიw იყენებენ რიცხვით ინდექსებს, და საკვანძო-დაფასების გამოყენება შეიძლება გამოიწვიოს გაუგებარმა ქცევამ. 
