<template>
  <!-- 층별 사각형 -->
  <div>

      
    <div class="col-8" id="refriMain">
      <h3>나의 냉장고 </h3>
      <!-- "../../images/no_image.png" -->
      <draggable
        v-model="rows"

        class="row wrap fill-height align-center sortable-list"
        style="background: grey;"
      >
        <v-flex
          v-for="row in rows"
          :key="row.index"
          class="sortable"
          xs12
          my-1
          style="background: white; min-height: 80px;"
        >
        
          <v-chip color="gray" @click="$router.push('/floorDetail')">
            {{ row.index }}
          </v-chip>
          
          <draggable
            :list="row.items"
            :group="{ name: 'row' }"
            class="row wrap justify-space-around;"  
          >
          
            <v-flex
              v-for="item in row.items"
              :key="item.title"
              xs4
              pa-3
              class="row-v"
            >
              <div>

              <v-card id="gredientCard" @click="gotoDetail(item)" :color="getColor(item.expirationDate)">
                <div>
                </div>
              <img id="ingredImg" :src="get_img_path(item.img_path, item.name)" alt="asdf" style="opacity:0.5;">
              </v-card>
                {{ item.name }}
              </div>
            </v-flex>
          </draggable>
        </v-flex>
      </draggable>
    </div>
  </div>
</template>


<script>
// var fs = require('fs')?

import http from "@/utils/http-require.js";
// import Navbar from "@/components/NavBar";
import jwtDecode from 'jwt-decode'
import store from "../../vuex/store"
import draggable from 'vuedraggable'


