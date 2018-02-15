<template>

  <div id="full">
    <div id="app">
      <router-view class="view"></router-view>
    </div>
    <div id="footer" >
      ETH & ERC20 Token 打赏地址:
      <el-button type="text" size="medium" @click="dialogVisible = true" >0x512524f4d31f9cB0d0d39d3a3A04d7320eD0965f </el-button>
    </div>
    <el-dialog
    title="Donate Address"
    :visible.sync="dialogVisible"
    width="30%"
    center>
      <div id="textCenter">
        <font face="PingFang SC" size="4px" ><b>0x512524f4d31f9cB0d0d39d3a3A04d7320eD0965f</b></font>
        <img src=" http://oxfq582iz.bkt.clouddn.com/ETH.png" >
      </div>
    </el-dialog>
  </div>
</template>

<script>
export default {
  data() {
    return {
      dialogVisible: false
    };
  },
  methods: {
  }
};
</script>

<style>
#app {
  font-family: Helvetica, sans-serif;
  text-align: center;
  padding-bottom:30px;
  overflow:hidden;
}

#full {
  min-height:100%;
}

#footer {
  margin-top:20px;
  height:30px;
  text-align: right;
  margin-right: 88px;

}

#textCenter {
  text-align: center;
}
</style>
