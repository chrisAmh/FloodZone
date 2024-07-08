mapboxgl.accessToken = 'pk.eyJ1IjoiY2hyaXNhbWgiLCJhIjoiY2x5MDliODQ3MGpjdzJ2cXZkdXRydWFkcyJ9.Tp78epbV_IfdcQKKSsPV6g'; // Replace with your Mapbox access token
var map = new mapboxgl.Map({
    container: 'map', // container id
    style: 'mapbox://styles/mapbox/streets-v11', // stylesheet location
    center: [-74.5, 40], // starting position [lng, lat]
    zoom: 9 // starting zoom
});

// Add zoom and rotation controls to the map.
map.addControl(new mapboxgl.NavigationControl());

function toggleSidebar() {
    var sidebar = document.querySelector('.sidebar');
    sidebar.classList.toggle('open');

    var toggleButton = document.querySelector('.toggle-button');
    if (sidebar.classList.contains('open')) {
        toggleButton.classList.add('sidebar-open');
    } else {
        toggleButton.classList.remove('sidebar-open');
    }
}
