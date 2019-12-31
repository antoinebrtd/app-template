import Vue from "vue";
import App from "./App";
import axios from "axios";

import vuetify from './plugins/vuetify';
import router from "./modules/router";
import auth from "./modules/auth";

Vue.config.productionTip = process.env.NODE_ENV === "production";
axios.defaults.withCredentials = true;


new Vue({
  router,
  vuetify,
  render: h => h(App)
}).$mount('#app');


Vue.mixin({
  data() {
    return {
      $_profile: auth.user.profile
    }
  }
});
