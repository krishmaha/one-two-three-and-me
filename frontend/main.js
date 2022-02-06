const el = (id) => document.getElementById(id);
let canvas = el("canvas");
let context = canvas.getContext("2d");

el("check").onclick = async function () {
  const imageData = context.getImageData(0, 0, canvas.width, canvas.height);

  const getGrayScaleValue = (x, y) => {
    const red = y * (canvas.width * 4) + x * 4;
    const redCoord = imageData.data[red]
    const blueCoord = imageData.data[red + 1]
    const greenCoord = imageData.data[red + 2]
    return (redCoord + blueCoord + greenCoord) / 3;
  }
  
  let grayScaleImage = []
  for (let i = 0; i < canvas.height; i++) {
    for (let j = 0; j < canvas.width; j++) {
      grayScaleImage.push(getGrayScaleValue(j, i))
    }
  }

  console.log(JSON.stringify(grayScaleImage))

  const response = await fetch("http://127.0.0.1:8000/model/predict/", {
    method: 'POST',
    headers: {
      'Origin': 'http://127.0.0.1:8887/'
    },
    body: JSON.stringify({'image' : grayScaleImage})
  })

  const data = await response.json();
  
  console.log(data.predicted);
  console.log(data.score);

};

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
