<template>
  <div>
    <div class="head">Common Questions:</div>
    <el-collapse v-model="activeNames" @change="handleChange">
      <el-collapse-item class="header" title="How can I check if my sale received an offer?" name="1">
        <div class="body">After logging in, you can check your buying offer at "Profile", in the left tool bar click "My Offers", then click "Your Selling Offers" to see and manage the status of your sale.</div>
        <div class="body">You can select which offer to accept by clicking on the green checkmark if there are multiple offers</div>
      </el-collapse-item>
      <el-collapse-item class="header" title="How can I check if my sale received an offer?" name="2">
        <div class="body">After logging in, you can check your buying offer at "Profile", in the left tool bar click "My Offers", then click "Your Buying Offers" to see and manage the status of your sale.</div>
        <div class="body">You can change the information of your offer in "Your Buying Offer" by clicking "Manage Offer."</div>
      </el-collapse-item>
      <el-collapse-item class="header" title="Can I make multiple offers to the same sale?" name="3">
        <div class="body">Unfortunately, to prevent confusion for the seller, you are not able to make multiple offers to the same sale. However, you are able to make changes to your offer by going to "My Offer," clicking "Your Buying Offer" and "manage offer."</div>
      </el-collapse-item>
      <el-collapse-item class="header" title="How do I make payment/exchange goods?" name="4">
        <div class="body">For security reasons, we do not support online transactions. Once an offer is confirmed, you are encouraged to exchange goods and make transactions on campus or anywhere that is safe. </div>
      </el-collapse-item>
    </el-collapse>
  </div>

</template>

<script>
export default {
  data() {
    return {
      activeNames: ['1']
    };
  },
  methods: {
    handleChange(val) {
      console.log(val);
    }
  }
}
</script>

<style scoped>
.head {
  font-size: 30px;
  font-family: "Hannotate SC", serif;
  margin-left: 100px;
  margin-top: 15px;
  max-width: 80%;
  text-align:center;
}
.body {
  font-size: 15px;
  font-family: "Hannotate SC", serif;
  margin-left: 100px;
  margin-top: 15px;
  max-width: 80%;
  text-align: left;
}
</style>