export default {
  name: "functional",
  display: "Functional third party",
  order: 17,
  components: {
      draggable,
  },
  data: () => ({

      img_path : '',
      username : '',
      rows: [
        {
          index: '4층',
          items: [
          ]
        },
        {
          index: '3층',
          items: [
          ]
        },
        {
          index: '2층',
          items: [
          ]
        },
        {
          index: '1층',
          items: [
          ]
        },
        {
          index: '장바구니',
          items: [
          ]
        }
      ],
      oldRows: [
        {
          index: '4층',
          items: [
          ]
        },
        {
          index: '3층',
          items: [
          ]
        },
        {
          index: '2층',
          items: [
          ]
        },
        {
          index: '1층',
          items: [
          ]
        },
        {
          index: '장바구니',
          items: [
          ]
        }
      ],
    enabled: true,
    sheet: false,
    sheet1: false,
    sheet2: false,
    sheet3: false,
    sheet4: false,
    sheet5: false,
    sheet6: false,
    itemsPerPage: 4,
    desserts: [],
    floor1:[],
    floor2:[],
    floor3:[],
    floor4:[],
    basket:[],
    title: {
      width: "30px"
    }
  }),
  methods: {
    get_img_path(path, name){
        return require('../../../../backend/media/AI/crop_img/'+this.username + '/' + name + '.jpg')
    },
    gotoDetail(res) {

      this.$router.push({ name:'productAddInfo', params: {res}})
    },
    initialize () {
      const dat = {}
      dat['user_id'] = jwtDecode(store.state.token).user_id
      this.username = jwtDecode(store.state.token).username
      
      http.get(`/userapi/getingredients/${dat['user_id']}`)
        .then((res) => {
          console.log(res.data)
            for(var i = 0; i < res.data.length; i++){
              switch(res.data[i][5]){
                case 4:
                  this.rows[0].items.push({
                      'value': false,
                      'name': res.data[i][0].substring(0,10),
                      'id': res.data[i][7],
                      'floor': res.data[i][5],
                      'expirationDate': res.data[i][6],
                      'category': res.data[i][3],
                      'note': res.data[i][4],
                      'img_path': `../../../../backend/media/AI/crop_img/${this.username}/`
      // this.img_path = '../backend/media/AI/crop_img'+this.username+'감/자.jpg'
      // // console.log(
      // //   fs.exists('../../../../backend/media/AI/crop_img/chpre/감자.jpg')
      // // )
      // try {
      //   // fs.exists('../../../../backend/media/AI/crop_img/chpre/감자.jpg')
      //   // console.log(2)
      //   this.img_path = require("../../../../backend/media/AI/crop_img/no_image.jpg")

      // }
      // catch(err){
      //   console.log(err)
      // }
                  })
                  break;
                case 3:
                  this.rows[1].items.push({
                      'value': false,
                      'name': res.data[i][0].substring(0,10),
                      'id': res.data[i][7],
                      'floor': res.data[i][5],
                      'expirationDate': res.data[i][6],
                      'category': res.data[i][3],
                      'note': res.data[i][4],
                      'img_path': `../../../../backend/media/AI/crop_img/${this.username}/`
                  })
                  break;
                case 2:
                  this.rows[2].items.push({
                      'value': false,
                      'name': res.data[i][0].substring(0,10),
                      'id': res.data[i][7],
                      'floor': res.data[i][5],
                      'expirationDate': res.data[i][6],
                      'category': res.data[i][3],
                      'note': res.data[i][4],
                      'img_path': `../../../../backend/media/AI/crop_img/${this.username}/`
                  })
                  break;
                case 1:
                  this.rows[3].items.push({
                      'value': false,
                      'name': res.data[i][0].substring(0,10),
                      'id': res.data[i][7],
                      'floor': res.data[i][5],
                      'expirationDate': res.data[i][6],
                      'category': res.data[i][3],
                      'note': res.data[i][4],
                      'img_path': `../../../../backend/media/AI/crop_img/${this.username}/`
                  })
                  break;
                default:
                  this.rows[4].items.push({
                      'value': false,
                      'name': res.data[i][0],
                      'id': res.data[i][7],
                      'floor': res.data[i][5],
                      'expirationDate': res.data[i][6],
                      'category': res.data[i][3],
                      'note': res.data[i][4],
                      'img_path': `../../../../backend/media/AI/crop_img/${this.username}/`
                  })
                  break;
              }
            }
            
            for (var j = 0; j < 5 ; j++){
              for (var k = 0; k < this.rows[j].items.length ; k++){
                console.log(j, k)
                this.oldRows[j].items.push(this.rows[j].items[k])
              }
            }
          }
        )
        .catch((err)=>{
          console.log(err)
        })
        .finally(() =>
        this.isLoading = false)
    },
    getColor (expirationDate) {
      if (expirationDate < 3) return 'red'
      else if (expirationDate < 7) return 'orange'
      else return 'green'
    },

    goDetail4: function() {
      console.log("4층 페이지 이동");
    },
    goDetail3: function() {
      console.log("3층 페이지 이동");
    },
    goDetail2: function() {
      console.log("2층 페이지 이동");
    },
    goDetail1: function() {
      console.log("1층 페이지 이동");
    }
  },
  created () {
    this.initialize()
  },
  watch: {
    rows: {

      deep: true,
      handler(){
        for (var j = 0; j < 5; j++){
          if (this.rows[j].items.length > this.oldRows[j].items.length){
            if (this.rows[j].items.length === 1){
              http.put(`/userapi/updateingredients/${this.rows[j].items[0].id}/`, j)
                .then((res) => {
                  console.log(res)
                }
                )
                .catch((err)=>{
                  console.log(err)
                })
              break
            }

            for (var k = 0; k < this.rows[j].items.length; k++){
              var flag = 1
              for (var l = 0; l < this.oldRows[j].items.length; l++){
                if (this.rows[j].items[k].id === this.oldRows[j].items[l].id){
                  flag = 0
                  break
                }

              }
              if (flag){

                http.put(`/userapi/updateingredients/${this.rows[j].items[k].id}/`, j)
                .then((res) => {
                  console.log(res)
                }
                )
                .catch((err)=>{
                  console.log(err)
                })
              }
            }
            break
          }
        }
        this.oldRows = [
        {
          index: '4층',
          items: [
          ]
        },
        {
          index: '3층',
          items: [
          ]
        },
        {
          index: '2층',
          items: [
          ]
        },
        {
          index: '1층',
          items: [
          ]
        },
        {
          index: '장바구니',
          items: [
          ]
        }
      ]
      for (var n = 0; n < 5 ; n++){

        for (var m = 0; m < this.rows[n].items.length ; m++){
          this.oldRows[n].items.push(this.rows[n].items[m])
        }
      }
      }

    }
  }
};
</script>


<style scoped>
#refriMain{
  text-align: center;
  margin: auto;
}
#gredientCard{
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  text-align: center;
  height: 7vh; width:20vw;
  overflow: auto;
  font-size: 1vw;
  font-weight: 800;


}
.buttons {
  margin-top: 35px;
}
.row-v {
  height: 80px;
  width: 200px;
}
.ghost {
  opacity: 0.5;
  background: #c8ebfb;
}
#ingredImg{
  height: 100%;
}
</style>