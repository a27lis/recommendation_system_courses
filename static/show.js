let content = document.getElementById("courses-block")
let show = document.getElementById("show-btn")
let form = document.getElementById("formControlSelect")

show.addEventListener("click", () => {
    content.style.display = "block"
})

form.addEventListener("click", () => {
    content.style.display = "none"
})


var options = ["Cat", "Dog", "Banana", "Apple", "Car", "Boat"]; // Массив с возможными значениями

function filterOptions() {
  var input = document.getElementById("myInput");
  var filter = input.value.toUpperCase();
  var dropdown = document.getElementById("dropdown");
  dropdown.innerHTML = "";
  for (var i = 0; i < options.length; i++) {
    if (options[i].toUpperCase().indexOf(filter) > -1) {
      var option = document.createElement("div");
      option.textContent = options[i];
      option.onclick = function(e) {
        input.value = this.textContent;
        dropdown.innerHTML = "";
      };
      dropdown.appendChild(option);
    }
  }
}
