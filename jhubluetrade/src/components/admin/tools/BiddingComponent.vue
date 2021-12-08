<template>
  <div>
    <span class="title_warp">You can manage your buying and selling offers here~</span>
    <el-divider></el-divider>
    <el-collapse v-model="activeName"  @change="handleMainCollapse">
      <el-collapse-item name="buying">
        <template slot="title" class="collapse_title_warp">
          <i class="header-icon el-icon-goods" style="margin-right: 10px"></i>
          Your Buying Offers
        </template>
        <div>
          <el-table
              :row-style="getRowClass" :header-row-style="getRowClass" :header-cell-style="getRowClass"
              :data="buyerData"
              height="250"
              border
              style="width: 95%">
            <el-table-column
                prop="commodityName"
                label="commodity name"
                align="center"
                width="180">
            </el-table-column>
            <el-table-column
                prop="price"
                label="your price"
                align="center"
                width="100">
            </el-table-column>
            <el-table-column
                prop="highestPrice"
                label="highest price up to now"
                align="center"
                width="180">
            </el-table-column>
            <el-table-column prop="message" label="message" align="center"></el-table-column>
            <el-table-column label="status" align="center" width="180">
              <template slot-scope="scope">
                <span>{{handleStatus(scope.row.status)}}</span>
              </template>
            </el-table-column>
            <el-table-column
                fixed="right"
                label="manage"
                width="200"
                align="center">
              <template slot-scope="scope">
                <el-button @click="handleManageBidding(scope.row)" type="text"><span>{{
                    showManageOptions(scope.row.status)
                  }}</span></el-button>
                <el-dialog title="new offers" :visible.sync="dialogFormVisible" :append-to-body="true">
                  <el-form :model="biddingManageBox">
                    <el-form-item label="new message: " label-width="100px">
                      <el-input textarea v-model="biddingManageBox.message"></el-input>
                    </el-form-item>
                    <el-form-item label="new price: " label-width="100px">
                      <el-input v-model="biddingManageBox.price"></el-input>
                    </el-form-item>
                  </el-form>
                  <div slot="footer" class="dialog-footer">
                    <el-button @click="dialogFormVisible = false">cancel</el-button>
                    <el-button type="primary" @click="handleNewBidding(scope.row)">confirm</el-button>
                  </div>
                </el-dialog>
              </template>
            </el-table-column>
          </el-table>
        </div>
      </el-collapse-item>
      <el-collapse-item name="selling">
        <template slot="title" class="collapse_title_warp">
          <i class="header-icon el-icon-sell" style="margin-right: 10px"></i>
          Your Selling Offers
        </template>
        <div v-if="postList.length > 0">
          <el-collapse accordion v-model="seller_mode" @change="handleSellerCollapse">
          <div v-for="fit in postList.length" :key="fit" style="margin-left: 20px">
            <el-collapse-item :title="postList[fit- 1].name" :name="postList[fit- 1].id">
              <el-table
                  :row-style="getRowClass" :header-row-style="getRowClass" :header-cell-style="getRowClass"
                  :data="sellerData"
                  height="250"
                  border
                  style="width: 95%">
                <el-table-column
                    prop="buyerName"
                    label="buyer"
                    align="center"
                    width="180">
                </el-table-column>
                <el-table-column
                    prop="email"
                    label="email"
                    align="center"
                    width="180">
                </el-table-column>
                <el-table-column
                    prop="price"
                    label="price"
                    align="center"
                    width="100">
                </el-table-column>
                <el-table-column
                    prop="message"
                    label="message"
                    align="center">
                </el-table-column>
                <el-table-column
                    fixed="right"
                    label="operation"
                    width="100"
                    align="center">
                  <template slot-scope="scope">
                    <el-tooltip effect="dark" :content="handleDisableSelectTooltip(scope.row.status)" placement="top-end">
                      <div>
                        <el-button @click="handleSelect(scope.row)"
                                   icon="el-icon-check" size="small" circle type="success"
                                   :disabled="handleDisableSelect(scope.row)">
                        </el-button>
                      </div>
                    </el-tooltip>
                  </template>
                </el-table-column>
              </el-table>
            </el-collapse-item>
          </div>
        </el-collapse>
        </div>
        <div style="padding-top: 30px" v-else>
          <span style="color: slateblue">Sorry, you do not have any selling commodity yet. :(</span>
        </div>
      </el-collapse-item>
      <el-collapse-item name="completed">
        <template slot="title" class="collapse_title_warp">
          <i class="header-icon el-icon-finished" style="margin-right: 10px"></i>
          Your Completed Offers
        </template>
        <el-collapse style="margin-left: 30px">
          <el-collapse-item title="buying orders">
            <el-table
                :row-style="getRowClass" :header-row-style="getRowClass" :header-cell-style="getRowClass"
                :data="completedData.buyer"
                height="250"
                border
                style="width: 95%">
              <el-table-column
                  prop="commodityName"
                  label="commodity name"
                  align="center"
                  width="180">
              </el-table-column>
              <el-table-column
                  prop="price"
                  label="your price"
                  align="center"
                  width="100">
              </el-table-column>
              <el-table-column prop="message" label="message" align="center"></el-table-column>
              <el-table-column label="status" align="center" width="180">
                <template slot-scope="scope">
                  <span>{{handleStatus(scope.row.status)}}</span>
                </template>
              </el-table-column>
            </el-table>
          </el-collapse-item>
          <el-collapse-item title="selling orders">
            <el-table
                :row-style="getRowClass" :header-row-style="getRowClass" :header-cell-style="getRowClass"
                :data="completedData.seller"
                height="250"
                border
                style="width: 95%">
              <el-table-column
                  prop="name"
                  label="commodity name"
                  align="center"
                  width="180">
              </el-table-column>
              <el-table-column prop="buyer" label="buyer" align="center" width="180">
              </el-table-column>
              <el-table-column
                  prop="price"
                  label="price"
                  align="center"
                  width="100">
              </el-table-column>
              
            </el-table>
          </el-collapse-item>
        </el-collapse>
      </el-collapse-item>
    </el-collapse>
  </div>
</template>

<script>
export default {
  name: "BiddingComponent",
  data() {
    return {
      dialogFormVisible: false,
      activeName: ['selling'],
      seller_mode: "",
      sellerData: [],
      buyerData: [],
      postList: [],
      completedData: [],
      biddingManageBox: {
        price: "",
        message: ""
      }
    }
  },
  created() {
    this.$axios.get("/post_list", {params: {owner: this.$store.state.email}})
    .then(resp => {
      this.postList = resp.data.data;
    })
  },
  methods: {
    getRowClass() {
      return "background:#3f5c6d2c; color:#000; text-align:center";
    },
    handlePostList() {
      this.$axios.get("/post_list", {params: {owner: this.$store.state.email}})
          .then(resp => {
            this.postList = resp.data.data;
          })
    },
    handleSellerCollapse() {
      this.$axios.get("/seller_bidding", {params: {commodityId: this.seller_mode}})
      .then(resp => {
        this.sellerData = resp.data.data;
      })
      console.log(this.sellerData)
    },
    handleDisableSelectTooltip(row) {
      if (row === 1) return "you have selected this buyer."
      else return "select this buyer.";
    },
    handleDisableSelect(row) {
      return row.status === 1;

    },
    handleMainCollapse() {
      this.handleBuyerCollapse();
      this.handleCompletedCollapse();
      this.handlePostList();
      console.log(this.completedData)
    },
    handleBuyerCollapse() {
      this.$axios.get("/buying_bidding", {params: {buyer: this.$store.state.email}})
          .then(resp => {
            this.buyerData = resp.data.data;
          })
    },
    handleCompletedCollapse() {
      this.$axios.get("/completed_bidding", {params: {consumer: this.$store.state.email}})
          .then(resp => {
            this.completedData = resp.data.data;
          })
    },
    handleStatus(status) {
      switch (status) {
        case 0: return "Pending";
        case 1: return "Selected By the Seller";
        case 2: return "Not Selected Temporarily";
        case 3: return "Confirmed";
        case 4: return "Denied";
        default: return "Sorry we cannot find your status :(";
      }
    },
    handleNewBidding(row) {
      this.dialogFormVisible = false;
      this.$axios({
        method: 'post',
        url: '/update_bidding/',
        data: {
          commodityId: row.id,
          email: this.$store.state.email,
          price: this.biddingManageBox.price,
          message: this.biddingManageBox.message
        }
      }).then(resp => {
        if (resp.data.code === 200) {
          this.$message({
            type: 'success',
            message: "successfully updated!"
          });
          location.reload()
        } else {
          this.$message({
            type: 'error',
            message: 'fail to update!'
          });
        }
      });
    },
    showManageOptions(row) {
      if (row !== 1) {
        return "manage offer"
      } else {
        return "confirm this offer"
      }
    },
    handleManageBidding(row) {
      if (row.status !== 1) {
        this.dialogFormVisible = true
      } else {
        this.$confirm("Confirming this offer? (Please confirm after you finish this trade. Once you confirmed, you cannot connect to seller anymore.)")
            .then(() => {
              this.$axios({
                method: "post",
                url: "/complete_order/",
                data: {
                  commodityId: row.id,
                  name: row.commodityName,
                  buyer: row.buyer,
                  price: row.price
                }
              }).then(resp => {
                if (resp.data.code === 200) {
                  this.$message("Confirmed!");
                } else {
                  this.$message({
                    type: "error",
                    message: "failed!"
                  })
                }
              })
            }).catch(() => {
              this.$message({
                type: 'info',
                message: "canceled"
              })
            });
      }
    },
    handleSelect(row) {
      console.log(row)
      this.$confirm("Are you sure to confirm this offer?", "Confirmation", {
        distinguishCancelAndClose: true,
        confirmButtonText: "Sure!",
        cancelButtonText: 'cancel'
      }).then(() => {
          this.$axios({
            method: 'post',
            url: '/select/',
            data: {
              commodityId: row.id,
              email: row.email,
            }
          }).then(resp => {
            if (resp.data.code === 200) {
              this.$confirm("You can contact the buyer at this email: " + row.email, "Contact Info", {
                confirmButtonText: "Sure!",
              });
            } else {
              this.$message({
                type: "error",
                message: "sorry, fail to select due to some reasons :("
              })
            }
          })
      }).catch(() => {
        this.$message({
          type: 'info',
          message: "canceled!"
        })
      });
    }
  }
}
</script>

<style scoped>
.title_warp {
  font-size: 30px;
  font-family: "Hannotate SC", serif;
  margin-top: 20px;
}
.collapse_title_warp {
  font-size: 25px;
  font-weight: bold;
}
/deep/ .el-collapse-item__header, .el-collapse-item__content, .el-collapse-item__wrap {
  background-color: transparent;
}
/deep/ .el-collapse-item__wrap {
  background-color: transparent;
}
/deep/ .el-collapse-item__content {
  background-color: transparent;
}
/deep/  .el-table, .el-table__expanded-cell {
  background-color: transparent;
}
/deep/ .el-table tr, .el-table td, .el-table th {
  background-color: transparent !important;
}
</style>