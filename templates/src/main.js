import Vue from 'vue'
import './plugins/vuetify'
import App from './App.vue'
import router from './router'
import {store} from './store'
import CKEditor from '@ckeditor/ckeditor5-vue';
import './registerServiceWorker'

var VueTruncate = require('vue-truncate-filter')

Vue.use(VueTruncate)
Vue.use( CKEditor );

Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
