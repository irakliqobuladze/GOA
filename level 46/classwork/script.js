let but = document.getElementById("button");
let but1 = document.getElementById("button1");
let but2 = document.getElementById("button1");

but.addEventListener('click',function(event){
    event.preventDefault()

    but.textContent = "hello"

    but.style.backgroundColor = "yellow"
})

but1.addEventListener('click',function(event){
    event.preventDefault()

    but.textContent = "hello world"

    but.style.backgroundColor = "blue"
})

but2.addEventListener('click',function(event){
    event.preventDefault()

    but.textContent = "gamarjoba"

    but.style.backgroundColor = "red"
})