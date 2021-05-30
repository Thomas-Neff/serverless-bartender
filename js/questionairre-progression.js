function questionairre1() {
  var T = document.getElementById("Question2");
  T.style.display = "block";
  var c = document.getElementById("Question1");
  c.style.display = "none";
}

function questionairre2() {
  var T = document.getElementById("Question3");
  T.style.display = "block";
  var c = document.getElementById("Question2");
  c.style.display = "none";
}

function results() {
  window.location.href = "/results.html";
}
