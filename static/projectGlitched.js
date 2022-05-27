const element = document.querySelector("#box");

element.addEventListener("mouseover", event => {
  console.log("Mouse in");
});

element.addEventListener("mouseout", event => {
  console.log("Mouse out");
});