let options = document.querySelector(".options");
let menu_options = document.querySelector(".menu_options");
let logo_name = document.querySelector(".logo_name");
let menu_button = document.querySelector(".menu_button");
let sidebar = document.querySelector(".sidebar");
let wrapper = document.querySelector(".wrapper");


function inactivate(){
    options.classList.toggle("inactive-options");
    menu_options.classList.toggle("inactive-menu_options");
    logo_name.classList.toggle("inactive-logo_name");
    sidebar.classList.toggle("inactive-sidebar");
    wrapper.classList.toggle("inactive-wrapper");

}


var myModal = document.getElementById('myModal')
var myInput = document.getElementById('myInput')

