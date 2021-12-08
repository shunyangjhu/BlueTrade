<template>
  <div class="bg" style="overflow: auto">
    <el-container class="container" style="max-height: 92%; width: 95%">
      <el-main v-if="commodity">
        <el-page-header title="back" @back="goBack" :content="'Commodity detail for ' + commodity.name"  style="margin: 10px 0 0 5px"></el-page-header>
        <el-divider></el-divider>
        <div>
          <el-col :span="8">
            <el-card body-style="padding: 0px">
              <div style="position: relative; left: 0px; top: 0px;">
                <el-carousel trigger="click" v-if="commodity.photos.length != 0" style="height: 450px">
                  <el-carousel-item v-for="imgUrl in commodity.photos" :key="imgUrl" style="height: 450px" >
                    <img :src="imgUrl"
                         alt="Item Picture" height="100%" width="100%" fit="contain" />
                  </el-carousel-item>
                </el-carousel>
                <el-carousel trigger="click" style="height: 450px" v-else>
                  <el-carousel-item style="height: 450px">
                    <img src="../../assets/imgs/default_no_photo.jpg"
                         height="100%" width="100%"
                         fit="contain"
                         alt="Item Picture" />
                  </el-carousel-item>
                </el-carousel>
              </div>
              <div>
                <span>{{ commodity.name }}</span><br>
                <span class="time">{{ commodity.updateDate }}</span>
              </div>
            </el-card>
          </el-col>
          <el-col :span="15">
            <el-row type="flex" justify="center">
              <el-col cols="6">Name:</el-col>
              <el-col cols="12">{{ commodity.name }}</el-col>
            </el-row>
            <el-divider></el-divider>
            <!--            <el-row type="flex" justify="center">-->
            <!--              <el-col cols="6">Owner:</el-col>-->
            <!--              <el-col cols="12">{{ commodity.owner }}</el-col>-->
            <!--            </el-row>-->
            <!--            <el-divider></el-divider>-->
            <el-row type="flex" justify="center">
              <el-col cols="6">Update date:</el-col>
              <el-col cols="12">{{ commodity.updateDate }}</el-col>
            </el-row>
            <!--          <el-divider></el-divider>-->
            <!--          <el-row type="flex" justify="center">-->
            <!--            <el-col cols="6" md="4">Location:</el-col>-->
            <!--            <el-col cols="12" md="8">{{ commodity.location }}</el-col>-->
            <!--          </el-row>-->
            <el-divider></el-divider>
            <el-row type="flex" justify="center">
              <el-col cols="6">Category:</el-col>
              <el-col cols="12">{{ commodity.category }}</el-col>
              <!--                <el-col cols="12">{{ commodity.category[0].toUpperCase() + commodity.category.slice(1) }}</el-col>-->
            </el-row>
            <el-divider></el-divider>
            <el-row type="flex" justify="center">
              <el-col cols="6">Price (USD):</el-col>
              <el-col cols="12" v-if="commodity.price > 0">$ {{ commodity.price }}</el-col>
              <el-col cols="12" v-else>Free</el-col>
            </el-row>
            <el-divider></el-divider>
            <el-row type="flex" justify="center">
              <el-col cols="6">Availability:</el-col>
              <el-col cols="12" v-if="commodity.onSale">Available</el-col>
              <el-col cols="12" v-else>Not Available</el-col>
            </el-row>
            <el-divider></el-divider>
            <el-row type="flex" justify="center">
              <el-col cols="6">Item Description:</el-col>
              <el-col cols="12">{{ commodity.description }}</el-col>
            </el-row>
            <el-divider></el-divider>
            <el-row type="flex" justify="center">
