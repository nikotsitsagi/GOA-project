function computer(processor,videocard,ram){
    this.processor = "i7 12th gen"
    this.videocard = "gtx 1080ti"
    this.ram = "2x8gb DDR4"


}
this.displayInfo = function() {
    console.log(`Processor: ${this.processor}`);
    console.log(`videocard: ${this.videocard}`);
    console.log(`RAM: ${this.ram}`);

}
function keyboard(key1,key2,key3,key4){
    this.key1 = "W"
    this.key2 = "A"
    this.key3 = "S"
    this.key4 = "D"
}
this.displayinfo = function(){
    console.log(`key1:${this.key1}`)
    console.log(`key2:${this.key2}`)
    console.log(`key3:${this.key3}`)
    console.log(`key4:${this.key4}`)

}

let array1 = [1, 2, 3, 4, 5];
let array2 = ['a', 'b', 'c', 'd'];
let array3 = [true, false, true, false];

console.log("array1:");
for (let item of array1) {
    console.log(item);
}

console.log("array2:");
for (let item of array2) {
    console.log(item);
}

console.log("array3:");
for (let item of array3) {
    console.log(item);
}

