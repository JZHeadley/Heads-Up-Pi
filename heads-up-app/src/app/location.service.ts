import { Subject, Observable } from 'rxjs';
import * as io from 'socket.io-client';

export class LocationService {
  private url = 'http://localhost:5000';  
  private socket;
  
  getInfo() {
    let observable = new Observable(observer => {
      this.socket = io(this.url);
      this.socket.on('withdraw', (data) => {
        observer.next(data);    
      });
      return () => {
        this.socket.disconnect();
      };  
    })     
    return observable;
  }  
}