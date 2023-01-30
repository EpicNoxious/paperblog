const lines = document.querySelector(".lines");
const slider = document.querySelector(".slider");
const place = document.querySelector(".place");
const nav__head = document.querySelector(".nav__head");
const line1 = document.querySelector(".line1");
const line2 = document.querySelector(".line2");
const menuitems = document.querySelectorAll(".menu-item");
lines.addEventListener("click", (e) => {
  slider.classList.toggle("slider-focus");
  nav__head.classList.toggle("nav__head-focus");
  place.classList.toggle("place-focus");
  line1.classList.toggle("line1-focus");
  line2.classList.toggle("line2-focus");
  menuitems.forEach((menuitem) => {
    menuitem.classList.toggle("menu-item-focus");
  });
  console.log("hey");
});
