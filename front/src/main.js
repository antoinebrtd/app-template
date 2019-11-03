import Vue from "vue";
import vuetify from './plugins/vuetify';
import App from "./App";
import router from "./modules/router";
import axios from "axios";

import auth from "./modules/auth";

Vue.config.productionTip = process.env.NODE_ENV === "production";
axios.defaults.withCredentials = true;

new Vue({
  router,
  vuetify,
  render: h => h(App)
}).$mount('#app')

Vue.mixin({
  data() {
    return {
      $_profile: auth.user.profile
    }
  }
});