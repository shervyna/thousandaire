import Vue from 'vue';
import Router from 'vue-router';
import Alphas from '../components/Alphas.vue';
import Simulation from '../components/Simulation.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/alphas',
      name: 'Alphas',
      component: Alphas,
    },
    {
      path: '/simulation',
      name: 'Simulation',
      component: Simulation,
    },
  ],
});
