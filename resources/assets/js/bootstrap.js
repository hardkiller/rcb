try {
  window.$ = window.jQuery = require('jquery');
} catch (e) {}

require('popper.js');
require('tooltip.js');
require('bootstrap');

window.Vue = require('vue');
window.VueRouter = require('vue-router');
