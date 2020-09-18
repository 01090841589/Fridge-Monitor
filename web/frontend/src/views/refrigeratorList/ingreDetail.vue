<template>
  <div>

  </div>
</template>

<script>
import http from "@/utils/http-require.js";
import jwtDecode from 'jwt-decode'
import store from "../../vuex/store"
export default {
    data (){
        return {
            base:[],
            dessert:[],
            editedItem: {
            name: '',
            expirationDate: 5,
            floor: 1,
            kind: '',
            note: '',
            },
        }
    },
    
    methods:{
        get_img_path(path, name){
            return require('../../../../backend/media/AI/crop_img/'+this.username + '/' + name + '.jpg')
        },
        initialize(){
            const dat = {}
            console.log("뭐야이게")
            console.log(this.$route.params)
            
            this.dessert.push(this.$route.params.res)

            console.log(this.dessert)

            dat['user_id'] = jwtDecode(store.state.token).user_id
            this.username = jwtDecode(store.state.token).username
            http.get(`/userapi/getingredients/${dat['user_id']}`)
            .then((res) => {
                console.log(res.data)
            })
        },
        gotoDetail(res) {
            this.$router.push({ name:'productAddInfo', params: {res}})
            },

    
    },
    mounted(){
        this.initialize()
    }
}
</script>

<style>

</style>