<template>
  <div id="app">
    <router-view :key="$route.fullPath" />
  </div>
</template>

<script>
import NavMenu from './components/common/NavMenu'

export default {
  name: 'App',
  // eslint-disable-next-line vue/no-unused-components
  components: {NavMenu}
}
</script>

<style>
@import "styles/reset.css";
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
