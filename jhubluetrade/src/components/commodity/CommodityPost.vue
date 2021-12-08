<template>
  <div class="bg" style="overflow: auto">
    <el-container class="container">
      <el-main>
        <el-scrollbar>
        <el-page-header title="back" @back="goBack" content="Post Your Commodity~" style="margin: 20px 0 0 5px"></el-page-header>
        <el-divider></el-divider>
        <el-row type="flex" justify="center">
          <el-form :model="commodityForm" :rules="rules" ref="commodityForm" label-width="120px" class="post-container">
            <el-form-item label="Name" prop="name">
              <el-input v-model="commodityForm.name" class="el-input"></el-input>
            </el-form-item>
            <el-form-item label="Category" prop="category">
              <el-cascader
                  placeholder="please select category"
                  v-model="commodityForm.category"
                  :options="categories"
                  @change="handleCategoryChange"
                  style="width: 100%"></el-cascader>
            </el-form-item>
            <el-form-item label="Price" prop="price">
              <el-input v-model="commodityForm.price" class="el-input"
                        placeholder="if you want to sell for free, just enter 0! :)"></el-input>
            </el-form-item>
            <el-form-item label="Picture" prop="picture">
              <el-button class="card-block" @click="uploadImages">
                <i class="el-icon-plus avatar-uploader-icon"></i>
              </el-button>
            </el-form-item>
            <el-form-item label="Description" prop="description">
              <el-input type="textarea" :rows="4" v-model="commodityForm.description" class="el-input"></el-input>
            </el-form-item>
            <el-form-item>
              <el-button type="primary" @click="onSubmit" style="margin-left: -90px">post!</el-button>
            </el-form-item>
          </el-form>
        </el-row>
        </el-scrollbar>
      </el-main>
    </el-container>
  </div>
</template>

<script>
// import qs from 'qs'
export default {
  name: "CommodityPost",
  data() {
    const validatePrice = (rule, value, callback) => {
      if (value.search("\\d+\\.{0,1}\\d*$") === -1) {
        callback("this is not a valid price!");
      } else {
        callback();
      }
    };
    return {
      dialogImageUrl: '',
      dialogVisible: false,
      fileList: [],
      commodityForm: {
        name: '',
        description: '',
        price: '',
        category: ''
      },
      iconShow: 0,
      categories: [
        {value: 'computers', label: 'computers', children: [
            {value: 'video games', label: 'video games'},
            {value: 'hardware', label: 'hardware'},]},
        {value: 'electronics', label: 'electronics'},
        {value: 'home & kitchen', label: 'home & kitchen'},
        {value: 'office products', label: 'office products'},
        {value: 'books', label: 'books'},
        {value: 'personal cares', label: 'personal cares'},
        {value: 'vehicles', label: 'vehicles'},
      ],
      rules: {
        name: {required: true},
        category: {required: true},
        price: [
          { validator: validatePrice, trigger: 'blur', required: true }
        ],
      }
    }
  },
  created() {
    if (this.$store.state.email === null || this.$store.state.email.length === 0) {
      this.$router.push("/login")
    }
  },
  methods: {
    goBack() {
      this.$router.push('/commodity_list')
    },
    handleCategoryChange(value) {
      this.commodityForm.category = value;
      console.log(value);
    },
    handleExceed() {
      this.$message.warning("limit 5 photos!");
    },
    uploadImages () {
      const options = {
        maxFiles: 5,
        onFileSelected: file => {
          if (file.size > 2000 * 2000) {
            throw new Error('File too big, select something smaller than 4MB');
          }
        },
        onUploadDone: resp => {
          for (var i = 0, len = resp.filesUploaded.length; i < len; i++) {
            this.fileList.push(resp.filesUploaded[i].url)
          }
          this.$message({
            type: "success",
            message: "success uploaded images!!"
          })
        }
      }
      this.$client.picker(options).open();
    },
    onSubmit() {
      // console.log(this.$store.state.email)
      if (this.$store.state.email === '') {
        this.$message({
          type: "error",
          message: "You cannot post without login :("
        })
      } else {
        let category = this.commodityForm.category[0];
        let subcategory = this.commodityForm.category.length === 2 ? this.commodityForm.category[1] : "";
        this.$axios({
          method: 'post',
          url: '/post/',
          data: {
            owner: this.$store.state.email,
            name: this.commodityForm.name,
            description: this.commodityForm.description,
            price: this.commodityForm.price,
            category: category,
            subcategory: subcategory,
            photos: this.fileList
          },
          headers: {
            'Content-Type': 'application/json',
          }
        }).then(resp => {
          if (resp.data.code === 200) {
            this.$alert('Great! You have post successfully! :)', 'Congratulation!', {
              confirmButtonText: 'confirm',
            });
            this.$router.push('/commodity_list');
          } else {
            this.$message({
              type: 'error',
              message: 'Sorry, we are sorry to inform you that your post failed for some reasons. :('
            });
          }
        }).catch(exception => {
          console.log(exception);
        });
      }
    }
  }
}
</script>

<style scoped>
@import "../../styles/scroll.css";
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
