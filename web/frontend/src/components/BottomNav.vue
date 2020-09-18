<template>
  <div>
    <div style="height: 30px"></div>
    <br>
    <v-bottom-navigation
      grow
      color="teal"
      style="position:fixed; bottom:0;"
    >
      <v-btn @click="gotoList('/list')" >
        <span>MY</span>
        <v-icon>mdi-account</v-icon>
      </v-btn>
  
      <v-btn @click="gotoList('/productAdd')">
        <span>Add</span>
        <v-icon>mdi-label</v-icon>
      </v-btn>
  
      <v-btn>
        <span @click="logout()">Log out</span>
        <v-icon>mdi-logout</v-icon>
      </v-btn>
    </v-bottom-navigation>
  </div>
</template>

<script>
import { mapActions } from 'vuex'
// import {mapActions} from "vuex"
export default {
// ...mapActions(["logout"]),
  name: "BottomNav",
  data: () => ({
    isLogin: true,
  }),
  methods:{

    gotoList(pth){
      if (this.$route.path != pth){

        this.$router.push(pth)
      }

    },
    ...mapActions(["logout"])
    },
  };
</script>

<style>

</style>
