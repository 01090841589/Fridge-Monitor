<template>
<div id="front" class="w3-center" style="margin-bottom:40px">
  <v-data-table
    :headers="headers"
    :items="desserts"
    class="elevation-1"
  >
    <template v-slot:top>
      <v-toolbar flat color="white">
        <v-toolbar-title>신규 식재료 리스트</v-toolbar-title>
        <v-divider
          class="mx-4"
          inset
          vertical
        ></v-divider>
        <v-spacer></v-spacer>
        <v-dialog v-model="dialog" max-width="500px">
          <template v-slot:activator="{ on }">
            <v-btn color="primary" dark class="mb-2" v-on="on" >재료 추가하기</v-btn>
          </template>
          <v-card>
            <v-card-title>
              <span class="headline">{{ formTitle }}</span>
            </v-card-title>

            <v-card-text>
              <v-container>
                <v-row>
                  <v-col cols="12" sm="6" md="3">
                    <v-text-field v-model="editedItem.name" label="품명"></v-text-field>
                  </v-col>
                  <v-col cols="12" sm="6" md="3">
                    <v-text-field v-model="editedItem.expirationDate" label="유통 기한"></v-text-field>
                  </v-col>
                  <v-col cols="12" sm="6" md="3">
                    <v-text-field v-model="editedItem.floor" label="위치(층)">층</v-text-field>
                  </v-col>
                  <v-col cols="12" sm="6" md="3">
                    <v-text-field v-model="editedItem.kind" label="분류"></v-text-field>
                  </v-col>
                  <v-col cols="12" sm="6" md="3">
                    <v-text-field v-model="editedItem.note" label="비고"></v-text-field>
                  </v-col>
                </v-row>
              </v-container>
            </v-card-text>

            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="blue darken-1" text @click="close">취소</v-btn>
              <v-btn color="blue darken-1" text @click="save">저장</v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
      </v-toolbar>
    </template>
    <template v-slot:item.actions="{ item }">
      <v-icon
        small
        class="mr-2"
        @click="editItem(item)"
      >
        mdi-pencil
      </v-icon>
      <v-icon
        small
        @click="deleteItem(item)"
      >
        mdi-delete
      </v-icon>
    </template>
    <template v-slot:item.expirationDate="{ item }">
      <v-chip :color="getColor(item.expirationDate)" dark>{{ item.expirationDate }}</v-chip>
    </template>
  </v-data-table>
  <v-btn class="listAdd_button" style="margin-bottom:60px" @click="uploaddata()">등록 완료</v-btn>
</div>
</template>

<script>

import http from "@/utils/http-require.js";
import jwtDecode from 'jwt-decode'
import store from "../../vuex/store"
  export default {
    components: { },
    data: () => ({
      user_id: -1,
      dialog: false,
      headers: [
        {
          text: '품명',
          align: 'start',
          sortable: false,
          value: 'name',
        },
        { text: '유통 기한', value: 'expirationDate' },
        { text: '분류', value: 'kind' },
        { text: '비고', value: 'note', sortable: false },
        { text: '수정', value: 'actions', sortable: false },
      ],
      desserts: [],
      editedIndex: -1,
      editedItem: {
        name: '',
        expirationDate: 5,
        floor: 1,
        kind: '',
        note: '',
      },
      defaultItem: {
        name: '',
        expirationDate: 0,
        floor: 1,
        kind: '',
        note: '',
      },
    }),

    computed: {
      formTitle () {
        return this.editedIndex === -1 ? '리스트 추가' : '리스트 수정'
      },
    },

    watch: {
      dialog (val) {
        val || this.close()
      },
    },

    created () {
      this.initialize()
    },

    methods: {
      uploaddata() {

          for(var i = 0; i < this.desserts.length; i++){
            this.desserts[i]['user_id'] = this.user_id;
          }

          
          if (this.$route.params.res === undefined){

            http.post(`/userapi/addingredients/`, this.desserts)
            .then((res) => {
              console.log(res)
              alert("등록이 완료되었습니다.");
              this.$router.push("/list")
            }
            )
            .catch((err)=>{
              console.log(err)
              alert("등록에 실패하였습니다.");
            })
            .finally(() =>
            this.isLoading = false)
          }
          else {
            http.put(`/userapi/updateingredients/${this.$route.params.res.id}/ `, this.$route.params.res)
            .then((res) => {
              console.log(res)
              alert("등록이 완료되었습니다.");
              this.$router.push("/list")
            }
            )
            .catch((err)=>{
              console.log(err)
              alert("등록에 실패하였습니다.");
            })
            .finally(() =>
            this.isLoading = false)
          }

      },
      initialize () {
        this.user_id = jwtDecode(store.state.token).user_id
        console.log(this.$route.params)
        if (this.$route.params.datas !== undefined){
          for(var i = 0; i < this.$route.params.datas.length; i++){
            this.desserts.push(this.$route.params.datas[i])
            this.desserts[i]['floor'] = -1
            this.desserts[i]['kind'] = '없음'
          }
        }
        if (this.$route.params.res){
          
            this.desserts.push(this.$route.params.res)
            this.desserts[0]['floor'] = this.$route.params.res.floor
            this.desserts[0]['kind'] = this.$route.params.res.category
        }
      },

      editItem (item) {
        this.editedIndex = this.desserts.indexOf(item)
        this.editedItem = Object.assign({}, item)
        this.dialog = true
      },

      deleteItem (item) {
        const index = this.desserts.indexOf(item)
        confirm('리스트에서 제거 하시겠습니까?') && this.desserts.splice(index, 1)
      },

      close () {
        this.dialog = false
        this.$nextTick(() => {
          this.editedItem = Object.assign({}, this.defaultItem)
          this.editedIndex = -1
        })
      },

      save () {
        if (this.editedIndex > -1) {
          Object.assign(this.desserts[this.editedIndex], this.editedItem)
        } else {
          this.desserts.push(this.editedItem)
        }
        this.close()
      },
      getColor (expirationDate) {
        if (expirationDate < 3) return 'red'
        else if (expirationDate < 7) return 'orange'
        else return 'green'
      },
    },
  }
</script>

<style>
.listAdd_button{
    font-size: 16px;
    border-radius: 5px;
    padding: 10px 15px;
    margin: 15px;
}
</style>