import { Component } from '@angular/core';

import { DeportivoPage } from '../deportivo/deportivo';
import { ContactPage } from '../contact/contact';
import { HomePage } from '../home/home';

@Component({
  templateUrl: 'tabs.html'
})
export class TabsPage {

  tab1Root = HomePage;
  tab2Root = DeportivoPage;
  tab3Root = ContactPage;

  constructor() {

  }
}
