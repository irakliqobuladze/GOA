const form = document.getElementById("form");

form.addEventListener('submit', function(e){
    e.preventDefault();

    const check1 = form.elements.check.checked;
    console.log(check1);
})