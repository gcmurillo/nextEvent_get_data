import { Component } from '@angular/core';
import { NavController } from 'ionic-angular';
import { RestProvider } from '../../providers/rest/rest';


@Component({
  selector: 'page-deportivo',
  templateUrl: 'deportivo.html'
})
export class DeportivoPage {

    data: any;
    sports: any[] = [];

    constructor(public navCtrl: NavController, public restProvider: RestProvider) {
        this.getData();
    }

    filter (data) {
        for (let i of data){
            if (i.categoria == 'deportivo') {
                this.sports.push(i);
            }
        }
    }

    getData() {
      this.restProvider.getData()
        .then(data => {
          this.data = data;
          // console.log(this.data);
          this.filter(this.data);
        });
        console.log(this.sports);
    }


}
