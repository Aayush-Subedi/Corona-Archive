// document.getElementById("test").innerHTML = "";

let radioVal = document.querySelector('input[name="userType"]:checked').value;
console.log("radioVal1:", radioVal);

// Unique forms for visitor and place owner usertypes
let emailInput = document.querySelector(".user-box.email");
let phoneInput = document.querySelector(".user-box.phone");
let addressInput = document.querySelector(".user-box.address");
let cityInput = document.querySelector(".user-box.city");
let passwordInput = document.querySelector(".user-box.password");

// Whenever user clicks on radio form, inputs only necessary to currently selected user type are
//  showed, rest are hidden
document.querySelector(".radio-container").addEventListener("click", () => {
  radioVal = document.querySelector('input[name="userType"]:checked').value;
  console.log("radioVal2:", radioVal);

  emailInput.classList.remove("hide");
  phoneInput.classList.remove("hide");
  addressInput.classList.remove("hide");
  cityInput.classList.remove("hide");
  passwordInput.classList.remove("hide");

  switch (radioVal) {
    case "visitor":
      break;

    case "place":
      cityInput.classList.add("hide");
      break;

    // case "agency":
    //   addressInput.classList.add("hide");
    //   cityInput.classList.add("hide");
    //   emailInput.classList.add("hide");
    //   break;

    // case "hospital":
    //   addressInput.classList.add("hide");
    //   cityInput.classList.add("hide");
    //   emailInput.classList.add("hide");
    //   passwordInput.classList.add("hide");
    //   break;
  }
});

// console.log(
//   "testing form.js radio: ",
//   document.querySelector('input[name="userType"]:checked').value
// );
