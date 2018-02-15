<template>
  <div id="creatComponent">
    <el-form ref="form" :model="form" label-width="80px">
      <el-form-item label="名称">
        <el-col :span="9">
        <el-input v-model="form.name"></el-input>
        </el-col>
      </el-form-item>
      <el-form-item label="全名">
        <el-col :span="9">
        <el-input v-model="form.fullName"></el-input>
        </el-col>
      </el-form-item>
      <el-form-item label="icon_small">
        <el-col :span="9">
          <el-input v-model="form.iconSmall"></el-input>
        </el-col>
      </el-form-item>
      <el-form-item label="icon_mid">
        <el-col :span="9">
          <el-input v-model="form.iconMid"></el-input>
        </el-col>
      </el-form-item>
      <el-form-item label="主页">
        <el-col :span="9">
          <el-input v-model="form.website"></el-input>
        </el-col>
      </el-form-item>
      <el-form-item label="白皮书">
        <el-col :span="9">
          <el-input v-model="form.whitepaper"></el-input>
        </el-col>
      </el-form-item>
      <el-form-item label="github地址">
        <el-col :span="9">
          <el-input v-model="form.gitAdderess"></el-input>
        </el-col>
      </el-form-item>
      <el-form-item label="描述">
        <el-col :span="16">
        <el-input type="textarea" v-model="form.desp"></el-input>
        </el-col>
      </el-form-item>
      <el-form-item>
        <el-col :span="16">
        <el-button type="primary" @click="onSubmit">立即创建</el-button>
        <el-button>取消</el-button>
        </el-col>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        form: {
          name: '',
          fullName: '',
          iconSmall: '',
          iconMid: '',
          website: '',
          whitepaper: '',
          gitAdderess: '',
          desp: ''
        }
      }
    },
    methods: {
      onSubmit() {
        this.$http.post('http://127.0.0.1:5000/api/project/add/', {
          'name':this.form.name,
          'fullname':this.form.fullName,
          'iconSmall':this.form.iconSmall,
          'iconMid':this.form.iconMid,
          'website':this.form.website,
          'whitepaper':this.form.whitepaper,
          'gitAddress':this.form.gitAdderess,
          'desp':this.form.desp,

        }).then(
         function(res) {
         // 这里是处理正确的回调
         this.$message({
          message: '添加成功',
          type: 'success'
        });
       }, function(res) {
           // 这里是处理错误的回调
           this.$message.error('添加失败');
       });
      }
    }
  }
</script>

<style>
</style>
