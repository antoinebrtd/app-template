// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from "vue";
import Vuetify from "vuetify";
import App from "./App";
import router from "./modules/router";
import axios from "axios";

import auth from "./modules/auth";

Vue.use(Vuetify, {
  theme: {
    primary: "#2196f3",
    secondary: '#ffc852',
    error: "#ff7a73",
    success: '#62bf70',
    tab: '#2b2b2b',
    gap: '#252525',
    grey: '#626262'
  }
});

Vue.config.productionTip = process.env.NODE_ENV === "production";
axios.defaults.withCredentials = true;

new Vue({
  el: "#app",
  router,
  components: {App},
  template: "<App/>"
});

Vue.mixin({
  data() {
    return {
      $_profile: auth.user.profile
    }
  }
});
