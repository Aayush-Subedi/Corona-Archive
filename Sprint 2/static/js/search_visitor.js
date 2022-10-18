function search(searchInput, searchDiv) {
  search(searchInput,searchDiv);
}

function search(searchInput, searchDiv) {
  // Declare variables
  var input, filter, table, tr, td, i, txtValue;
  input = document.getElementById(searchInput);
  filter = input.value.toLowerCase();
  searchDiv = document.getElementById(searchDiv);
  tr = searchDiv.getElementsByTagName("li");

  // Loop through all rows, and hide those who don't match the search query
  for (i = 0; i < tr.length; i++) {
    td = tr[i].getElementsByTagName("div")[1];
    if (td) {
      txtValue = td.textContent || td.innerText;
      if (txtValue.toLowerCase().indexOf(filter) > -1) {
        tr[i].style.display = "";
      } else {
        tr[i].style.display = "none";
      }
    }
  }
}