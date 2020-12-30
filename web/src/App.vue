<template>
  <div id="app">
    <sidebar-menu :menu="menu" />
    <router-view />
  </div>
</template>

<script>
export default {
  data() {
    return {
      menu: [
        {
          header: true,
          title: 'Thousandaire',
          hiddenOnCollapse: true,
        },
        {
          title: 'Alphas',
          icon: 'fa fa-code',
          child: [
            {
              href: '/alphas',
              title: 'Alpha List',
              icon: 'fa fa-list-ul',
            },
            {
              href: '/simulation',
              title: 'Simulation',
              icon: 'fa fa-flask',

            },
          ],
        },
        {
          href: '/metrics',
          title: 'Metrics',
          icon: 'fa fa-chart-line',
        },
      ],
    };
  },
};
</script>

<style>
#app {
  margin-top: 60px;
  font-family: 'Open Sans', sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
