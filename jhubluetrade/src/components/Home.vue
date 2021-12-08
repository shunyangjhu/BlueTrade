<template>
  <div>
    <nav-menu class="nav-menu"></nav-menu>
    <router-view :key="$route.fullPath" />
  </div>
</template>

<script>
import NavMenu from './common/NavMenu'
export default {
  name: "Home",
  components: {NavMenu}
}
</script>

<style scoped>
</style>
