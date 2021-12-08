<template>
  <div class="bg">
    <el-container class="container" style="max-height: 92%; width: 95%">
      <el-main v-if="commodityList">
        <!--        <el-row style="position: relative; margin-right:90%; margin-bottom: 1%;">-->
        <!--          <el-select v-model="filterValue" value-key="value" placeholder="Select">-->
        <!--            <el-option v-for="item in filterOptions" :key="item.value" :label="item.label" :value="item">-->
        <!--              {{ item.label }}-->
        <!--            </el-option>-->
        <!--          </el-select>-->
        <!--        </el-row>-->
        <el-row>
          <div id="sortBox" style="padding-bottom: 10px; float: left">
            <el-select v-model="selectedFilter" value-key="id" placeholder="Sort By...">
              <el-option
                  v-for="item in filterOptions"
                  :key="item.label"
                  :label="item.label"
                  :value="item.value">
              </el-option>
            </el-select>
          </div>
        </el-row>
        <el-row>
          <!--<search-bar></search-bar>-->
          <el-tooltip effect="dark" placement="right"
                      v-for="item in sortedList"
                      :key="item.id">
            <p slot="content" style="font-size: 14px;margin-bottom: 6px;">{{ item.name }}</p>
            <p slot="content" style="font-size: 13px;margin-bottom: 6px">
              <!--              <span>{{item.owner}}</span> /-->
              <span>{{item.updateDate}}</span> /
              <!--          <span>{{item.location}}</span> /-->
              <span v-if="item.price > 0">For Sale</span>
              <span v-else>Free</span>
            </p>
            <p slot="content" style="width: auto; max-width: 300px;" class="brief">{{ item.description }}</p>

            <el-card class="commodityItem"
                     bodyStyle="padding:18px;" shadow="hover">
              <div class="cover">
                <router-link :to="{path:'/commodity_item',query: {id: item.id}}" v-if="item.photos.length > 0">
                  <img :src="item.photos[0]" alt="Item Picture">
                </router-link>
                <router-link :to="{path:'/commodity_item',query: {id: item.id}}" v-else>
                  <img src="../../assets/imgs/default_no_photo.jpg" alt="Item Picture">
                </router-link>
              </div>
              <div class="info">
                <div class="title">
                  <router-link :to="{path:'/commodity_item',query: {id: item.id}}">{{item.name}}</router-link>
                </div>
                <!--                <div class="title">-->
                <!--                  <a class="seller">{{item.owner}}</a>-->
                <!--                </div>-->
                <div class="title">
                  <a class="seller" v-if="item.price > 0">$ {{ item.price }}</a>
                  <a class="seller" v-else>Free</a>
                </div>
                <!--            <div class="title">-->
                <!--              <a class="seller">{{ item.location }}</a>-->
                <!--            </div>-->
                <div class="title">
                  <a class="seller">Update Date: {{ item.updateDate }}</a>
                </div>
                <!--            <div class="title">-->
                <!--              <a class="seller">Contact me <i class="far fa-comment" /></a>-->
                <!--            </div>-->
              </div>
              <!--          <a class="seller" href="">{{item.seller}}</a>-->
              <!--          <a class="seller" v-bind:href="'contact/' + item.id">Contact the seller</a>-->
            </el-card>
          </el-tooltip>
        </el-row>

<!--        <el-row>-->
<!--          <el-pagination-->
<!--              @current-change="setPage"-->
<!--              :hide-on-single-page="true"-->
<!--              layout="total, prev, pager, next, jumper"-->
<!--              :total="this.commodityList.length"-->
<!--              style="position: fixed; padding-left: 35%">-->
<!--          </el-pagination>-->
<!--        </el-row>-->
      </el-main>
      <el-main v-else>
        <el-header style="float: left">No Commodity Found.</el-header>
      </el-main>
    </el-container>
  </div>
</template>

<script>
export default {
  name: 'CommodityListPage',
  data () {
    return {
      commodityList: [],
      error: [],
      query: '',
      filterOptions: [{
        value: 'price_l2h',
        label: 'Price: low to high',
      }, {
        value: 'price_h2l',
        label: 'Price: high to low',
      }, {
        value: 'most_recent',
        label: 'Most recent updated',
      }, {
        value: 'least_recent',
        label: 'Oldest updated',
      }],
      selectedFilter: null,
      // page: 1,
      // pageSize: 14,
    }
  },
  created() {
    // this.filterValue = this.filterOptions[0]
    // console.log('Current filter is: ' + this.filterValue)
    //console.log('Query in commodityList:'+ this.$route.query.searchQuery);

    if (this.$route.query.searchQuery != null)
    {
      console.log('query detected before get list')
      this.query = this.$route.query.searchQuery
    }
    //this.getList()
    this.getTestList()
  },
  methods: {
    //get all the commodity
    getList(){
      this.$axios.get('/search/', {
        params: {
          query: this.query
        }
      })
          .then((response) => {
            // console.log('data received from server: ' + JSON.stringify(response.data))
            this.commodityList = response.data
          })
          .catch(err => {
            console.log('error happened when making GET request: '+err)
            this.error.push(err)
          })
    },
    getTestList(){
      this.$axios.get('/search/', {
        params: {
          searchQuery: this.query
        }
      })
          .then((response) => {
            // default ordering of data by update date
            // console.log('data received from server: ' + JSON.stringify(response.data))
            // this.commodityList = response.data.data.sort(function(a, b) {
            //   return new Date(b.updateDate) - new Date(a.updateDate);
            // })
            this.commodityList = response.data.data
          })
          .catch(err => {
            console.log('error happened when making GET request: '+err)
            this.error.push(err)
          })
    },
    //set the page number
    // setPage (val) {
    //   this.page = val
    // },
  },
  computed: {
    // Slice data for pagination
    // slicedListData(){
    //   return this.commodityList
    //       .slice(this.pageSize * this.page - this.pageSize, this.pageSize * this.page)
    // },
    //Sort List by selection
    sortedList(){
      let tempList = this.commodityList;
      switch (this.selectedFilter) {
        case "price_l2h":
          return tempList.slice().sort((a, b) => a.price - b.price);
        case "price_h2l":
          return tempList.slice().sort((a, b) => b.price - a.price);
        case "most_recent":
          return tempList.sort((a, b) => new Date(b.updateDate) - new Date(a.updateDate));
        case "least_recent":
          return tempList.sort((a, b) => new Date(a.updateDate) - new Date(b.updateDate));
        // case "category":
        //   return this.commodityList.filter(com => com.category == this.selectedFilter);
        default:
          return tempList.sort((a, b) => new Date(b.updateDate) - new Date(a.updateDate));
      }
    },
  }
}
</script>

<style scoped>
@import "../../styles/bg.css";
.commodityItem{
  width: 235px;
  margin-bottom: 50px;
  margin-right: 15px;
  height: 308px;
  float: left;
  text-align: center;
  /*padding-top: 50px;*/
}

.cover {
  width: 200px;
  height: 200px;
  margin-bottom: 7px;
  overflow: hidden;
  cursor: pointer;
}

img {
  width: 100%;
  height: 100%;
  /*margin: 0 auto;*/
}

.title {
  font-size: 14px;
  /*text-align: left;*/
}

.seller {
  color: #333;
  width: 102px;
  font-size: 13px;
  margin-bottom: 6px;
  /*text-align: left;*/
}

.brief {
  display: block;
  line-height: 17px;
}

a {
  text-decoration: none;
}

a:link, a:visited, a:focus {
  color: #3377aa;
}
</style>
