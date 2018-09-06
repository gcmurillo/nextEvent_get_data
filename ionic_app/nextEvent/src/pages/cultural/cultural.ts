import { Component } from '@angular/core';
import { NavController } from 'ionic-angular';
import { RestProvider } from '../../providers/rest/rest';
/**
 * Generated class for the CulturalPage page.
 *
 * See https://ionicframework.com/docs/components/#navigation for more info on
 * Ionic pages and navigation.
 */

@Component({
  selector: 'page-cultural',
  templateUrl: 'cultural.html',
})
export class CulturalPage {

    data: any;
    culture: any[] = [];

    constructor(public navCtrl: NavController, public restProvider: RestProvider) {
        this.getData();
    }

    filter (data) {
        for (let i of data){
            if (i.categoria == 'cultural') {
                this.culture.push(i);
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
        console.log(this.culture);
    }



}
