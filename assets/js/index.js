require("../scss/mystyles.scss")
require("../scss/flights.scss")

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

L.Icon.Default.mergeOptions({
    iconRetinaUrl: marker2x,
    iconUrl: marker,
    shadowUrl: markerShadow,
})
//----------------------------------------------------------------------------
window.drawFlight = drawFlight
window.drawPicture = drawPicture


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
