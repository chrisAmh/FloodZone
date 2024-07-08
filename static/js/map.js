function toggleSidebar() {
    const sidebar = document.getElementById("sidebar");
    const toggleButton = document.getElementById("toggleButton");
    sidebar.classList.toggle("open");
    toggleButton.classList.toggle("sidebar-open");
    toggleButton.style.display = sidebar.classList.contains("open") ? "none" : "block";
}

function dropdown() {
    document.getElementById("submenu").classList.toggle("hidden");
    document.getElementById("arrow").classList.toggle("rotate-180");
}

// Search functionality using Nominatim
document.getElementById('searchButton').addEventListener('click', function() {
const query = document.getElementById('searchInput').value;
if (query) {
fetch(`https://nominatim.openstreetmap.org/search?format=json&q=${query}`)
    .then(response => response.json())
    .then(data => {
        if (data.length > 0) {
            const result = data[0];
            const latlng = [result.lat, result.lon];
            map.setView(latlng, 13);
        } else {
            alert('Location not found.');
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
    
}
});