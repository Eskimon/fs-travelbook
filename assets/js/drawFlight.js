export function drawFlight(departure, arrival, points, map, style, color) {
  //let poly = [[departure[0], departure[1]]];
  let _color = color || "#3388ff"
  let poly = []
  let lastLon = points[0][1]
  let wrap = false
  for(let i=0; i < points.length; i++) {
    if((lastLon < 0 && points[i][1] > 0 && Math.abs(points[i][1] > 150)) ||
        (lastLon > 0 && points[i][1] < 0 && Math.abs(points[i][1] < -150))) {
      wrap = true
    }
    let point = L.latLng(points[i][0], points[i][1])
    if(wrap) {
      point.lng += (point.lng < 0) ? 360 : -360
    }
    poly.push(point)
    lastLon = points[i][1]
  }
  // let lastpoint = L.latLng(arrival[0], arrival[1]);
  // if(wrap) {
    // lastpoint.lng += (lastpoint.lng < 0) ? 360 : -360
  // }
  // poly.push(lastpoint)
  let polyline = L.polyline(poly, {color: _color}).addTo(map)

  let startLoc = L.latLng(departure[0], departure[1])
  let stopLoc = L.latLng(arrival[0], arrival[1])
  if(wrap) {
    stopLoc.lng += (stopLoc.lng < 0) ? 360 : -360
  }
  let dep_mark = null
  let arr_mark = null
  if(style == 1) {
    dep_mark = L.marker(startLoc, {icon: window.take_off_icon, zIndexOffset: 500}).addTo(map)
    arr_mark = L.marker(stopLoc, {icon: window.landing_icon, zIndexOffset: 600}).addTo(map)
  } else if(style == 2) {
    let pointOption = {
      radius: 5,
      stroke: true,
      color: "#000000",
      weight: 1,
      fill: true,
      fillColor: _color,
      // opacity: 0,
      // fillOpacity: 0,
      zIndexOffset: 500,
    }
    dep_mark = L.circleMarker(startLoc, pointOption).addTo(map)
    arr_mark = L.circleMarker(stopLoc, pointOption).addTo(map)
  }

  return {polyline, dep_mark, arr_mark}
}
