// Code adapted from: https://developers.google.com/maps/documentation/javascript/adding-a-google-map
// Code for Markers adapted from: https://developers.google.com/maps/documentation/javascript/custom-markers#maps_custom_markers-javascript
// Code for Legend adapted from: https://developers.google.com/maps/documentation/javascript/adding-a-legend#adding_the_legend_content


// Initialize and add the map
function initMap() {
  // The default location of Boston
  var default_location = { lat: 42.361145, lng: -71.057083 };
  // The map, centered at Boston
  map = new google.maps.Map(document.getElementById("map"), {
    zoom: 12,
    center: default_location,
  });
  var markers = {
    Race: {
      name: "Racial Injustice",
      icon: "/static/BLM.png", 
    },
    SexualOrientation: {
      name: "Sex-Based Discrimination",
      icon: "/static/rainbow.png", 
    },
    Assault: {
      name: "Sexual Assault",
      icon: "/static/sex.png",
    },
  };
  var pinpoint = [
    {
      position: new google.maps.LatLng(42.34696471308552, -71.06937363567481),
      type: "Race",
      message: "The Steppingston Foundation".link("https://www.tsf.org/")
    },
    {
      position: new google.maps.LatLng(40.667582601998646, -73.98151730683426),
      type: "Race",
      message: "The Loveland Foundation".link("https://thelovelandfoundation.org/")
    },
    {
      position: new google.maps.LatLng(42.314910, -71.061090),
      type: "Race",
      message: "Black Lives Matter Boston".link("https://blacklivesmatterboston.org/")
    },
    {
      position: new google.maps.LatLng(42.327089341537, -71.08289089146993),
      type: "Race",
      message: "Families For Justice as Healing".link("https://justiceashealing.org/")
    },
    {
      position: new google.maps.LatLng(42.358770763557956, -71.05933912028803),
      type: "SexualOrientation",
      message: "The Boston Alliance of Gay, Lesbian, Bisexual and Transgender Youth (BAGLY)".link("https://www.bagly.org/")
    },
    {
      position: new google.maps.LatLng(42.344210941937824, -71.09899680680019),
      type: "SexualOrientation",
      message: "Fenway Health".link("https://fenwayhealth.org/")
    },
    {
      position: new google.maps.LatLng(42.35892926723323, -71.05961923567533),
      type: "SexualOrientation",
      message: "GLBTQ Legal Advocates & Defenders (GLAD)".link("http://www.glad.org/")
    },
    {
      position: new google.maps.LatLng(42.366047650624644, -71.10206645100757),
      type: "Assault",
      message: "Boston Area Rape Crisis Center".link("https://barcc.org/")
    },
    {
      position: new google.maps.LatLng(42.35235824017516, -71.12067980866513),
      type: "Assault",
      message: "EVA Center".link("https://www.evacenter.org/")
    },
    {
      position: new google.maps.LatLng(42.351739270660765, -71.12023887797666),
      type: "Assault",
      message: "My Life My Choice".link("https://www.mylifemychoice.org/")
    },
    {
      position: new google.maps.LatLng(42.327965835122725, -71.08269876448483),
      type: "Assault",
      message: "Urban League of Eastern Massachusetts".link("https://www.ulem.org/")
    }
  ];
  
  // Create Array for popup messages
   popup = [];
  
  // Create markers
  for (let i = 0; i < pinpoint.length; i++) {
    var marker = new google.maps.Marker({
      position: pinpoint[i].position,
      icon: markers[pinpoint[i].type].icon,
      map: map,
    });
    popup[i] = pinpoint[i].message;
    messages: attachmessage(marker, popup[i]);
  }

  // Create Legend
  var legend = document.getElementById('legend');
  
  for (var key in markers) {
    var type = markers[key];
    var name = type.name;
    var icon = type.icon;
    var div = document.createElement('div');
    div.innerHTML = '<img src="' + icon + '"> ' + name;
    legend.appendChild(div);
  }
  
  // Put Legend onto top right of map
  map.controls[google.maps.ControlPosition.RIGHT_TOP].push
  (document.getElementById('legend'));
  
}

  // Function to attach popup messages to markers
  function attachmessage(marker, popup) {
    const infowindow = new google.maps.InfoWindow({
      content: popup
    });
    marker.addListener("click", () => {
      infowindow.open(marker.get("map"), marker);
    });
  }





      
      