import Vue from 'vue'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import App from './App.vue'
import VueRouter from "vue-router";
import VueResource from 'vue-resource'


Vue.use(VueRouter);
Vue.use(VueResource);
Vue.use(ElementUI)

import echarts from "echarts"
import listPage from './component/ListPage.vue'
import detailComponent from './component/Detail.vue'
import creatComponent from './component/createProject.vue'

// 创建一个路由器实例
// 并且配置路由规则
const router = new VueRouter({
  mode: 'history',
  base: __dirname,
  routes: [
    {
      path: '/',
      component: listPage
    },
    {
      path: '/coin/:coinname',
      component: detailComponent
    },
    {
      path: '/crprot',
      component: creatComponent
    }
  ]
})

const app = new Vue({
  router: router,
  render: h => h(App)
}).$mount('#app')
