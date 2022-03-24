$(document).ready(function () {
    const map = L.map('map').setView([53.9, 27.56], 6);
    L.tileLayer('https://api.maptiler.com/maps/streets/{z}/{x}/{y}.png?key=HoVAsZnamBouzxZdVK1I', {
        attribution: 'Map data &copy; <a href="https://www.maptiler.com/copyright/" target="_blank">&copy; MapTiler</a> ' +
            '<a href="https://www.openstreetmap.org/copyright" target="_blank">&copy; OpenStreetMap contributors</a>',
    }).addTo(map);

    function tags_adder(data) {
        const coordinates = JSON.parse(data)
        let list = '<ol>\n'
        for (let i in coordinates) {
            let lat = coordinates[i].fields.latitude
            let lng = coordinates[i].fields.longitude
            list = list + `<li> ${lat}°, ${lng}°</li>`
        }

        $('#coordinates').html(list + '</ol>');
    }

    map.on("click", function (e) {
        new L.Marker([e.latlng.lat, e.latlng.lng]).addTo(map);
        let array = [e.latlng.lat, e.latlng.lng]
        let coordinates = JSON.stringify(array)
        console.log(array)
        $.post(
            '/create_location',
            {
                'coordinates': coordinates
            });
        $.get('/coordinates_view', tags_adder);

    });
});



