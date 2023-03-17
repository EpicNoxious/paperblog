const nav = document.querySelector("nav");
const footer = document.querySelector("footer");
const slider = document.querySelector(".slider");
const place = document.querySelector(".place");
const nav__head = document.querySelector(".nav__head");
const lines = document.querySelector(".lines");
const line1 = document.querySelector(".line1");
const line2 = document.querySelector(".line2");
const menuitems = document.querySelectorAll(".menu-item");

//
// blog.html page
//
if (window.location.href.match(new RegExp("blogs/[0-9a-z-]*/$"))) {
  nav.style.cssText = "display: none;";
  document.documentElement.style.cssText = "padding: 0";
}

//
// blogs.html page
//
else if (window.location.href.match(new RegExp("blogs/$"))) {
  footer.style.cssText = "display: none;";
}
//
// signupin.html
//
else if (window.location.href.match(new RegExp("members/"))) {
  nav.style.cssText = "display: none;";
}
//
// add.html
//
else if (window.location.href.match(new RegExp("add/$"))) {
  nav.style.cssText = "display: none;";
}
//
// update.html
//
else if (window.location.href.match(new RegExp("update/[0-9a-z-]*/$"))) {
  nav.style.cssText = "display: none;";
}
//
// delete.html
//
else if (window.location.href.match(new RegExp("delete/[0-9a-z-]*/$"))) {
  nav.style.cssText = "display: none;";
}
//
// nav slider working
//
lines.addEventListener("click", (e) => {
  // if (window.location.href.match(new RegExp("blogs/$"))) {
  //   slider.classList.toggle("slider-focus");
  // } else {
  //   slider.classList.toggle("slider-blogs-focus");
  // }
  slider.classList.toggle("slider-focus");
  nav__head.classList.toggle("nav__head-focus");
  place.classList.toggle("place-focus");
  line1.classList.toggle("line1-focus");
  line2.classList.toggle("line2-focus");
  menuitems.forEach((menuitem) => {
    menuitem.classList.toggle("menu-item-focus");
  });
});

//
// login plane
//
let object = document.querySelector("#object");
let objectWidth = object.offsetWidth;
let windowWidth = window.innerWidth - objectWidth;
let documentHeight = document.documentElement.offsetHeight - window.innerHeight;
let contain = document.querySelector(".login-container");

//
// function to detect collision of plane with contain
//
doElsCollide = function (object, contain) {
  object.offsetBottom = object.offsetTop + object.offsetHeight; // length of object
  object.offsetRight = object.offsetLeft + object.offsetWidth; // breadth of object
  contain.offsetBottom = contain.offsetTop + contain.offsetHeight; // length of contain
  contain.offsetRight = contain.offsetLeft + contain.offsetWidth; // breadth of contaienr

  return (
    object.offsetRight > contain.offsetLeft &&
    object.offsetRight < contain.offsetRight
  );
};

window.addEventListener("scroll", function () {
  let scrollPosition = document.documentElement.scrollTop;
  let objectPositionLeft = windowWidth * (scrollPosition / documentHeight);
  object.style.cssText = `left: ${objectPositionLeft}px`;
  if (doElsCollide(object, contain)) {
    object.classList.add("change");
  } else {
    object.classList.remove("change");
  }
});
