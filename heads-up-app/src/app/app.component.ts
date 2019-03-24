import { Component, OnInit, OnDestroy } from '@angular/core';
// import { Control } from '@angular/common';
import { LocationService } from './location.service';



@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  providers: [LocationService]
})
export class AppComponent implements OnInit, OnDestroy {
  allInfo = [];
  connection;
  info;

  // Map Info
  lat: number = 37.269148;
  lng: number = -76.715872+.0014;
  bearing = "NE";

  iconUrl = {
    url: require('./currentLocation.png'), // gives a data://<value>
    scaledSize: {
      height: 50,
      width: 50
    },
    anchor: { x: 555, y: 26 }
}

  // Speedometer Info
  gaugeType = "arch";
  speed = 0;
  // gaugeLabel = "Speed";
  gaugeAppendText = "mph";
  min = 0;
  max = 30;
  thick = 35;
  thresholdConfig = {
    '0': { color: '#0EE500' },
    '1': { color: '#28E701' },
    '2': { color: '#42EA02' },
    '3': { color: '#5CED03' },
    '4': { color: '#76F004' },
    '5': { color: '#91F305' },
    '6': { color: '#ABF606' },
    '7': { color: '#C5F907' },
    '8': { color: '#DFFC08' },
    '9': { color: '#FAFF0A' },
    '10': { color: '#FAF50A' },
    '11': { color: '#FBEB0A' },
    '12': { color: '#FBE20A' },
    '13': { color: '#FCD80A' },
    '14': { color: '#FCCE0A' },
    '15': { color: '#FDC50A' },
    '16': { color: '#FDBB0A' },
    '17': { color: '#FEB10A' },
    '18': { color: '#FFA80A' },
    '19': { color: '#FF9B0A' },
    '20': { color: '#FF8E0A' },
    '21': { color: '#FF810A' },
    '22': { color: '#FF740A' },
    '23': { color: '#FF670A' },
    '24': { color: '#FF4E0A' },
    '25': { color: '#FF410A' },
    '26': { color: '#FF340A' },
    '27': { color: '#FF270A' },
    '28': { color: '#FF1B0A' },
    '29': { color: '#DB1A14' },
    '30': { color: '#B8191F' }
  }

  styles = [
    {
        "featureType": "all",
        "elementType": "labels.text.fill",
        "stylers": [
            {
                "saturation": 36
            },
            {
                "color": "#000000"
            },
            {
                "lightness": 40
            }
        ]
    },
    {
        "featureType": "all",
        "elementType": "labels.text.stroke",
        "stylers": [
            {
                "visibility": "on"
            },
            {
                "color": "#000000"
            },
            {
                "lightness": 16
            }
        ]
    },
    {
        "featureType": "all",
        "elementType": "labels.icon",
        "stylers": [
            {
                "visibility": "off"
            }
        ]
    },
    {
        "featureType": "administrative",
        "elementType": "all",
        "stylers": [
            {
                "visibility": "off"
            }
        ]
    },
    {
        "featureType": "administrative",
        "elementType": "geometry.fill",
        "stylers": [
            {
                "color": "#000000"
            },
            {
                "lightness": 20
            }
        ]
    },
    {
        "featureType": "administrative",
        "elementType": "geometry.stroke",
        "stylers": [
            {
                "color": "#000000"
            },
            {
                "lightness": 17
            },
            {
                "weight": 1.2
            }
        ]
    },
    {
        "featureType": "landscape",
        "elementType": "all",
        "stylers": [
            {
                "visibility": "off"
            }
        ]
    },
    {
        "featureType": "landscape",
        "elementType": "geometry",
        "stylers": [
            {
                "color": "#000000"
            },
            {
                "lightness": 20
            }
        ]
    },
    {
        "featureType": "poi",
        "elementType": "all",
        "stylers": [
            {
                "visibility": "off"
            }
        ]
    },
    {
        "featureType": "poi",
        "elementType": "geometry",
        "stylers": [
            {
                "color": "#000000"
            },
            {
                "lightness": 21
            }
        ]
    },
    {
        "featureType": "road",
        "elementType": "all",
        "stylers": [
            {
                "visibility": "off"
            }
        ]
    },
    {
        "featureType": "road",
        "elementType": "geometry",
        "stylers": [
            {
                "visibility": "on"
            },
            {
                "saturation": "42"
            },
            {
                "lightness": "37"
            },
            {
                "color": "#d21616"
            }
        ]
    },
    {
        "featureType": "road",
        "elementType": "geometry.fill",
        "stylers": [
            {
                "visibility": "on"
            },
            {
                "color": "#891111"
            }
        ]
    },
    {
        "featureType": "road",
        "elementType": "geometry.stroke",
        "stylers": [
            {
                "visibility": "on"
            },
            {
                "color": "#a82d2d"
            }
        ]
    },
    {
        "featureType": "road",
        "elementType": "labels.text",
        "stylers": [
            {
                "visibility": "off"
            }
        ]
    },
    {
        "featureType": "road.highway",
        "elementType": "geometry.fill",
        "stylers": [
            {
                "color": "#000000"
            },
            {
                "lightness": 17
            }
        ]
    },
    {
        "featureType": "road.highway",
        "elementType": "geometry.stroke",
        "stylers": [
            {
                "color": "#000000"
            },
            {
                "lightness": 29
            },
            {
                "weight": 0.2
            }
        ]
    },
    {
        "featureType": "road.highway",
        "elementType": "labels.text",
        "stylers": [
            {
                "visibility": "off"
            }
        ]
    },
    {
        "featureType": "road.arterial",
        "elementType": "geometry",
        "stylers": [
            {
                "color": "#000000"
            },
            {
                "lightness": 18
            }
        ]
    },
    {
        "featureType": "road.arterial",
        "elementType": "labels.text",
        "stylers": [
            {
                "visibility": "off"
            }
        ]
    },
    {
        "featureType": "road.local",
        "elementType": "all",
        "stylers": [
            {
                "visibility": "on"
            }
        ]
    },
    {
        "featureType": "road.local",
        "elementType": "geometry",
        "stylers": [
            {
                "color": "#000000"
            },
            {
                "lightness": 16
            }
        ]
    },
    {
        "featureType": "road.local",
        "elementType": "labels.text",
        "stylers": [
            {
                "visibility": "off"
            }
        ]
    },
    {
        "featureType": "transit",
        "elementType": "all",
        "stylers": [
            {
                "visibility": "off"
            }
        ]
    },
    {
        "featureType": "transit",
        "elementType": "geometry",
        "stylers": [
            {
                "color": "#000000"
            },
            {
                "lightness": 19
            }
        ]
    },
    {
        "featureType": "transit.station",
        "elementType": "all",
        "stylers": [
            {
                "visibility": "off"
            }
        ]
    },
    {
        "featureType": "water",
        "elementType": "geometry",
        "stylers": [
            {
                "color": "#0f252e"
            },
            {
                "lightness": 17
            }
        ]
    }
]

  constructor(private locationService: LocationService) { }

  ngOnInit() {
    this.connection = this.locationService.getInfo().subscribe(info => {
      this.allInfo.push(info);
      console.log(info)
      this.lat = info['lat'];
      this.lng = info['long']+.0014;
      this.bearing = info['bearing'];
      this.speed = info['speed'];
    })
  }

  ngOnDestroy() {
    this.connection.unsubscribe();
  }

}
