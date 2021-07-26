require("../scss/flight.scss")
import { drawFlight } from "./drawFlight.js"

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