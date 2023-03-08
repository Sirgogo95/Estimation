let options = document.querySelector(".options");
let menu_options = document.querySelector(".menu_options");
let logo_name = document.querySelector(".logo_name");
let menu_button = document.querySelector(".menu_button");
let sidebar = document.querySelector(".sidebar");
let wrapper = document.querySelector(".wrapper");


function inactivate(){
    if (localStorage.getItem("active") == "si") {
        localStorage.setItem("active", "no");
    } else {
        localStorage.setItem("active", "si")
    }
    options.classList.toggle("inactive-options");
    menu_options.classList.toggle("inactive-menu_options");
    logo_name.classList.toggle("inactive-logo_name");
    sidebar.classList.toggle("inactive-sidebar");
    wrapper.classList.toggle("inactive-wrapper");  
}

document.addEventListener('DOMContentLoaded', function() {
    if (localStorage.getItem("active") == "no"){
        inactivate()
        localStorage.setItem("active", "no")
    }

})




function myFunction() {
    // Declare variables
    var input, filter, table, tr, td, i, txtValue;
    input = document.getElementById("form-control me-2");
    filter = input.value.toUpperCase();
    table = document.getElementById("table table-hover");
    tr = table.getElementsByTagName("tr");
  
    // Loop through all table rows, and hide those who don't match the search query
    for (i = 0; i < tr.length; i++) {
      td = tr[i].getElementsByTagName("td")[0];
      if (td) {
        txtValue = td.textContent || td.innerText;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
          tr[i].style.display = "";
        } else {
          tr[i].style.display = "none";
        }
      }
    }
  }


