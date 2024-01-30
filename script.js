$(document).ready(function () {
  // إنشاء الخريطة
  var map = L.map('map').setView([0, 0], 2);
  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '© OpenStreetMap contributors'
  }).addTo(map);

  // دالة لجلب بيانات JSON وتحديث الخريطة
  function updateMap() {
    $.getJSON('location.json', function (data) {
      // حذف العلامات الحالية عند تحديث الخريطة
      map.eachLayer(function (layer) {
        if (layer instanceof L.Marker) {
          map.removeLayer(layer);
        }
      });

      // إضافة العلامات الجديدة من بيانات JSON
      data.forEach(function (item) {
        var marker = L.marker([item.latitude, item.longitude])
          .addTo(map)
          .bindPopup('IP: ' + item.ip);
      });
    });
  }

  // تحديث الخريطة كل 3 ثواني
  setInterval(updateMap, 3000);

  // تحديث الخريطة لأول مرة عند بدء التشغيل
  updateMap();
});
