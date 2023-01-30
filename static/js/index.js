const nav = document.querySelector("nav");
const slider = document.querySelector(".slider");
const place = document.querySelector(".place");
const nav__head = document.querySelector(".nav__head");
const lines = document.querySelector(".lines");
const line1 = document.querySelector(".line1");
const line2 = document.querySelector(".line2");
const menuitems = document.querySelectorAll(".menu-item");

// change slider on particular url
if (window.location.href.indexOf("blogs.html") > -1) {
  nav.classList.add("nav-blogs");
  slider.classList.add("slider-blogs");
} else {
  nav.classList.remove("nav-blogs");
  slider.classList.remove("slider-blogs");
}
lines.addEventListener("click", (e) => {
  if (window.location.href.indexOf("blogs.html") > -1) {
    slider.classList.toggle("slider-blogs-focus");
  } else {
    slider.classList.toggle("slider-focus");
  }
  nav__head.classList.toggle("nav__head-focus");
  place.classList.toggle("place-focus");
  line1.classList.toggle("line1-focus");
  line2.classList.toggle("line2-focus");
  menuitems.forEach((menuitem) => {
    menuitem.classList.toggle("menu-item-focus");
  });
  console.log("hey");
});
