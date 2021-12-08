<template>
  <div class="bg" style="overflow: auto">
    <el-container class="container">
      <el-main>
        <el-scrollbar>
          <el-page-header title="back" @back="goBack" content="Edit Profile" style="margin: 20px 0 0 5px"></el-page-header>
          <el-divider></el-divider>
          <el-row type="flex" justify="center">
            <el-form :model="editProfileForm" :rules="rules" ref="editProfileForm" label-width="120px" class="post-container">
              <el-form-item label="Username" prop="username">
                <el-input v-model="editProfileForm.name" class="el-input"
                          placeholder="Please enter a username"></el-input>
              </el-form-item>
              <el-form-item label="Email" prop="email">
                <el-input v-model="editProfileForm.email" class="el-input"
                          placeholder="Example: bluejade@jhu.edu"></el-input>
              </el-form-item>
              <el-form-item label="Password" prop="password">
                <el-input type="password" show-password v-model="editProfileForm.password" autocomplete="off"
                          placeholder="Enter password: length should be in 6 to 16"></el-input>
              </el-form-item>
              <el-form-item label="Confirm Password" prop="confirm password">
                <el-input show-password v-model="editProfileForm.password2" autocomplete="off"
                          placeholder="Confirm your password"></el-input>
              </el-form-item>
              <el-form-item>
                <el-button type="primary" @click="EditPost" style="margin-left: -90px">Submit Changes</el-button>
              </el-form-item>
            </el-form>
          </el-row>
        </el-scrollbar>
      </el-main>
    </el-container>
  </div>
</template>

<script>
export default {
  name: "EditPost",
  data() {
    const validatePass = (rule, value, callback) => {
      if (this.editProfileForm.password2 !== '') {
        this.$refs.editProfileForm.validateField('password2');
      }
      callback();
    };
    const validatePassConfirm = (rule, value, callback) => {
      if (value !== this.editProfileForm.password) {
        callback(new Error("Passwords do not match."));
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
    return {
      dialogImageUrl: '',
      dialogVisible: false,
      fileList: [],
      editProfileForm: {
        username: '',
        email: '',
        password: '',
        password2:'',
      },
      rules: {
        username: [
          { required: true, message: 'Please enter a username!', trigger: 'blur' },
        ],
        password: [
          { required: true, message: 'Please enter a password!', trigger: 'blur' },
          { min: 6, max: 16, message: 'length should be in 6 to 16', trigger: 'blur' },
          { validator: validatePass, trigger: 'blur' }
        ],
        password2:[
          { required: true, message: 'Please re-enter password!', trigger: 'blur' },
          { min: 6, max: 16, message: 'length should be in 6 to 16', trigger: 'blur' },
          { validator: validatePassConfirm, trigger: 'blur', required: true }
        ],
        email: [
          { required: true, message: 'Please enter a JHU email!', trigger: 'blur' },
          { validator: validateEmail, trigger: 'blur', required: true }
        ],
      }
    }
  },
  methods: {
    register() {
      this.$axios({
        method: 'post',
        url: '/edit_profile/',
        data: {
          name: this.editProfileForm.username,
          email: this.editProfileForm.email,
          password: this.editProfileForm.password,
          password2: this.editProfileForm.password2,
        },
      }).then(resp => {
        if (resp.status === 200) {
          this.$alert("Congrats! Profile change was successful!");
        } else {
          this.$alert("You haven't made any change to your profile!");
        }
        this.$router.push("/login");
      })
    }
  }
}
</script>

<style scoped>
@import "../../styles/bg.css";
.post-container {
  margin: 20px auto;
  width: 600px;
  padding: 0 50px 50px 50px;
}
.avatar-uploader-icon {
  font-size: 28px;
  color: #8c939d;
  width: 178px;
  height: 178px;
  line-height: 178px;
  text-align: center;
}
.card-block {
  border: 1px dashed #d9d9d9;
  border-radius: 6px;
  cursor: pointer;
  position: relative;
  overflow: hidden;
  background-color: transparent;
}
.card-block:hover {
  border-color: #409EFF;
}
</style>
