const el = (id) => document.getElementById(id);
var canvas = el("canvas");
var context = canvas.getContext("2d");

el("check").onclick = function () {};

el("shuffle").onclick = function () {};

el("clear").onclick = function () {
  context.clearRect(0, 0, canvas.width, canvas.height);
};

el("settings").onclick = function () {};
