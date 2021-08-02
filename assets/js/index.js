require("../scss/mystyles.scss")
require("../scss/flights.scss")

import pic_tipeee from "../img/tipeee.png"
import { drawFlight } from "./drawFlight.js"
import { drawPicture } from "./drawPicture.js"


import L from "leaflet"
import "leaflet/dist/leaflet.css"
//----------------------------------------------------------------------------
/* This code is needed to properly load the images in the Leaflet CSS */
// stupid hack so that leaflet's images work after going through webpack
import marker from "leaflet/dist/images/marker-icon.png"
import marker2x from "leaflet/dist/images/marker-icon-2x.png"
import markerShadow from "leaflet/dist/images/marker-shadow.png"

delete L.Icon.Default.prototype._getIconUrl

let take_off = encodeURI("data:image/svg+xml," + "<svg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'><path d='M2.5,19H21.5V21H2.5V19M22.07,9.64C21.86,8.84 21.03,8.36 20.23,8.58L14.92,10L8,3.57L6.09,4.08L10.23,11.25L5.26,12.58L3.29,11.04L1.84,11.43L3.66,14.59L4.43,15.92L6.03,15.5L11.34,14.07L15.69,12.91L21,11.5C21.81,11.26 22.28,10.44 22.07,9.64Z' fill='#000000'/></svg>").replace("#","%23")
let landing = encodeURI("data:image/svg+xml," + "<svg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'><path d='M2.5,19H21.5V21H2.5V19M9.68,13.27L14.03,14.43L19.34,15.85C20.14,16.06 20.96,15.59 21.18,14.79C21.39,14 20.92,13.17 20.12,12.95L14.81,11.53L12.05,2.5L10.12,2V10.28L5.15,8.95L4.22,6.63L2.77,6.24V11.41L4.37,11.84L9.68,13.27Z' fill='#000000' /></svg>").replace("#","%23")

L.Icon.Default.mergeOptions({
    iconRetinaUrl: marker2x,
    iconUrl: marker,
    shadowUrl: markerShadow,
})

window.take_off_icon = L.icon({iconUrl: take_off, iconSize: 30})
window.landing_icon = L.icon({iconUrl: landing, iconSize: 30})

//----------------------------------------------------------------------------
window.drawFlight = drawFlight
window.drawPicture = drawPicture


// Burger menu
document.addEventListener("DOMContentLoaded", () => {
  // Get all "navbar-burger" elements
  const $navbarBurgers = Array.prototype.slice.call(document.querySelectorAll(".navbar-burger"), 0)

  // Check if there are any navbar burgers
  if ($navbarBurgers.length > 0) {

    // Add a click event on each of them
    $navbarBurgers.forEach( el => {
      el.addEventListener("click", () => {

        // Get the target from the "data-target" attribute
        const target = el.dataset.target
        const $target = document.getElementById(target)

        // Toggle the "is-active" class on both the "navbar-burger" and the "navbar-menu"
        el.classList.toggle("is-active")
        $target.classList.toggle("is-active")

      })
    })
  }
})

// Notifications
document.addEventListener("DOMContentLoaded", () => {
  (document.querySelectorAll(".notification .delete") || []).forEach(($delete) => {
    const $notification = $delete.parentNode

    $delete.addEventListener("click", () => {
      $notification.parentNode.removeChild($notification)
    })
  })
})

// Lightbox
document.addEventListener("DOMContentLoaded", () => {
  let lbTarget = document.querySelector(".lb-wrapper")
  if(!lbTarget)
    return
  let lbTitle = lbTarget.querySelector(".lb-name")
  let lbDescription = lbTarget.querySelector(".lb-description")
  let lbImg = lbTarget.querySelector("img")
  lbTarget.addEventListener("click", () => {lbTarget.classList.remove("show")})
  let sources = document.querySelectorAll(".lb-source") || []
  sources.forEach(($elmt) => {
    $elmt.addEventListener("click", () => {
      lbImg.src = $elmt.src
      lbTitle.textContent = $elmt.dataset.name
      lbDescription.textContent = $elmt.dataset.description
      lbTarget.classList.add("show")
    })
  })
})

// Modals
document.addEventListener("DOMContentLoaded", () => {

  (document.querySelectorAll(".modal-opener") || []).forEach(($elmt) => {

    $elmt.addEventListener("click", ($event) => {
      let modal = document.getElementById($elmt.dataset.target)
      let html = document.querySelector("html")
      console.log(modal)
      modal.classList.add("is-active")
      html.classList.add("is-clipped")

      modal.querySelector(".modal-background").addEventListener("click", function(e) {
        e.preventDefault()
        modal.classList.remove("is-active")
        html.classList.remove("is-clipped")
      })

    })
  })
})
