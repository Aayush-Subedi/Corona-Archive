// After Page Load
document.addEventListener("DOMContentLoaded", function () {
  let entryTime = document.getElementById("entry-time");
  let exitTime = document.getElementById("exit-time");
  entryTime.value = "2022-04-19T17:21:00";
  exitTime.value = "2022-09-21T17:23:00";
});

function searchAll() {
  // Declare variables
  var tr, placeTD, visitorTD, i, placeTDValue, visitorTDValue;
  let visitorInput = document.getElementById("visitor-input");
  let placeInput = document.getElementById("place-input");
  let entryTime = document.getElementById("entry-time");
  let exitTime = document.getElementById("exit-time");

  let visitorValue = visitorInput.value.toLowerCase();
  let placeValue = placeInput.value.toLowerCase();
  let searchDiv = document.getElementById("data-table");
  let fromDate = new Date(entryTime.value);
  let toDate = new Date(exitTime.value);

  // Check if entry time is after exit time
  if (fromDate > toDate) {
    alert("Entry time must be before exit time");
    return;
  }

  tr = searchDiv.getElementsByTagName("li");

  const isDateOverlaped = (firstDateRange, secondDateRange) => {
    // f-from -----------f-to
    //          s-from -------------- s-to
    const overlappedEnd =
      firstDateRange.from <= secondDateRange.from &&
      firstDateRange.to >= secondDateRange.from &&
      firstDateRange.to <= secondDateRange.to;

    // f-from ----------------------- f-to
    //          s-from --------- s-to
    const overlappedBetween =
      firstDateRange.from <= secondDateRange.from &&
      firstDateRange.to >= secondDateRange.to;

    //            f-from -----------f-to
    // s-from -------------- s-to
    const overlappedStart =
      firstDateRange.from >= secondDateRange.from &&
      firstDateRange.from <= secondDateRange.to &&
      firstDateRange.to >= secondDateRange.to;

    return overlappedEnd || overlappedBetween || overlappedStart;
  };

  // Loop through all rows, and hide those who don't match the search query
  for (i = 0; i < tr.length; i++) {
    placeTD = tr[i].getElementsByTagName("div")[1];
    visitorTD = tr[i].getElementsByTagName("div")[0];
    entryDateTD = tr[i].getElementsByTagName("div")[2];
    exitDateTD = tr[i].getElementsByTagName("div")[3];
    if (placeTD && visitorTD) {
      placeTDValue = placeTD.textContent || placeTD.innerText;
      visitorTDValue = visitorTD.textContent || visitorTD.innerText;
      // console.log("Place at " + i + " " + placeTDValue);
      // console.log("Visitor at" + i + " " + visitorTDValue);

      // Check if entryDate and exitDate doesn't exist
      if (entryTime.value == "" && exitTime.value == "") {
        tr[i].style.display = "";
      }

      if (entryTime.value != "" && exitTime.value != "") {
        let entryDateTDValue = new Date(entryDateTD.innerHTML);
        let exitDateTDValue = new Date(exitDateTD.innerHTML);


        if (
          placeTDValue.toLowerCase().indexOf(placeValue) > -1 &&
          visitorTDValue.toLowerCase().indexOf(visitorValue) > -1 &&
          isDateOverlaped(
            {
              from: fromDate,
              to: toDate,
            },
            {
              from: entryDateTDValue,
              to: exitDateTDValue,
            }
          )

          // Check if entryDate and exitDate is between fromDate and toDate
          // ((entryDateTDValue >= fromDate && entryDateTDValue <= toDate) ||
          //   (fromDate >= entryDateTDValue && fromDate <= exitDateTDValue))

          // fromDate <= entryDateTDValue &&
          // toDate >= entryDateTDValue

          // entryDateTDValue >= fromDate &&
          // exitDateTDValue <= toDate
        ) {
          tr[i].style.display = "";
        } else {
          tr[i].style.display = "none";
        }
      } else if (entryTime.value != "" && exitTime.value == "") {
        let entryDateTDValue = new Date(entryDateTD.innerHTML);
        let exitDateTDValue = new Date(exitDateTD.innerHTML);
        if (
          placeTDValue.toLowerCase().indexOf(placeValue) > -1 &&
          visitorTDValue.toLowerCase().indexOf(visitorValue) > -1 &&
          isDateOverlaped(
            {
              from: fromDate,
              to: new Date(),
            },
            {
              from: entryDateTDValue,
              to: exitDateTDValue,
            }
          )
        ) {
          tr[i].style.display = "";
        } else {
          tr[i].style.display = "none";
        }
      } else if (entryTime.value == "" && exitTime.value != "") {
        let entryDateTDValue = new Date(entryDateTD.innerHTML);
        let exitDateTDValue = new Date(exitDateTD.innerHTML);
        if (
          placeTDValue.toLowerCase().indexOf(placeValue) > -1 &&
          visitorTDValue.toLowerCase().indexOf(visitorValue) > -1 &&
          isDateOverlaped(
            {
              from: new Date('2021-04-19T17:21:00'),
              to: toDate,
            },
            {
              from: entryDateTDValue,
              to: exitDateTDValue,
            }
          )

        ) {
          tr[i].style.display = "";
        } else {
          tr[i].style.display = "none";
        }
      }
    }
  }
}
