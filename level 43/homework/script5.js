const form = document.getElementById("form");

form.addEventListener('submit', function(e){
    e.preventDefault();

    const dropDownMenu = form.elements.dropDown.value;
    console.log(dropDownMenu);
})