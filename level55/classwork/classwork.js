//1)
const fruits = ["apple", "banana", "watermelon"];
for (const fruit in fruits); {
    console.log(fruits);
}
//2)
const person = {
    name: "niko",
    age: 16,
    proffesion: "programmer"

};
for (const key in person) {
    console.log(`${key}: ${person[key]}`);
}
const name = "niko";
const age = 16;

const greeting = `hello my name is ${name} and i am ${age} years old.`;
console.log(greeting);

const numbers = [1, 2, 3, 4];

numbers.forEach(function(number) {
  console.log(number);
});

// 6) 
const user = {
  name: "Ana",
  greet() {
    console.log("Hi, I’m Ana!");
  }
};
user.greet();

// 7) 
const age = 22;
const city = "tbilisi";
const student = {
  name: "giorgi",
  age,  
  city  
};
console.log(student);

// 8) 
const skill = "javascript";
const devSkills = {
  [`level_of_${skill}`]: "begginer"
};
console.log(devSkills);