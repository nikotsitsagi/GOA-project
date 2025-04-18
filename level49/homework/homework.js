setInterval(function() {
    console.log("hello");
  }, 1000);

  setTimeout(function() {
    console.log("გამარჯობა ყოველი წამში!");
  }, 1000);

  const box = document.createElement("div");
  document.body.appendChild(box);

  const paragraph = document.createElement("p");
  const text = document.createTextNode("Hello, this is a paragraph!");
  paragraph.appendChild(text);
  box.appendChild(paragraph);

  const temp = document.createElement("div");
  temp.textContent = "I will be removed soon.";
  box.appendChild(temp);

  setTimeout(() => {
    box.removeChild(temp);
  }, 3000);

  setTimeout(() => {
    const newHeading = document.createElement("h1");
    newHeading.textContent = "I replaced the paragraph!";
    box.replaceChild(newHeading, paragraph);
  }, 5000);