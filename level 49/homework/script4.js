const div = document.getElementById("container");

let p = document.createElement("p");
let textNode1 = document.createTextNode("Hello World");

p.appendChild(textNode1);
div.replaceChildChild(p);


let button = document.createElement("button");
let textNode2 = document.createTextNode("click me");

button.appendChild(textNode2);
div.replaceChild(button, p);

