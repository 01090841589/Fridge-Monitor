<template>
  <div>

  <v-overlay opacity="0.8">

  <vue-typer class="loading"
    :text='["Loading...", "Almost...", "Really...", "Close...", "Wait...", "Sorry...", "거의 다됨..."]'
    :repeat='Infinity'
    :shuffle='false'
    initial-action='typing'
    :pre-type-delay='70'
    :type-delay='100'
    :pre-erase-delay='2000'
    :erase-delay='250'
    erase-style='clear'
    :erase-on-complete='false'
  ></vue-typer>


  <br>
  <div class="spinner">
    <div class="cube1"></div>
    <div class="cube2"></div>
  </div>
  <div id="cancelBnt">
    <v-btn  @click="this.loadingCancel"> 취소 </v-btn>
  </div>
  <br>

  <!-- <div class="midalign">
    <v-progress-circular
        :size="200"
        :width="15"
        color="white"
        indeterminate
      ></v-progress-circular> -->
  <!-- </div> -->
  </v-overlay>
</div>
</template>

<script>
import {mapActions, mapState} from "vuex"
import { VueTyper } from 'vue-typer'
export default {
  
  components: {
    VueTyper,
  },
  data() {
    return {
    }
  },

  computed: {
    ...mapState(["isLoading"])
    },
  methods :{
    ...mapActions(["loading"]),
    loadingCancel(){
      this.loading()
      this.$router.go(-1)
    }
    },
 mounted() {

 }
}
</script>

<style lang="scss">
  #cancelBnt{
    color : white;
    text-align: center;
  }
  .loading{
    font-size: 3rem;

  }
  .vue-typer .char{
  color: white !important;
  }
  .midalign{
    display: block;
    text-align: center;
    color: white !important;
  }
  .spinner {
  margin: 100px auto;
  width: 40px;
  height: 40px;
  position: relative;
}

.cube1, .cube2 {
  background-color: white;
  width: 15px;
  height: 15px;
  position: absolute;
  top: 0;
  left: 0;
  
  -webkit-animation: sk-cubemove 1.8s infinite ease-in-out;
  animation: sk-cubemove 1.8s infinite ease-in-out;
}

.cube2 {
  -webkit-animation-delay: -0.9s;
  animation-delay: -0.9s;
}

@-webkit-keyframes sk-cubemove {
  25% { -webkit-transform: translateX(42px) rotate(-90deg) scale(0.5) }
  50% { -webkit-transform: translateX(42px) translateY(42px) rotate(-180deg) }
  75% { -webkit-transform: translateX(0px) translateY(42px) rotate(-270deg) scale(0.5) }
  100% { -webkit-transform: rotate(-360deg) }
}

@keyframes sk-cubemove {
  25% { 
    transform: translateX(42px) rotate(-90deg) scale(0.5);
    -webkit-transform: translateX(42px) rotate(-90deg) scale(0.5);
  } 50% { 
    transform: translateX(42px) translateY(42px) rotate(-179deg);
    -webkit-transform: translateX(42px) translateY(42px) rotate(-179deg);
  } 50.1% { 
    transform: translateX(42px) translateY(42px) rotate(-180deg);
    -webkit-transform: translateX(42px) translateY(42px) rotate(-180deg);
  } 75% { 
    transform: translateX(0px) translateY(42px) rotate(-270deg) scale(0.5);
    -webkit-transform: translateX(0px) translateY(42px) rotate(-270deg) scale(0.5);
  } 100% { 
    transform: rotate(-360deg);
    -webkit-transform: rotate(-360deg);
  }
}
</style>
