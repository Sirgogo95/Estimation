function myFunction() {
    // Declare variables
    var sel = document.querySelector(".precio_select").value
    var input, filter, table, tr, td, i, txtValue;
    input = document.getElementById("search_box");
    filter = input.value.toUpperCase();
    table = document.getElementById("table table-hover");
    tr = table.getElementsByTagName("tr");
  
    // Loop through all table rows, and hide those who don't match the search query
    for (i = 0; i < tr.length; i++) {
      td = tr[i].getElementsByTagName("td")[sel];
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
