import Vue from 'vue'
import Vuex from 'vuex'
import VueRouter from 'vue-router'

require('./bootstrap');

const mainWindow = require("./mainWindow/mainWindow.vue");

const routes = [
  {
    path: '/',
    name: 'root',
    component: mainWindow
  },
];

Vue.use(Vuex);

const store = require('./store.js');

const router = new VueRouter({
  routes
});

Vue.use(VueRouter);

import vSelect from 'vue-select';
Vue.component('v-select', vSelect);


import VueDialog from 'vuedialog';

import  {default as plugin, Component as Vuedals, Bus} from 'vuedals';
Vue.use(plugin);

VueDialog.setBus(Bus);

const app = new Vue({
  el: '#app',
  router,
  store,
  methods: {
  },
  components: {
    'vuedals': Vuedals,
    'vuedialog': VueDialog
  }
});
