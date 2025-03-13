const form = document.getElementById("form");

form.addEventListener('submit', function(e){
    e.preventDefault();

    const radValue = form.rad.elements.value;
    console.log(radValue);
})