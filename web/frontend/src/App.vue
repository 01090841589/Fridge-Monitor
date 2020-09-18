<template>

  <v-app id="inspire" class="viewport">
    <Loading v-if="isLoading"></Loading>
    <v-content>
      <transition name="fade">
        <router-view :key="$route.fullPath"></router-view>
      </transition>
      <div>
      </div>
      <BottomNav v-if="isLogin" class="bottom-nav" />
    </v-content>
  </v-app>

</template>

<script>
import BottomNav from "./components/BottomNav";
import Loading from "@/components/LoadingPage.vue";
import {mapState, mapActions} from "vuex"
export default {
  name: "App",
  props: {
    source: String,
  },

  components: {
    BottomNav,
    Loading
  },

  computed:{
    ...mapState(["isLogin","isLoading"])
  },
  methods:{
    ...mapActions(["loading"])
  },
  created(){
    console.log("hit")
    console.log(this.isLoading)
    if(this.isLoading){
      this.loading()
   }
  }

};

</script>

<style lang="scss" scoped>

@import url("https://fonts.googleapis.com/css?family=Black+Han+Sans|Do+Hyeon|Jua|Nanum+Gothic|Sunflower:300");
#effect {
  font-family: "Do Hyeon", sans-serif;
}


</style>
