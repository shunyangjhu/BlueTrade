<template>
  <div class="bg">
    <div class="login_out">
      <el-row type="flex" justify="center">
        <el-form :model="registerForm" :rules="rules" ref="registerForm" status-icon label-width="180px" style="margin-right: 10px; margin-left: -30px">
          <h3 class="login_title">Register</h3>
          <el-form-item label="username: " prop="username">
            <el-input v-model="registerForm.username" class="el-input" prefix-icon="el-icon-user"></el-input>
          </el-form-item>
          <el-form-item label="password: " prop="password">
            <el-input type="password " show-password v-model="registerForm.password" autocomplete="off" prefix-icon="el-icon-key"></el-input>
          </el-form-item>
          <el-form-item label="confirm password: " prop="confirm_password">
            <el-input type="password " show-password v-model="registerForm.confirm_password" autocomplete="off" prefix-icon="el-icon-key"></el-input>
          </el-form-item>
          <el-form-item label="JHU email: " prop="jhu_email">
            <el-input v-model="registerForm.jhu_email" autocomplete="off" prefix-icon="el-icon-message"></el-input>
          </el-form-item>
          <el-form-item>
            <el-button type="text"
                       style="color: #ece0a5; font-family: 'Hannotate SC', serif; font-size: 18px; width: 40%; margin-left: -150px"
                       @click="register">register</el-button>
          </el-form-item>
        </el-form>
      </el-row>
    </div>
  </div>
</template>

<script>
export default {
  name: "Register",
  data(){
    const validatePass = (rule, value, callback) => {
      if (this.registerForm.confirm_password !== '') {
        this.$refs.registerForm.validateField('confirm_password');
      }
      callback();
    };
    const validatePass2 = (rule, value, callback) => {
      if (value !== this.registerForm.password) {
        callback(new Error('inconsistent password!'));
      } else {
        callback();
      }
    };
    const validateEmail = (rule, value, callback) => {
      if (value.search("([\\w\\.])+@jh(.)*\\.edu$") === -1) {
        callback("this is not an valid JHU email!");
      } else {
        callback();
      }
    }
    return{
      registerForm: {
        username: '',
        password: '',
        confirm_password: '',
        jhu_email: ''
      },
      rules: {
        username: [
          { required: true, message: 'please enter the username!', trigger: 'blur' },
        ],
        password: [
          { required: true, message: 'please enter the password!', trigger: 'blur' },
          { min: 6, max: 16, message: 'length should be in 6 to 16', trigger: 'blur' },
          { validator: validatePass, trigger: 'blur' }
        ],
        confirm_password:[
          { required: true, message: 'please confirm the password!', trigger: 'blur' },
          { min: 6, max: 16, message: 'length should be in 6 to 16', trigger: 'blur' },
          { validator: validatePass2, trigger: 'blur', required: true }
        ],
        jhu_email: [
          { required: true, message: 'please enter the JHU email!', trigger: 'blur' },
          { validator: validateEmail, trigger: 'blur', required: true }
        ],
      }
    }
  },
  methods: {
    register() {
      this.$axios({
        method: 'post',
        url: '/register/',
        data: {
          name: this.registerForm.username,
          email: this.registerForm.jhu_email,
          password: this.registerForm.password
        },
      }).then(resp => {
        if (resp.status === 200) {
          this.$alert("Congrats! Successfully register!");
        } else {
          this.$alert("You have already registered! Please log in directly!");
        }
        this.$router.push("/login/");
      })
    }
  }

}
</script>

<style scoped>
@import "../../styles/bg.css";
.login_out {
  width: 500px;
  height: 400px;
  margin: 200px auto;
  overflow: hidden;
  padding-top: 30px;
  line-height: 20px;
  background-color: rgba(37, 47, 76, 0.9);
}
.login_title {
  font-family: "Hannotate SC", serif;
  font-size: 30px;
  margin: 5px auto 50px auto;
  text-align: center;
  color: #ffffff;
}
/deep/ .el-form-item label {
  font-family: "Hannotate SC", serif;
  font-size: 18px;
  color: #ffffff;
}
/deep/ .el-input__inner {
  height: 40px;
  background-color: rgba(255, 255, 255, 0.3);
}
/deep/ .el-input input {
  color: #ffffff !important;
}
</style>
