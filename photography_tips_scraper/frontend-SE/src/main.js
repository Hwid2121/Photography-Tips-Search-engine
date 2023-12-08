import { createApp } from "vue";
import axios from '../../backend/node_modules/axios';
import { registerPlugins } from '@/plugins'

import App from './App.vue';
import router from './router';

import VueCookies  from "vue-cookies";


const app = createApp(App);

registerPlugins(app)

axios.defaults.withCredentials = true;
axios.defaults.baseURL = process.env.VUE_APP_BASE_URL;  // the FastAPI backend

app.use(router);
app.mount("#app");
console.log('process.env.VUE_APP_BASE_URL', process.env.VUE_APP_BASE_URL)

app.use(VueCookies);



// /**
//  * main.js
//  *
//  * Bootstraps Vuetify and other plugins then mounts the App`
//  */

// // Plugins
// import { registerPlugins } from '@/plugins'

// // Components
// import App from './App.vue'

// // Composables
// import { createApp } from 'vue'

// const app = createApp(App)

// registerPlugins(app)

// app.mount('#app')
