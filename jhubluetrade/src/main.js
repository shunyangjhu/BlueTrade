import Vue from 'vue'
import App from './App.vue'
import router from './router'
import ElementUI from 'element-ui';
import * as filestack from 'filestack-js';
import locale from '../node_modules/element-ui/lib/locale/lang/en';
import "element-ui/lib/theme-chalk/index.css";
import global from "./assets/global";
import axios from "axios"
import store from './store'

//axios.defaults.baseURL = 'http://localhost:8000/api'
axios.defaults.baseURL = 'https://bluetrade.herokuapp.com/api'
// axios.defaults.baseURL = 'http://localhost:8443/api'
// axios.defaults.withCredentials = true

axios.defaults.timeout = 5000;
axios.defaults.headers = {
  "Content-Type": "application/json",
};
const client = filestack.init('A6KZwO1u8QfureQLP9SDDz');

Vue.prototype.$axios = axios
Vue.prototype.$global = global
Vue.prototype.$client = client
Vue.config.productionTip = false

Vue.use(ElementUI, {locale});

new Vue({
  render: h => h(App),
  router,
  store
}).$mount('#app')

// axios.get("/authentication").then(resp => {
//   global.user.id = resp.data.id;
//   global.user.username = resp.data.user;
// })

// router.beforeEach(() => {
//
// })
