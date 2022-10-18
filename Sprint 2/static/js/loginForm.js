// document.getElementById("test").innerHTML = "";

let radioVal = document.querySelector('input[name="userType"]:checked').value;
console.log("loginForm.js");

// Unique forms for visitor and place owner usertypes
let emailInput = document.querySelector(".user-box.email");
let nameInput = document.querySelector(".user-box.name");

// Whenever user clicks on radio form, inputs only necessary to currently selected user type are
//  showed, rest are hidden
document.querySelector(".radio-container").addEventListener("click", () => {
  radioVal = document.querySelector('input[name="userType"]:checked').value;
  console.log("radioVal2:", radioVal);
  // console.log("hiding visitor");

  emailInput.classList.remove("hide");

  emailInput.querySelector("input").removeAttribute("required");
  nameInput.querySelector("input").removeAttribute("required");
  switch (radioVal) {
    case "visitor":
      document.querySelector('input[name="name"]').value = "";
      emailInput.querySelector("input").setAttribute("required", "");
      nameInput.classList.add("hide");
      break;

    case "place":
      document.querySelector('input[name="name"]').value = "";
      emailInput.querySelector("input").setAttribute("required", "");

      nameInput.classList.add("hide");
      break;

    case "agency":
      document.querySelector('input[name="email"]').value = "";
      nameInput.classList.remove("hide");
      emailInput.classList.add("hide");
      nameInput.querySelector("input").setAttribute("required", "");
      break;

    case "hospital":
      document.querySelector('input[name="name"]').value = "";
      nameInput.classList.remove("hide");
      emailInput.classList.add("hide");
      nameInput.querySelector("input").setAttribute("required", "");
      break;
  }
});

// console.log(
//   "testing form.js radio: ",
//   document.querySelector('input[name="userType"]:checked').value
// );
