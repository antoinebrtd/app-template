import Vue from 'vue';
import Vuetify from 'vuetify/lib';

Vue.use(Vuetify);

export default new Vuetify({
  icons: {
    iconfont: 'mdi',
  },
  theme:{
    primary: "#2196f3",
    secondary: '#ffc852',
    error: "#ff7a73",
    success: '#62bf70',
    tab: '#2b2b2b',
    gap: '#252525',
    grey: '#626262'
  }
});
