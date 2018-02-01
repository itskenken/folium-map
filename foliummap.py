import folium as flm
from geopy.geocoders import Nominatim

geo = Nominatim()
mtac = geo.geocode("Sheraton Music City Hotel")
awatext = 'This is where AWA is.'
mtactext = 'This is where MTAC is.'

momo = geo.geocode("Georgia World Congress Center")
momotext = 'This is where Momocon is.' 

generic = 'not much here'

fg = flm.FeatureGroup(name="pyMap")
map = flm.Map(location=[34.068660, -84.553299], zoom_start=6, tiles= "Mapbox Bright")
fg.add_child(flm.Marker(
    location=[33.883565, -84.466498], popup=generic, icon = flm.Icon(color='red')))
fg.add_child(flm.Marker(
    location=[mtac.latitude, mtac.longitude], popup=mtactext
))
fg.add_child(flm.Marker(
    location=[momo.latitude, momo.longitude], popup=momotext
))
map.add_child(fg)



map.save("Map1.html")
