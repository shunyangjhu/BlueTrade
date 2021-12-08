<template>
  <div>
    <el-header style="font-family: 'sans-serif'; font-size: 50px">Manage Your Commodities</el-header>
    <el-main>
      <div v-if="commodities.length > 0">
        <el-table
            :data="commodities"
            style="width:100%;"
            :header-cell-style = "setTableHeaderStyle"
            :default-sort = "{prop: 'updateDate', order: 'descending'}"
            border stripe height="450px">
          <el-table-column
              prop="name"
              label="Commodity Name"
              align="center"
              sortable
              width="150">
          </el-table-column>
          <el-table-column
              prop="price"
              label="Price($)"
              align="center"
              sortable
              width="120">
          </el-table-column>
          <el-table-column
              :formatter="cellValueRenderer"
              prop="onSale"
              label="Availability"
              align="center"
              sortable
              width="120">
          </el-table-column>
          <el-table-column
              prop="createDate"
              label="Date Created"
              align="center"
              sortable
              width="120">
          </el-table-column>
          <el-table-column
              prop="updateDate"
              label="Last Updated"
              align="center"
              sortable
              width="120">
          </el-table-column>
          <el-table-column
              prop="description"
              label="Description"
              align="center"
              width="auto">
          </el-table-column>
          <el-table-column
              label="Operations"
              align="center"
              width="300px">
            <template slot-scope="{ row }">
              <el-button type="primary" icon="el-icon-edit" round @click.prevent="updateCommodityInfoForm(row)">Edit</el-button>
              <el-button type="danger" icon="el-icon-delete" round @click.prevent="deleteCommodity(row)">Delete</el-button>
            </template>
          </el-table-column>
        </el-table>

        <el-dialog :visible="showUpdateForm" width="30%" title="Update Item Information" :show-close="false" append-to-body>
          <el-form :model="updateItemFormData">
            <el-form-item label="Name: " prop="name">
              <el-input v-model="updateItemFormData.name" class="el-input" style="width: 50%; float: left"></el-input>
            </el-form-item>
            <el-form-item label="Price($): " prop="price">
              <el-input-number v-model="updateItemFormData.price" class="el-input" :min="0" style="width: 50%; float: left"></el-input-number>
            </el-form-item>
            <el-form-item label="Is Available?" prop="onSale">
              <el-switch
                  v-model="updateItemFormData.onSale"
                  :active-value="true"
                  :inactive-value="false"
                  active-color="#13ce66"
                  style="float: left; padding-top: 10px">
              </el-switch>
            </el-form-item>
            <el-form-item label="Description: " prop="description">
              <textarea placeholder="Enter any message you wanna say to the owner.."
                        v-model="updateItemFormData.description"
                        style="height: 100px; width: 100%; max-width: 100%"/>
            </el-form-item>
            <el-form-item>
              <el-button type="primary" @click="updateCommodity">Submit</el-button>
              <el-button type="info" @click="handleDialogCancel">Cancel</el-button>
            </el-form-item>
          </el-form>
        </el-dialog>
      </div>
      <div style="padding-top: 30px" v-else>
        <span style="color: slateblue">Sorry, you have not posted any commodity yet.</span>
      </div>
    </el-main>
  </div>
</template>

<script>
export default {
  data() {
    return {
      commodities: [],
      showUpdateForm: false,
      updateItemFormData: {
        name: null,
        price: null,
        description: null,
        onSale: true
      }
    }
  },
  created() {
    this.getPostedCommodities()
  },
  methods: {
    getPostedCommodities(){
      this.$axios.get('/post_list', {
        params: {
          //owner: 'seller1@jhu.edu' //TODO: use user info from $store
          owner: this.$store.state.email
        }
      })
          .then((response) => {
            //console.log('data received from server: '+JSON.stringify(response.data))
            this.commodities = response.data.data
          })
    },
    updateCommodityInfoForm(rowData){
      const itemInfo = rowData
      this.updateItemFormData = itemInfo
      this.showUpdateForm = true
    },
    updateCommodity(){
      console.log(this.updateItemFormData)
      this.$axios.post('/update_item/', this.updateItemFormData)
          .then((response) => {
            console.log('data received from server: '+JSON.stringify(response.data))
            alert(response.data.data)
            if(response.data.data === 'update successfully!'){
              this.showUpdateForm = false
            }
          })
    },
    deleteCommodity(rowData){
      const decision = confirm('Are you sure you want to delete ' + rowData.name + '? This action is irreversible! ')
      if (decision){
        //console.log(rowData)
        this.$axios.post('/delete_item/', rowData)
            .then((response) => {
              console.log('data received from server: '+JSON.stringify(response.data))
              alert(response.data.data)
              this.$router.go(0)
            })
      }
    },
    cellValueRenderer(row, column, cellValue) {
      let value = cellValue;
      if (typeof row[column.property] === 'boolean') {
        value = String(cellValue).toUpperCase();
        if(value === 'TRUE'){
          value='Available'
        }
        else {
          value='Not Available'
        }
      }
      return value;
    },
    handleDialogCancel(){
      this.showUpdateForm = false
      this.$router.go(0)
    },
    setTableHeaderStyle(){
      return "background: #d8e2f2; font-weight: bold;"
    }
  },
}
</script>

<style scoped>

</style>