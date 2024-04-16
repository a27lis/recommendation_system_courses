let content = document.getElementById("courses-block")
let show = document.getElementById("show-btn")
let form = document.getElementById("formControlSelect")

show.addEventListener("click", () => {
    content.style.display = "block"
})

form.addEventListener("click", () => {
    content.style.display = "none"
})