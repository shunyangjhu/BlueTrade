<template>
  <div class="bg">
    <el-container class="container">
      <el-aside width="300px">
        <user-side-bar></user-side-bar>
      </el-aside>
      <el-main>
        <router-view></router-view>
      </el-main>
    </el-container>
  </div>
</template>

<script>
import UserSideBar from "./UserSideBar";
export default {
  name: "UserPage",
  components: {UserSideBar},
  data () {
    return {}
  }
}
</script>

<style scoped>
</style>
