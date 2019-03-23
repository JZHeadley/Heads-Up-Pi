import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  gaugeType = "arch";
  gaugeValue = 16.3;
  gaugeLabel = "Speed";
  gaugeAppendText = "mph";
  min = 0;
  max = 30;
  thick = 40;
  thresholdConfig = {
    '0': {color: '#0EE500'},
    '1': {color: '#28E701'},
    '2': {color: '#42EA02'},
    '3': {color: '#5CED03'},
    '4': {color: '#76F004'},
    '5': {color: '#91F305'},
    '6': {color: '#ABF606'},
    '7': {color: '#C5F907'},
    '8': {color: '#DFFC08'},
    '9': {color: '#FAFF0A'},
    '10': {color: '#FAF50A'},
    '11': {color: '#FBEB0A'},
    '12': {color: '#FBE20A'},
    '13': {color: '#FCD80A'},
    '14': {color: '#FCCE0A'},
    '15': {color: '#FDC50A'},
    '16': {color: '#FDBB0A'},
    '17': {color: '#FEB10A'},
    '18': {color: '#FFA80A'},
    '19': {color: '#FF9B0A'},
    '20': {color: '#FF8E0A'},
    '21': {color: '#FF810A'},
    '22': {color: '#FF740A'},
    '23': {color: '#FF670A'},
    '24': {color: '#FF4E0A'},
    '25': {color: '#FF410A'},
    '26': {color: '#FF340A'},
    '27': {color: '#FF270A'},
    '28': {color: '#FF1B0A'},
    '29': {color: '#DB1A14'},
    '30': {color: '#B8191F'}  
  }

  
}
