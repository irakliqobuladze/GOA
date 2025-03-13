const submit = document.getElementById("submit");
const form = document.getElementById("form");

submit.addEventListener('click', function(event){
    event.preventDefault();

    const name = form.elementSibling.name;
    const email = form.elements.email;
    const password = form.elements.password;

    console.log(name.value);
    console.log(email.value);
    console.log(password.value);
})