<template>
  <div style="margin-top: 20px">
    <span class="title_warp">Account Security</span>
    <el-divider></el-divider>
    <div class="security_form">
      <el-row type="flex" justify="center">
        <el-form :model="securityForm" status-icon label-width="120px">
          <el-form-item label="email: " prop="email" disabled>
            <span style="color: #8c939d">{{ securityForm.email }}</span>
            <i class="el-icon-lock" style="margin-left: 10px"></i>
          </el-form-item>
          <el-form-item label="phone: " prop="phone">
            <el-button type="text">
              <div v-if="securityForm.phone === null || securityForm.phone.length === 0">
                <span>you have not set up phone yet, click to set!</span>
              </div>
              <div v-else>
                <span>{{ securityForm.phone }}</span>
              </div>
            </el-button>
          </el-form-item>
        </el-form>
      </el-row>

    </div>
  </div>
</template>

<script>
export default {
  name: "SecurityManagement",
  data() {
    return {
      securityForm: {
        email: this.$store.state.email,
        phone: "",

      }
    }
  },
  created() {
    this.email = this.$store.state.email;
  }
}
</script>

<style scoped>
.title_warp {
  font-size: 30px;
  font-family: "Hannotate SC", serif;
  margin-top: 20px;
}
.security_form {
  width: 500px;
  height: 200px;
  margin: 200px auto;
  overflow: hidden;
  padding-top: 30px;
  line-height: 20px;
  background-color: rgba(255, 255, 255, 0.5);
}

/deep/ .el-form-item label {
  font-family: "Yu Gothic",serif;
  font-size: 20px;
  font-weight: bold;
  color: #000000;
}

/deep/ .el-input input {
  color: #ffffff !important;
}
</style>