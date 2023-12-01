import { createApp } from "vue";
import axios from 'axios';
import { registerPlugins } from '@/plugins'



import App from './App.vue';
import router from './router';

const app = createApp(App);

registerPlugins(app)

axios.defaults.withCredentials = true;
axios.defaults.baseURL = 'http://localhost:8000/';  // the FastAPI backend

app.use(router);
app.mount("#app");


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
