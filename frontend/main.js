const el = (id) => document.getElementById(id);
let canvas = el("canvas");
let context = canvas.getContext("2d");

el("check").onclick = function () {};

el("shuffle").onclick = function () {
  let newNumber = Math.floor(Math.random() * 10);
  el("number").textContent = newNumber;
};

el("clear").onclick = function () {
  context.clearRect(0, 0, canvas.width, canvas.height);
};

el("settings").onclick = function () {};

const modal = document.querySelector(".modal");
const trigger = document.querySelector(".trigger");
const closeButton = document.querySelector(".close-button");

function toggleModal() {
  modal.classList.toggle("show-modal");
}

function windowOnClick(event) {
  if (event.target === modal) {
    toggleModal();
  }
}

trigger.addEventListener("click", toggleModal);
closeButton.addEventListener("click", toggleModal);
window.addEventListener("click", windowOnClick);
