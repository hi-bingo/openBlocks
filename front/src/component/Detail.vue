<template>
  <div id="detailComponent">
    <el-container>
      <el-header></el-header>
      <el-container>
        <el-aside width="32%" >
          <el-row >
            <el-col :offset="6" :span="18">
          <h1 >
            <img v-bind:src=coinDetail.iconMid style="vertical-align:-9px">
            {{coinDetail.fullName}}
          </h1>
        </el-col>
      </el-row>
          <el-row >
            <el-col :offset="10" :span="14">
              <el-table :data="priceInfo" :show-header="false" style="width: 60%" >
                    <el-table-column prop="key"  align="center">
                    </el-table-column>
                    <el-table-column prop="value"  align="center">
                    </el-table-column>
                  </el-table>
            </el-col>
          </el-row>


        </el-aside>
        <el-main>
          <el-row id='baseRow'  ></el-row>

          <el-row  id='baseRow'  >
            <el-col :span="2" :offset="1">
              <b >GitHub地址:</b>
            </el-col>
            <el-col id='baseCell' :offset="1" :span="17">
              <a target="_blank" v-bind:href=coinDetail.gitAddress >{{coinDetail.gitAddress}}</a>
            </el-col>
          </el-row>
          <el-row  id='baseRow'  >
            <el-col  :span="2" :offset="1" >
              <b >官网地址:</b>
            </el-col>
            <el-col id='baseCell' :offset="1" :span="17">
              <a target="_blank" v-bind:href=coinDetail.website >{{coinDetail.website}}</a>
            </el-col>
          </el-row>
          <el-row  id='baseRow'>
            <el-col :span="2" :offset="1">
              <b >白皮书:</b>
            </el-col>
            <el-col id='baseCell' :offset="1" :span="17">
              <a target="_blank" v-bind:href=coinDetail.whitepaper >{{coinDetail.whitepaper}}</a>
            </el-col>
          </el-row>
          <el-row  id='baseRow'>
            <el-col :span="18" :offset="1" >
              <p  id='desp'>{{coinDetail.desp}}</p>
            </el-col>
          </el-row>
          <el-row  id='baseRow'></el-row>
          <el-row  id='baseRow'></el-row>
          <el-row>
            <el-col :span="21" :offset="1">
          <div class="charts">
            <div id="commitStats" :style="{width:'800px',height:'300px'}"></div>
          </div>
        </el-col>
        </el-row>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>




<script>
import echarts from 'echarts'

  export default {
    data() {
      return {
        coinDetail: {},
        priceInfo:[]
      }
    },
    methods: {

    },
    created: function() {
     var coin=this.$route.path.split('/')[2]
     this.$http.jsonp('http://127.0.0.1:5000/api/project/'+coin, {}).then(
      function(res) {
      // 这里是处理正确的回调
       var commitStats=echarts.init(document.getElementById("commitStats"))
        console.log(res);
        var obj = {}
        obj.iconMid = '/static/'+res.body.iconMid
        obj.name = res.body.name
        obj.fullName = res.body.fullName
        obj.website=res.body.website
        obj.whitepaper=res.body.whitepaper
        obj.desp=res.body.desp
        obj.gitAddress=res.body.gitAddress
        obj.desp=res.body.desp
        obj.currentPriceCNY=res.body.currentPriceCNY
        obj.currentPriceUSD=res.body.currentPriceUSD
        obj.marketPriceCNY=res.body.marketPriceCNY
        obj.marketPriceUSD=res.body.marketPriceUSD
        obj.amount = res.body.amount
        obj.supply = res.body.supply
        obj.star = res.body.star
        obj.forks = res.body.forks
        obj.contributors = res.body.contributors
        obj.issue = res.body.openIssue
        obj.releases = res.body.releases
        obj.lastCommit = res.body.lastCommit
        obj.weekCommit = res.body.weekCommit
        obj.monthCommit = res.body.monthCommit
        obj.seasonCommit = res.body.seasonCommit
        obj.commitStats=JSON.parse(res.body.commitStats)
        this.coinDetail= obj;
        this.priceInfo=[{
          key:"现价（￥）:",
          value:'￥'+this.coinDetail.currentPriceCNY
        },{
          key:"流通市值（￥）:",
          value:'￥'+(this.coinDetail.marketPriceCNY/100).toFixed(3)+' 亿'
        },{
          key:"流通量:",
          value:this.coinDetail.supply
        },{
          key:"总量:",
          value:this.coinDetail.amount
        },{
          key:"Star:",
          value:this.coinDetail.star
        },{
          key:"Fork:",
          value:this.coinDetail.forks
        },{
          key:"Releases:",
          value:this.coinDetail.releases
        },{
          key:"Contributors:",
          value:this.coinDetail.contributors
        }]

        var xData=[]
        var yData=[]
        for (let i = 0; i < obj.commitStats.length; i++) {
            xData.push(obj.commitStats[i][0])
            yData.push(obj.commitStats[i][1])
        }
        var options = {
          title: {
              text: '最近一年commit周统计',
               left: 'center',
          },
          color: ['#3398DB'],
          tooltip : {
              trigger: 'axis',
              axisPointer : {            // 坐标轴指示器，坐标轴触发有效
                  type : 'shadow'        // 默认为直线，可选为：'line' | 'shadow'
              }
          },
          grid: {
              left: '3%',
              right: '4%',
              bottom: '3%',
              containLabel: true
          },
          xAxis : [
              {
                  type : 'category',
                  data : xData,
                  axisTick: {
                      alignWithLabel: true
                  }
              }
          ],
          yAxis : [
              {
                  type : 'value'
              }
          ],
          series : [
              {
                  name:'commit数量',
                  type:'bar',
                  barWidth: '60%',
                  data:yData
              }
          ]
      };
      commitStats.setOption(options)

    }, function(res) {
        // 这里是处理错误的回调
        console.log(res);
          this.coinDetail= null;
    });
  },


  }
</script>


<style>
#baseRow {
  height:50px;
}

#baseCell{
  text-align: left;
}

#desp{
  text-indent:50px;
  text-align:left
}
</style>
