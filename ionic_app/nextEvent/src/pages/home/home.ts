import { Component } from '@angular/core';
import { NavController } from 'ionic-angular';
import { RestProvider } from '../../providers/rest/rest';

@Component({
  selector: 'page-home',
  templateUrl: 'home.html'
})
export class HomePage {

  data: any;

  constructor(public navCtrl: NavController, public restProvider: RestProvider) {
      this.getData();
  }

  getData() {
    this.restProvider.getData()
      .then(data => {
        this.data = data;
        console.log(this.data);
      });
  }

}
