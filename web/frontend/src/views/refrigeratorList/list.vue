
<template>
  <div id="reFront" class="w3-center">
    <h1 style="background-color:white">냉장고 리스트</h1>
    <v-btn id="gotoMain" color="info"  @click="$router.push('/main')"> 층별로 보기</v-btn>
    <v-data-table 
      :headers="headers" 
      :items="desserts" 
      hide-default-footer 
      class="elevation-1" 
    >
      <template v-slot:item.name="{ item }">
        <v-chip @click="gotoDetail(item)"  dark>{{ item.name }}</v-chip>
      </template>
    
      <template v-slot:item.expirationDate="{ item }">
        <v-chip :color="getColor(item.expirationDate)" dark>{{ item.expirationDate }}</v-chip>
      </template>

      <template v-slot:item.floor="{ item }">
        <v-chip v-if="item.floor > -1">{{item.floor}}</v-chip>
        <v-chip v-else>장바구니</v-chip>

      </template>
      
      <template v-slot:item.actions="{ item }">
      <!-- <v-icon
        small
        class="mr-2"
        @click="editItem(item)"
      >
        mdi-pencil
      </v-icon> -->
      <v-icon
        small
        @click="deleteItem(item)"
      >
        mdi-delete
      </v-icon>
        <!-- <td>{{ props.item.name }}</td>
        <td class="text-xs-right" >{{ props.item.num }}</td>
        <td class="text-xs-right">{{ props.item.expirationDate }}</td>
        <td class="text-xs-right">{{ props.item.category }}</td>
        <td class="text-xs-right">{{ props.item.note }}</td>
        <td class="text-xs-right">{{ props.item.iron }}</td> -->

      </template>
    </v-data-table>
    
  </div>
</template>

<script>
import http from "@/utils/http-require.js";
// import axios from 'axios'
import jwtDecode from 'jwt-decode'
import store from "../../vuex/store"
export default {
  name: "list",
  components: { },
  data() {
    return {
      user_id : -1,
      headers: [
        {
          text: "식품명",
          align: "center",
          sortable: false,
          value: "name"
        },
        { text: "남은기한", value: "expirationDate" },
        { text: "위치(층)", value: "floor" },
        { text: "분류", value: "category" },
        { text: "비고", value: "note" },
        { text: '삭제', value: 'actions', sortable: false },
      ],
      desserts: [
      ]
    };
  },
  methods:{
    gotoDetail(res) {
      this.$router.push({ name:'ingreDetail', params: {res}})
    },
    
    editItem (item) {
      this.editedIndex = this.desserts.indexOf(item)
      this.editedItem = Object.assign({}, item)
      this.dialog = true
    },

    deleteItem (item) {
      const index = this.desserts.indexOf(item)
      var r = confirm('리스트에서 제거 하시겠습니까?')
      if (r == true){
        this.desserts.splice(index, 1)
        console.log(item.id)
        http.delete(`/userapi/updateingredients/${item.id}/ `)
          .then((res) => {
            console.log(res)
            this.$router.push("/list")
          }
          )
          .catch((err)=>{
            console.log(err)
          })
          .finally(() =>
          this.isLoading = false)
        }

    },

      
    initialize () {
      const dat = {}
      dat['user_id'] = jwtDecode(store.state.token).user_id
      http.get(`/userapi/getingredients/${dat['user_id']}`, dat)
          .then((res) => {
            console.log(res.data)
              for(var i = 0; i < res.data.length; i++){
                this.desserts.push({
                    'value': false,
                    'name': res.data[i][0],
                    'num': -1,
                    'floor': res.data[i][5],
                    'expirationDate': res.data[i][6],
                    'category': res.data[i][3],
                    'note': res.data[i][4],
                    'id': res.data[i][7]
                })
              }
            }
          )
          .catch((err)=>{
            console.log(err)
            alert("등록에 실패하였습니다.");
          })
          .finally(() =>
          this.isLoading = false)
    },
    getColor (expirationDate) {
      if (expirationDate < 3) return 'red'
      else if (expirationDate < 7) return 'orange'
      else return 'green'
    },
  },
  created () {
    this.initialize()
  },
};
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Black+And+White+Picture&display=swap');
  #gotoMain{
    font-family: 'Black And White Picture', sans-serif;
    font-size: 2vw;
    text-align: center;
    display: flex;
    margin: 15px;
    /* background: skyblue;
    color: rgb(255, 255, 255);
    font-size: 3vh;
    border-radius: 5px;
    padding: 3px;
    border: 1px solid black;
    font-weight: 700; */
  }
  #gotoMain:hover{
    /* background: firebrick; */
  }
</style>