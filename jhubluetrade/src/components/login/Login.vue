<template>
  <div class="bg">
    <div class="login_out">
      <el-row type="flex" justify="center">
        <el-form :model="loginForm" :rules="rules" status-icon label-width="120px">
          <h3 class="login_title">Log In</h3>
          <el-form-item label="email " prop="email">
            <el-input v-model="loginForm.email" class="el-input" prefix-icon="el-icon-user"></el-input>
          </el-form-item>
          <el-form-item label="password " prop="password">
            <el-input type="password" show-password v-model="loginForm.password" autocomplete="off" prefix-icon="el-icon-key"></el-input>
          </el-form-item>
          <el-form-item  label="verify code " prop="verify_code">
            <el-input v-model="loginForm.verify_code" placeholder="please enter the verify code"></el-input>
          </el-form-item>
          <el-form-item>
            <div @click="refreshValidateCode" class="validate_box">
              <Validate :validateCode="validateCode"></Validate>
              <el-button type='text' class="validate_btn">refresh</el-button>
            </div>
          </el-form-item>
          <el-form-item style="margin-top: -10px">
            <el-button type="text"
                       style="color: #ece0a5; font-family: 'Hannotate SC', serif; font-size: 18px; width: 40%; margin-left: -90px"
                       @click="login">login</el-button>
            <router-link to="register"><el-button type="text" style="color: #ece0a5; font-family: 'Hannotate SC', serif; font-size: 18px">register</el-button></router-link>
          </el-form-item>
        </el-form>
      </el-row>
    </div>
  </div>
</template>

<script>
import Validate from "./Validate";
export default {
  name: "Login",
  data(){
    const validateEmail = (rule, value, callback) => {
      if (value.search("([\\w\\.])+@jh(.)*\\.edu$") === -1) {
        callback("this is not an valid JHU email!");
      } else {
        callback();
      }
    }
    return{
      loginForm: {
        email: '',
        password: '',
        verify_code: ''
      },
      validateCode: '',
      rules: {
        email: [
          { validator: validateEmail, trigger: 'blur', required: true }
        ],
      }
    }
  },
  mounted() {
    this.generateValidateCode();
  },
  components: {Validate},
  methods: {
    generateRandomNumber() {
      return Math.floor(Math.random() * 10);
    },
    generateValidateCode() {
      for (let i = 0; i < 4; i++) {
        this.validateCode += this.generateRandomNumber().toString();
      }
    },
    refreshValidateCode() {
      this.validateCode = '';
      this.generateValidateCode();
    },
    login() {
      if (this.validateCode === this.loginForm.verify_code) {
        this.$axios({
          method: 'post',
          url: '/login/',
          data: {
            email: this.loginForm.email,
            password: this.loginForm.password
          }
        }).then(resp => {
          //console.log(resp)
          if (resp.data.code === 200) {
            this.$alert("successful login!");
            this.$store.commit('login', this.loginForm.email);
            this.$router.push('/commodity_list');
            //console.log(this.$store.state.email);
          } else {
            this.$message({
              type: "error",
              message: "wrong email or password!"
            })
          }
        })
      } else {
        this.$message({
          type: "error",
          message: "wrong validate code! please reenter!"
        })
      }
    }
  }

}
</script>

<style scoped>
@import "../../styles/bg.css";
  .login_out {
    width: 500px;
    height: 410px;
    margin: 150px auto;
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
  .validate_box{
    display: flex;
    margin-left: -50px;
    cursor: pointer;
  }
  .validate_btn{
    color: #ece0a5;
    font-family: "Hannotate SC", serif;
    font-size: 18px;
    margin-bottom: 10px;
    padding-left: 30px;
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
