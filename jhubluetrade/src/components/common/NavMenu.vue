<template>
  <div>
    <el-row :gutter="24">
      <el-col :span="4">
        <router-link to="/home">
          <img src="../../assets/imgs/blueJadeLogo.jpeg" style="height: 60px; width: 105px;" />
        </router-link>
      </el-col>
      <el-col :span="10" style="padding-top: 15px; padding-left: 0">
        <el-input
            placeholder="Press Enter To Search"
            v-model="searchQuery"
            @input="updateSearchQuery"
            @keydown.enter.native.prevent="search"
            prefix-icon="el-icon-search"
            clearable>
        </el-input>
      </el-col>
      <el-col :span="10" style="float: right; padding-top: 3px">
        <el-menu :router="true" :default-active="$route.path" mode="horizontal" active-text-color="red">
          <el-menu-item v-for="(item,i) in navList" :key="i" :index="item.name" @click="comListClickListener">
            <div v-if="item.navItem === 'Profile'">
              <div v-if="$store.state.email !== null && $store.state.email.length !== 0">
                <el-dropdown @command="handleCommand">
                  <span class="el-dropdown-link">
                    {{ item.navItem }} <img :src="user.avatar" style="width:30px; height:30px;" class="el-avatar--circle"  alt=""/>
                  </span>
                  <el-dropdown-menu slot="dropdown">
                    <el-dropdown-item icon="el-icon-s-custom" @click="handleProfile" command="profile">profile</el-dropdown-item>
                    <el-dropdown-item icon="el-icon-goods" @click="handleManageGoods" command="manageGoods">manage goods</el-dropdown-item>
                    <el-dropdown-item icon="el-icon-s-comment" @click="handleMyOffers" command="myOffers">my offers</el-dropdown-item>
                    <el-dropdown-item icon="el-icon-upload2" @click="handleLogOut" command="logout">log out</el-dropdown-item>
                  </el-dropdown-menu>
                </el-dropdown>
              </div>
              <div v-else>
                <el-dropdown @command="handleCommand">
                <span class="el-dropdown-link">
                    {{ item.navItem }}
<!--                  <img :src="user.avatar" style="width:30px; height:30px;" class="el-avatar&#45;&#45;circle"  alt=""/>-->
                </span>
                  <el-dropdown-menu>
                    <el-dropdown-item icon="el-icon-download" @click="handleLogIn" command="login">log in</el-dropdown-item>
                  </el-dropdown-menu>
                </el-dropdown>
              </div>
            </div>
            <div v-else>
              {{ item.navItem }}
            </div>
          </el-menu-item>
          <!--      <span style="position: absolute;padding-top: 20px;right: 43%;font-size: 20px;font-weight: bold">BlueJade &#45;&#45; Second Hand First Choice</span>-->
        </el-menu>
      </el-col>
      <!--      <el-col :span="4">-->
      <!--        <el-menu :router="true" :default-active="$route.path" mode="horizontal" active-text-color="red">-->
      <!--          <el-menu-item style="float: right">-->
      <!--            <router-link to="/user_page/dashboard">-->
      <!--              <i class="el-icon-user" />Profile-->
      <!--            </router-link>-->
      <!--          </el-menu-item>-->

      <!--          &lt;!&ndash;      <el-menu-item index="/user_page/dashboard" style="float: right">&ndash;&gt;-->
      <!--          &lt;!&ndash;        <el-avatar :size="20" :src="circleUrl"></el-avatar>&ndash;&gt;-->
      <!--          &lt;!&ndash;      </el-menu-item>&ndash;&gt;-->
      <!--        </el-menu>-->
      <!--      </el-col>-->
    </el-row>
  </div>
</template>

<script>
export default {
  name: "NavMenu",
  data () {
    return {
      navList: [
        {name: '/post', navItem: 'Post Commodity', disabled: false},
        {name: '/commodity_list', navItem: 'All Commodities', disabled: false},
        // {name: '/login', navItem: 'Log In', disabled: false},
        {name: '', navItem: 'Profile', disabled: true},
      ],
      searchQuery: '',
      user: {
        id: "",
        email: "",
        name: "",
        phone: "",
        avatar: "https://cdn.filestackcontent.com/rdABreSNSdCXTTwcRlz1"
      },
    }
  },
  methods: {
    search(){
      // console.log('Enter key pressed with query: '+ this.searchQuery)
      //this.$router.push({name: 'CommodityListPage',params:{ searchQuery:this.searchQuery}});
      if (this.searchQuery !== ''){
        this.$router.push({path: '/commodity_list?searchQuery='+this.searchQuery});
      }
      else{
        this.$router.push({path: '/commodity_list'}).catch(err => {console.log(err)});
        //this.$router.go(0);
      }
    },
    handleCommand(command) {
      switch (command) {
        case "profile": this.handleProfile(); break;
        case "manageGoods": this.handleManageGoods(); break;
        case "myOffers": this.handleMyOffers(); break;
        case "login": this.handleLogIn(); break;
        case "logout": this.handleLogOut(); break
      }
    },
    handleProfile() {
      this.$router.push("/user_page/dashboard")
    },
    handleManageGoods() {
      this.$router.push("/user_page/manage_post")
    },
    handleMyOffers() {
      this.$router.push("/user_page/bidding")
    },
    handleLogIn() {
      this.$router.push("/login")
    },
    handleLogOut() {
      console.log("logout")
      this.$confirm("Are you sure to log out?", "Confirmation", {
        distinguishCancelAndClose: true,
        confirmButtonText: "Sure!",
        cancelButtonText: 'cancel'
      }).then(() => {
        console.log(this.$store.state.email)
        this.$store.commit("logout")
        this.$router.go(0);
        console.log(this.$store.state.email)
      }).catch((exp) => {
        console.log(exp)
        this.$message({
          type: 'info',
          message: "canceled!"
        })
      })
    },
    updateSearchQuery(){
      //TODO: need to fix the redundant path error, may or may not need this feature
      // console.log('searchQuery Changed to: ' + this.searchQuery)
      // if (this.searchQuery != ''){
      //   this.search()
      // }
      // else {
      //   this.$router.push({path: this.$route.path}).catch(err => {console.log(err)});
      // }
    },
    comListClickListener(){
      if (this.$route.name === 'CommodityListPage'){
        this.searchQuery=''
        //this.$router.go(0);
      }
    }
  },
  watch: {
    //prevent and replace special chars and extra white spaces for search
    searchQuery(value){
      this.searchQuery = value
          .replace(/(?!\w|\s|-)./g, '')
          .replace(/\s+/g, ' ')
          .trimStart()
      // .replace(/^(\s*)([\W\w]*)(\b\s*$)/g, '$2')
    }
  },
  created() {
    this.$axios({
      method: 'post',
      url: '/consumer',
      data: {
        email: this.$store.state.email
      }}).then(resp => {
      this.user.name = resp.data.data.name;
      if (resp.data.data.avatar != null) {
        this.user.avatar = resp.data.data.avatar;
      }
    })
  }
}
</script>

<style scoped>
@import "../../styles/bg.css";
.el-menu {
  background-color: rgba(255, 255, 255, 0.8);
}
</style>
