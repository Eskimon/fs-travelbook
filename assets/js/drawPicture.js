export function drawPicture(coords, title, url, map) {
  let customOptions = {"minWidth": "800", "maxWidth": "1000", "className" : "lb-source"}
  let icon = L.icon({
    iconUrl: `${url}`,
    iconSize: [50, 50] },
  )
  let content = `<h1 class='title has-text-centered'>${title}</h1><img class='lb-source' src="${url}" width='800px'/>`
  let marker = L.marker(coords,{icon: icon}).bindPopup(content, customOptions).addTo(map)
  return {icon, marker}
}
