<template>
  <div class="accordion" role="tablist">
    <el-card no-body class="mb-1">
      <el-card-header header-tag="header" class="p-1" role="tab">
        <el-card-title class="head" block v-b-toggle.accordion-1 variant="info">Contact Us</el-card-title>
      </el-card-header>
      <el-collapse id="accordion-1" visible accordion="my-accordion" role="tabpanel">
        <el-card-body>
          <el-card-text class="body">If you encounter any questions, feel free to contact us at:</el-card-text>
          <div></div>
          <el-card-text class="body">{{ text }}</el-card-text>
          <div></div>
          <el-card-text class="body">If you have question about a specific order, please include your username and commodity name in the email. Please expect up to 48 hours from when the email is sent for us to reply. We are happy to assist you!</el-card-text>
        </el-card-body>
      </el-collapse>
    </el-card>
  </div>
</template>

<script>
export default {
  data() {
    return {
      text: `
          1961609155emanon@gmail.com
        `
    }
  }
}
</script>

<style scoped>
.head {
  font-size: 28px;
  font-family: "Hannotate SC", serif;
  margin-top: 15px;
  max-width: 80%;
}
.body {
  font-size: 18px;
  font-family: "Hannotate SC", serif;
  margin-top: 15px;
  max-width: 80%;
  text-align: left;
}
</style>