<template>
  <div style="margin-top: 20px">
    <div>
      <el-row :gutter="20">
        <el-col :span="6">
          <el-image shape="square" style="width: 85px; height: 85px" :src="user.avatar" :preview-src-list="list"></el-image>
        </el-col>
        <el-col :span="13" style="text-align: left; margin-left: -10px">
          <el-row style="height: 50px">
            <span class="user-name">{{ user.name }}</span>
            <el-button type="text" style="margin-left: 10px" @click="handleChangeName">
              <i class="el-icon-edit"></i>
            </el-button>
          </el-row>
          <el-row style="height: 30px">
            <el-link href="/#/user_page/bidding">your offers</el-link>
            <el-divider direction="vertical"></el-divider>
            <el-link href="/#/user_page/manage_post">manage posts</el-link>
<!--            <el-divider direction="vertical"></el-divider>-->
<!--            <el-link>wanted list</el-link>-->
            <el-divider direction="vertical"></el-divider>
            <el-link href="/#/user_page/security">account security</el-link>
          </el-row>
         </el-col>
      </el-row>
    </div>
    <el-divider></el-divider>
    <div class="promotion">
      <div style="text-align: left">
        <span>special recommendations for you:</span>
      </div>
<!--      <el-carousel :interval="4000" type="card" style="margin-top: 30px">-->
<!--        <el-carousel-item v-for="item in 6" :key="item">-->
<!--          <h3 class="medium">{{ item }}</h3>-->
<!--        </el-carousel-item>-->
<!--      </el-carousel>-->
      <el-carousel :interval="4000" type="card" style="margin-top: 30px">
        <el-carousel-item v-for="item in recommendations" :key="item.id">
          <div class="item">
            <div class="item__content">{{ item.name }}</div>
            <router-link :to="{path:'/commodity_item',query: {id: item.id}}" v-if="item.photos.length > 0">
              <img class="item__image" :src="item.photos[0]" alt="Item Picture">
            </router-link>
            <router-link :to="{path:'/commodity_item',query: {id: item.id}}" v-else>
              <img class="item__image" src="src/assets/imgs/default_no_photo.jpg" alt="Item Picture">
            </router-link>
          </div>
        </el-carousel-item>
      </el-carousel>
    </div>
  </div>

</template>

<script>
export default {
  name: "UserDashboard",
  data () {
    return {
      user: {
        id: "",
        name: "",
        phone: "",
        avatar: "https://cdn.filestackcontent.com/rdABreSNSdCXTTwcRlz1"
      },
      recommendations: [],
      list: []
    }
  },
  created() {
    if (this.$store.state.email === '' || this.$store.state.email === null) {
      this.$router.push("/login");
    }
    this.$axios({
      method: 'post',
      url: '/consumer/',
      data: {
        email: this.$store.state.email
      }}).then(resp => {
        this.user.name = resp.data.data.name;
        if (resp.data.data.avatar != null) {
          this.user.avatar = resp.data.data.avatar;
          this.list.push(resp.data.data.avatar)
        } else {
          this.list.push(this.user.avatar)
        }
    })
    this.getRecommendation();
  },
  methods: {
    handleChangeName() {
      this.$prompt('please enter new nickname: ', 'NEW NICKNAME', {
        confirmButtonText: 'confirm',
        cancelButtonText: 'cancel'
      }).then(({ value }) => {
        console.log(value)
        this.$axios({
          method: "post",
          url: "/manage_profile/",
          data: {
            name: value,
            email: this.$store.state.email
          }
        })
      }).catch(() => {
        this.$message({
          type: 'info',
          message: 'cancel update!'
        });
      });
    },
    getRecommendation() {
      this.$axios.get('/top_recommendation', {params: {email: this.$store.state.email}})
      .then((response) => {
        console.log(this.$store.state.email)
        console.log(response.data.recommendations)
        this.recommendations = response.data.recommendations;
      })
    },
  }
}
</script>

<style scoped>
  .user-name {
    font-size: 25px;
    font-family: "Helvetica Neue", Helvetica, "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", "微软雅黑", Arial, sans-serif;
    font-weight: bold;
  }
  .promotion {
    margin: 0 50px 0 50px;
  }
  .el-carousel__item h3 {
    color: #475669;
    font-size: 14px;
    opacity: 0.75;
    line-height: 150px;
    margin: 0;
  }

  .el-carousel__item:nth-child(2n) {
    background-color: #99a9bf;
    width: 500px;
    height: 300px;
  }

  .el-carousel__item:nth-child(2n+1) {
    background-color: #d3dce6;
    width: 500px;
    height: 300px;
  }
</style>
