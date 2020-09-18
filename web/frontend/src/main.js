import Vue from "vue";
import App from "./App.vue";
import Vuex from "vuex";
import store from "./vuex/store";
import router from "./routes";
import vuetify from "./plugins/vuetify";

import BootstrapVue from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

Vue.use(Vuex);
Vue.use(BootstrapVue)

new Vue({
  vuetify,
  router,
  store,
  beforeCreate() {
  },
  render: (h) => h(App),
}).$mount("#app");
