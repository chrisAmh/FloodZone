document.addEventListener('DOMContentLoaded', (event) => {
  const LEAFLET_CONFIG = {
      DEFAULT_CENTER: [5.6037, -0.1870],
      DEFAULT_ZOOM: 13,
      TILES: [
          ['OpenStreetMap', 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
              attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
          }],
          ['Terrain Map', 'http://services.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', {
              attribution: 'Tiles &copy; Esri &mdash; Source: Esri, i-cubed, USDA, USGS, AEX, GeoEye, Getmapping, Aerogrid, IGN, IGP, UPR-EGP, and the GIS User Community'
          }],
          ['Data Map', 'https://cartodb-basemaps-{s}.global.ssl.fastly.net/dark_all/{z}/{x}/{y}.png', {
            attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a> &copy; <a href="http://cartodb.com/attributions">CartoDB</a>'
          }],
        ['Another Layer', 'https://{s}.another-layer.org/{z}/{x}/{y}.png', {
          attribution: '&copy; <a href="https://www.another-layer.org/copyright">Another Layer</a>'
      }],
            ]
  };

  // Create map with Leaflet using DEFAULT_CENTER and DEFAULT_ZOOM from config
  const map = L.map('mapid', {
      zoomControl: false
  }).setView(LEAFLET_CONFIG.DEFAULT_CENTER, LEAFLET_CONFIG.DEFAULT_ZOOM); 

  // Base Layers from LEAFLET_CONFIG.TILES
  const baseLayers = {};
  LEAFLET_CONFIG.TILES.forEach(([name, url, options]) => {
      baseLayers[name] = L.tileLayer(url, options);
  });

  // Start with the first layer as the default basemap
  const defaultLayer = Object.values(baseLayers)[0]; 
  defaultLayer.addTo(map);

  // Add Layer Control to switch between base layers
  L.control.layers(baseLayers).addTo(map);

  // Add Zoom Control
  L.control.zoom({ position: 'topright' }).addTo(map);

  main_map_init(map); 
});


var dataset = new L.GeoJSON.AJAX("{% url 'tweet_view' %}", {
  pointToLayer: function(feature, latlng) {
      return L.circleMarker(latlng, {
          fillColor: 'teal',
          color: '#537898',
          weight: 1,
          fillOpacity: 0.5
      });
  }
}).on({
  mouseover: function(e) {
      this.setStyle({ color: 'yellow' });
  },
  mouseout: function(e) {
      this.setStyle({ color: '#537898' });
  }
});

dataset.addTo(map); // Add the data to the map object


    function openSidebar() {
      document.getElementById("sidebar").classList.toggle("hidden");
    }

    function dropdown() {
      document.getElementById("submenu").classList.toggle("hidden");
      document.getElementById("arrow").classList.toggle("rotate-180");
    }

     // Call your function to initialize the GeoJSON layer


