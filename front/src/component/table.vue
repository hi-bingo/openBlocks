<template>
 <div>
   <div style="margin-top: 25px;margin-right:100px;  text-align:right">
     <el-autocomplete class="inline-input" v-model="state" :fetch-suggestions="querySearch" placeholder="输入关键词..." :trigger-on-focus="false" @select="handleSelect"></el-autocomplete>
      <el-button type="primary" slot="append" icon="el-icon-search"></el-button>
    </el-input>
  </div>
  <el-table id='tablelist' :data="tableData"  style="width: 100%" :default-sort="{prop: 'lastCommit', order: 'descending'}"
    highlight-current-row
    @current-change="handleCurrentChange">
    <el-table-column prop="name" label="名称" width="100" header-align="center" fixed>
      <template slot-scope="scope">
       <img v-bind:src="scope.row.iconSmall" alt="coin">
       <font font-family="Arial" size="3px" ><b>{{ scope.row.name }}</b></font>
     </template>
    </el-table-column>
    <el-table-column prop="price" label="现价" sortable  width="100" header-align="center" fixed>
      <template slot-scope="scope">
       ￥{{ scope.row.price }}
     </template>
    </el-table-column>
    <el-table-column prop="mc" label="市值(亿)" sortable  width="100" header-align="center" fixed>
      <template slot-scope="scope">
       ￥{{ scope.row.mc }}亿
     </template>
    </el-table-column>
    <el-table-column prop="lastCommit" label="最近代码提交时间" width="150" sortable header-align="center" fixed>
    </el-table-column>
    <el-table-column prop="weekCommit" label="本周代码提交次数" sortable header-align="center" fixed>
    </el-table-column>
    <el-table-column prop="monthCommit" label="本月代码提交次数" sortable header-align="center" fixed>
    </el-table-column>
    <el-table-column prop="seasonCommit" label="季度代码提交次数" sortable header-align="center" fixed>
    </el-table-column>
    <el-table-column prop="star" label="Star" sortable width="120"  header-align="center" fixed>
    </el-table-column>
    <el-table-column prop="watch" label="Watch"  sortable header-align="center" fixed>
    </el-table-column>
    <el-table-column prop="fork" label="Fork" sortable header-align="center" fixed>
    </el-table-column>
    <el-table-column prop="issue" label="Issue" sortable header-align="center" fixed>
    </el-table-column>
    <el-table-column prop="contributors" label="Contributors" sortable header-align="center" fixed>
    </el-table-column>
    <el-table-column prop="releases" label="Release" sortable header-align="center" fixed>
    </el-table-column>
  </el-table>
    <el-pagination
      @current-change="handlePageChange"
      background
      layout="prev, pager, next"
      :page-count="total" >
    </el-pagination>
</div>
</template>

<script>
  export default {
    data() {
      return {
        tableData: [],
        total:10,
        state:''
      }
    },
    methods: {
      formatter(row, column) {
        return row.address;
      },
      handleCurrentChange(val) {
        this.$router.push('/coin/'+val.name)
     },
     querySearch(queryString, cb) {
        var querySuggest = this.querySuggest;
        var results = queryString ? querySuggest.filter(this.createFilter(queryString)) : querySuggest;
        // 调用 callback 返回建议列表的数据
        cb(results);
      },
      createFilter(queryString) {
        return (querySuggest) => {
          return (querySuggest.value.toLowerCase().indexOf(queryString.toLowerCase()) != -1);
        };
      },
     handleSelect(item) {
       this.$router.push('/coin/'+item.val)
      },

     handlePageChange(currentPage){
       this.$http.jsonp('http://127.0.0.1:5000/api/project/all/', {params:{'page':currentPage,'per_page':12}}).then(
        function(res) {
        // 这里是处理正确的回调
        var data=[];
        for (let i = 0; i < res.body['res'].length; i++) {
                var obj = {}
                obj.iconSmall = 'static/'+res.body['res'][i].iconSmall
                obj.name = res.body['res'][i].name
                obj.star = res.body['res'][i].star
                obj.fork = res.body['res'][i].forks
                obj.watch = res.body['res'][i].watch
                obj.contributors = res.body['res'][i].contributors
                obj.issue = res.body['res'][i].issue
                obj.releases = res.body['res'][i].releases
                obj.lastCommit = res.body['res'][i].lastCommit
                obj.weekCommit = res.body['res'][i].weekCommit
                obj.monthCommit = res.body['res'][i].monthCommit
                obj.seasonCommit = res.body['res'][i].seasonCommit
                obj.mc = res.body['res'][i].marketPriceCNY=='/'? '/ ':  parseFloat((res.body['res'][i].marketPriceCNY/100).toFixed(2))
                obj.price = res.body['res'][i].currentPriceCNY=='/'? '/ ': parseFloat(res.body['res'][i].currentPriceCNY.toFixed(2))
                data[i] = obj
              }
              this.tableData= data;
              this.total=res.body['pages'];
      }, function(res) {
          // 这里是处理错误的回调
            this.tableData= [{'name':'bch'}];
      });
     }
    },
    created: function() {
     this.$http.jsonp('http://127.0.0.1:5000/api/project/all/', {params:{'page':1,'per_page':12}}).then(
      function(res) {
      // 这里是处理正确的回调
        console.log(res);
      var data=[];
      for (let i = 0; i < res.body['res'].length; i++) {
              var obj = {}
              obj.iconSmall = 'static/'+res.body['res'][i].iconSmall
              obj.name = res.body['res'][i].name
              obj.star = res.body['res'][i].star
              obj.fork = res.body['res'][i].forks
              obj.watch = res.body['res'][i].watch
              obj.contributors = res.body['res'][i].contributors
              obj.issue = res.body['res'][i].issue
              obj.releases = res.body['res'][i].releases
              obj.lastCommit = res.body['res'][i].lastCommit
              obj.weekCommit = res.body['res'][i].weekCommit
              obj.monthCommit = res.body['res'][i].monthCommit
              obj.seasonCommit = res.body['res'][i].seasonCommit
              obj.mc = res.body['res'][i].marketPriceCNY=='/'? '/ ':  parseFloat((res.body['res'][i].marketPriceCNY/100).toFixed(2))
              obj.price = res.body['res'][i].currentPriceCNY=='/'? '/ ': parseFloat(res.body['res'][i].currentPriceCNY.toFixed(2))
              data[i] = obj
            }
      this.tableData= data;
      this.total=res.body['pages'];
      this.querySuggest=res.body['querySuggest'];
    }, function(res) {
        // 这里是处理错误的回调
        console.log(res);
          this.tableData= [{'name':'bch'}];
    });
  }

  }


</script>
