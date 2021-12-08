<template>
  <div>
    <el-menu :default-openeds="['1', '4']" class="el-menu" :router="true" :default-active="$route.path">
      <el-submenu index="1">
        <template slot="title"><i class="el-icon-user-solid"></i>Personal Center</template>
        <el-menu-item index="/user_page/dashboard"><i class="el-icon-user"></i>My Profile</el-menu-item>
        <el-menu-item index="/user_page/avatar"><i class="el-icon-picture-outline-round"></i>My Avatar</el-menu-item>
        <el-menu-item index="/user_page/manage_post"><i class="el-icon-goods"></i>Manage Goods</el-menu-item>
        <el-menu-item index="/user_page/security"><i class="el-icon-help"></i>Security</el-menu-item>
      </el-submenu>
<!--      <el-menu-item index="2">-->
<!--        <template slot="title"><i class="el-icon-star-on"></i>My Star Items</template>-->
<!--      </el-menu-item>-->
      <el-menu-item index="/user_page/bidding">
        <template slot="title"><i class="el-icon-s-comment"></i>My Offers</template>
      </el-menu-item>
      <el-submenu index="4">
        <template slot="title"><i class="el-icon-question"></i>Help Center</template>
        <el-menu-item index="/user_page/about_us">About Us</el-menu-item>
        <el-menu-item index="/user_page/contact_us">Contact Us</el-menu-item>
        <el-menu-item index="/user_page/common_questions">Common Questions</el-menu-item>
      </el-submenu>
    </el-menu>
  </div>
</template>

<script>
export default {
  name: "UserSideBar",
  methods: {

  }
}
</script>

<style scoped>
  /deep/ .el-menu {
    background-color: rgba(255, 255, 255, 0);
  }
</style>
