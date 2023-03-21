document.getElementById("redirect1").addEventListener("mouseover", mouseOver1);
document.getElementById("redirect1").addEventListener("mouseout", mouseOut1);
document.getElementById("redirect2").addEventListener("mouseover", mouseOver2);
document.getElementById("redirect2").addEventListener("mouseout", mouseOut2);
function mouseOver1() {
  about ="The document similarity checker helps to find the similarity of two documents";
  document.getElementById("about1").innerHTML = about;
}
function mouseOut1() {
  document.getElementById("about1").innerHTML = "";
}
function mouseOver2() {
  about ="The best document finder finds the most similar document to a given document";
  document.getElementById("about2").innerHTML = about;
}
function mouseOut2() {
  document.getElementById("about2").innerHTML = "";
}
