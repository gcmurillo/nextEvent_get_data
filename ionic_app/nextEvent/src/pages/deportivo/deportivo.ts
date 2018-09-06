import { Component } from '@angular/core';
import { NavController } from 'ionic-angular';
import { RestProvider } from '../../providers/rest/rest';


@Component({
  selector: 'page-deportivo',
  templateUrl: 'deportivo.html'
})
export class DeportivoPage {

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