<!--              TODO: Add to list feature button-->
<!--              <el-button :type="isStarred ? 'primary' : 'default'" @click="addToStarred">-->
<!--                <i :class="isStarred ? 'el-icon-star-on' : 'el-icon-star-off'" id="starredButton" /> {{ this.isStarred ? 'Added' : 'Add to List' }}-->
<!--              </el-button>-->
              <el-button @click="checkPostAuthentication">
                <i class="el-icon-chat-dot-round" /> Leave Message & Make Offer
              </el-button>
            </el-row>
          </el-col>
        </div>

        <el-dialog :visible="showBiddingForm" width="30%" title="Make Offer and Leave Message" :show-close="false" append-to-body>
          <el-form :model="biddingForm">
            <el-form-item label="Price($): " prop="price">
              <el-input-number v-model="biddingForm.price" class="el-input" :min="0"></el-input-number>
            </el-form-item>
            <el-form-item label="Message: " prop="message">
              <textarea placeholder="Enter any message you wanna say to the owner.."
                        v-model="biddingForm.message"
                        style="height: 100px; width: 100%; max-width: 100%"/>
            </el-form-item>
            <el-form-item>
              <el-button type="primary" @click.prevent="postBidding" >Submit</el-button>
              <el-button type="info" @click="handleCloseForm">Cancel</el-button>
            </el-form-item>
          </el-form>
        </el-dialog>
      </el-main>

      <el-main v-else>
        <el-header style="float: left; color: slateblue">No Commodity Item Found.</el-header>
      </el-main>
    </el-container>
  </div>
</template>

<script>
export default {
  name: "CommodityItemPage",
  data() {
    return {
      testCommodity: [],
      commodity: null,
      id: null,
      error: null,
      showBiddingForm: false,
      biddingForm: {
        price: '',
        message: '',
        buyer: '',
        commodityId: ''
      },
      isStarred: false
    }
  },
  created() {
    if (this.$route.query.id != null)
    {
      // console.log('Item Id detected before get item')
      this.id = this.$route.query.id
    }
    //this.getCommodityItem()
    this.getTestItem()
  },
  methods: {
    getCommodityItem(){
      this.$axios.get('/search-id?id='+this.id, {
        params: {
          query: this.id
        }})
          .then((response) => {
            // console.log('data received from server: '+JSON.stringify(response.data))
            this.commodity = response.data
          })
          .catch(err => {
            console.log('error happened when making GET request: '+err)
            this.error.push(err)
          })
    },
    checkPostAuthentication() {
      this.$axios.get('/check_post_authentication', {
        params: {
          commodityId: this.id,
          buyer: this.$store.state.email
        }
      }).then(resp => {
        if (resp.data.data === true) {
          this.showBiddingForm = true;
        } else {
          this.$alert("You have already post an offer here. Please go to Your Offers page to manage!");
        }
      })
    },
    goBack(){
      this.$router.push('/commodity_list')
    },
    getTestItem(){
      this.$axios.get('/item?commodityId='+this.id)
          .then((response) => {
            //console.log('data received from server: '+JSON.stringify(response.data))
            this.commodity = response.data.data
            //console.log('Current commodity object: ' + JSON.stringify(this.commodity))
            //console.log(this.commodity.photos)
          })
    },
    postBidding(){
      //this.biddingForm.buyer = 'phe18@jhu.edu' //TODO: use user info from $store
      this.biddingForm.buyer = this.$store.state.email
      this.biddingForm.commodityId = this.id
      console.log(this.biddingForm)
      this.$axios.post('/post_bidding/', this.biddingForm)
          .then((response) => {
            // console.log('data received from server: '+ JSON.stringify(response.data))
            alert(response.data.data)
            this.showBiddingForm=false
            this.biddingForm.price = ''
            this.biddingForm.message = ''
          })
          .catch(error => {
            console.log(error)
          })
    },
    handleCloseForm(){
      const decision = confirm('Are you sure you want to close the dialog? You will lose anything you have entered.');
      if(decision){
        this.showBiddingForm=false
        this.biddingForm.price = ''
        this.biddingForm.message = ''
      }
    },
    addToStarred(){
      this.isStarred = !this.isStarred;
    }
  }
}
</script>

<style scoped>
.time {
  font-size: 13px;
  color: #999;
}
.carousel-inner>.item>img, .carousel-inner>.item>a>img {
  display: block;
  height: auto;
  max-width: 100%;
  line-height: 1;
  margin:auto;
  width: 100%;
}
</style>