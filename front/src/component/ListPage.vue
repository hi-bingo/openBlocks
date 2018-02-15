<template>

  <div id="listPage">
    <el-row>
      <el-col :span="24">
        <font face="PingFang SC" size="6" >开源区块链项目统计</font>
      </el-col>
    </el-row>

    <el-row>
      <el-col :span="22" :offset=1>
          <tablelist ></tablelist>
      </el-col>
    </el-row>
  </div>
</template>


<script>
import tablelist from '../component/table.vue'

export default {
  name: 'listPage',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App'
    }
  },
  components: {
    tablelist
  }
}
</script>

<style>
</style>
