<template>
  <div>
    <span class="title_warp">Click to change your avatar~</span>
    <el-divider></el-divider>
<!--    <el-button>-->
    <el-image :src="avatarUrl" fit="fill" @click="changeAvatar" style="width: 200px; height: 200px; cursor: pointer">
    </el-image>
<!--    </el-button>-->
    <el-divider></el-divider>
    <span class="footer_remind">please upload image within 2M, required form: png, jpeg</span>
  </div>
</template>

<script>
export default {
  name: "AvatarManagement",
  data () {
    return {
      avatarUrl: "",
      newAvatarUrl: "",
    }
  },
  methods: {
    changeAvatar() {
      const options = {
        transformations: {
          crop: false,
          circle: true,
          rotate: true
        },
        onUploadDone: resp => {
          //console.log(resp)
          for (var i = 0, len = resp.filesUploaded.length; i < len; i++) {
            this.newAvatarUrl = resp.filesUploaded[i].url
          }
          this.$axios({
            method: 'post',
            url: '/change_avatar/',
            data: {
              email: this.$store.state.email,
              avatar: this.newAvatarUrl
            }
          }).then(resp => {
            if (resp.data.code === 200) {
              this.$message({
                type: "success",
                message: "success uploaded images!!"
              })
            }
          })
          this.$router.go(0)
        }
      };
      this.$client.picker(options).open();
    }
  },
  created() {
    this.$axios({
      method: 'post',
      url: '/consumer/',
      data: {
        email: this.$store.state.email
      }}).then(resp => {
        //console.log(resp.data.data.avatar)
        if (resp.data.data.avatar != null) {
          this.avatarUrl = resp.data.data.avatar;
        } else {
          this.avatarUrl = "https://cdn.filestackcontent.com/rdABreSNSdCXTTwcRlz1"
        }
    })
  }
}
</script>

<style scoped>
.footer_remind{
  font-size: 12px;
  font-family: Avenir, Helvetica, Arial, sans-serif;
  color: #8c939d;
}
.title_warp{
  font-size: 30px;
  font-family: "Hannotate SC", serif;
  margin-top: 20px;
}
</style>
