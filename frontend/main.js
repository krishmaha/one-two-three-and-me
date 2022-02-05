const el = (id) => document.getElementById(id);

var canvas = el("canvas");

var context = canvas.getContext("2d");

var start = function (coors) {
  context.beginPath();
  context.moveTo(coors.x, coors.y);
  this.isDrawing = true;
};

var move = function (coors) {
  if (this.isDrawing) {
    context.strokeStyle = "#fff";
    context.lineJoin = "round";
    context.lineWidth = 3;
    context.lineTo(coors.x, coors.y);
    context.stroke();
  }
};

var stop = function (coors) {
  if (this.isDrawing) {
    this.touchmove(coors);
    this.isDrawing = false;
  }
};

var drawer = {
  isDrawing: false,
  mousedown: start,
  mousemove: move,
  mouseup: stop,
  touchstart: start,
  touchmove: move,
  touchend: stop,
};

var draw = function (e) {
  var coors = {
    x: e.clientX || e.targetTouches[0].pageX,
    y: e.clientY || e.targetTouches[0].pageY,
  };
  drawer[e.type](coors);
};

canvas.addEventListener("mousedown", draw, false);
canvas.addEventListener("mousemove", draw, false);
canvas.addEventListener("mouseup", draw, false);
canvas.addEventListener("touchstart", draw, false);
canvas.addEventListener("touchmove", draw, false);
canvas.addEventListener("touchend", draw, false);

var go = function (e) {
  this.parentNode.removeChild(this);
  draw(e);
};

el("go").addEventListener("mousedown", go, false);
el("go").addEventListener("touchstart", go, false);

// prevent elastic scrolling
document.body.addEventListener(
  "touchmove",
  function (e) {
    e.preventDefault();
  },
  false
);
