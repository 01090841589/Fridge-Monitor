<template>
<div>
  <div id="loadingTyper">
  <VueTyper
    :text='["로딩 중입니다.","제가 지금 가고 있습니다... ","거의 다됐어요 진짜 거의 다됨...", "간다. 된다. 된다! 된다!!! 쨘!!!!!!", "기대가 된단 말이었어요","이제 조금 남았다","3, 2, 1...","쨘!!!!","Really...", "자 다같이...", "하나...", "둘...", "셋!!"]'
    :repeat='Infinity'
    :shuffle='false'
    initial-action='typing'
    :pre-type-delay='70'
    :type-delay='120'
    :pre-erase-delay='1500'
    :erase-delay='250'
    erase-style='clear'
    :erase-on-complete='false'> </VueTyper>
  </div>
  <div class="loadingBody">
      <div class='road'></div>
      <div class='wrap'>
      <div class='cube'>
          <div class='face'>
          <div class='topdoor'></div>
          <div class='bottomdoor'>
              <div class='smile'></div>
          </div>
          </div>
          <div class='face'></div>
          <div class='face'></div>
          <div class='face'></div>
          <div class='face'></div>
          <div class='face'></div>
      </div>
      <div class='plug'></div>
      <div class='legs'>
          <div class='lower'></div>
      </div>
      <div class='legs left'>
          <div class='lower'></div>
      </div>
  </div>
  <div id="cancelBnt">
    <v-btn  @click="this.loadingCancel"> 취소 </v-btn>
  </div>
</div>
</div>

</template>

<script>
import {mapActions, mapState} from "vuex"

import { VueTyper } from 'vue-typer'
export default {
  components: {
  VueTyper,
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

  

}
</script>

<style>
#loadingTyper{
  z-index: 3;
  top: 30%;
  font-size: 2rem;
  position:absolute; left:50%; transform:translateX(-50%);
  background-color: rgba(255, 248, 238, 0.5);
}
#cancelBnt{
  position:absolute; top:80%; left:50%; transform:translateX(-50%);
}
.loadingBody {
  position: absolute;
  z-index: 1;
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  overflow: hidden;
  background: linear-gradient(to top, rgba(255, 255, 255, 0.2), rgb(182, 246, 255));
}
.loadingBody .road {
  position: absolute;
  width: 100%;
  height: 40vh;
  bottom: 0;
  background: linear-gradient(to bottom, rgba(55, 189, 2, 0.2), rgba(91, 255, 41,0.5) 30%);
  overflow: hidden;
  transform-style: preserve-3d;
  box-shadow: inset 0 3px 0 0 #222;
  min-width: 1000px;
}
.loadingBody .road:before {
  content: '';
  position: absolute;
  width: 200%;
  left: -50%;
  height: 200px;
  top: 100px;
  background: repeating-linear-gradient(-35deg, transparent, transparent 200px, #090909 200px, #090909 202px, transparent 202px), rgba(187,187,187,0.5);
  background-size: 700px 100%;
  transform: skewY(2.5deg) rotateX(-50deg);
  animation: sidewalk 4s linear infinite;
  box-shadow: inset 0 0 0 3px #222;
}
@keyframes sidewalk {
  0% {
    background-position: 0% 50%;
  }
  100% {
    background-position: -200% 50%;
  }
}
.loadingBody .wrap {
  width: 100px;
  height: 400px;
  perspective: 10000px;
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translateX(-50%) translateY(-50%);
}
.loadingBody .wrap .legs {
  width: 7px;
  height: 75px;
  background: #222;
  position: absolute;
  z-index: 3;
  bottom: -10px;
  left: 0;
  border-radius: 10px;
  transform-origin: 50% 0%;
  animation: run1 0.35s ease-in-out infinite alternate;
}
.loadingBody .wrap .legs.left {
  left: 50px;
  z-index: -1;
  animation-delay: -0.175s;
}
.loadingBody .wrap .legs.left .lower {
  animation-delay: -0.175s;
}
.loadingBody .wrap .legs.left .lower:before {
  animation-delay: -0.175s;
}
@keyframes run1 {
  0% {
    transform: rotate(-50deg);
  }
  100% {
    transform: rotate(70deg);
  }
}
.loadingBody .wrap .legs .lower {
  position: absolute;
  bottom: -67.5px;
  height: 70px;
  width: 7px;
  background: #222;
  border-radius: 10px;
  transform-origin: 75% 0%;
  animation: run2 0.35s ease-in-out infinite alternate;
}
@keyframes run2 {
  0% {
    transform: rotate(10deg);
  }
  100% {
    transform: rotate(90deg);
  }
}
.loadingBody .wrap .legs .lower:after {
  content: '';
  position: absolute;
  width: 35px;
  height: 10px;
  background: #222;
  left: -1.5px;
  bottom: 0;
  border-radius: 10px;
  transform-origin: 10% 50%;
  animation: run3 0.35s ease-in-out infinite alternate;
}
@keyframes run3 {
  0% {
    transform: rotate(10deg);
  }
  100% {
    transform: rotate(50deg);
  }
}
.loadingBody .wrap .plug {
  content: '';
  position: absolute;
  width: 15px;
  height: 20px;
  background: #222;
  z-index: 9;
  border-radius: 0 20px 20px 0;
  left: -195px;
  bottom: 52.5px;
  animation: plug 0.25s linear infinite alternate;
}
.loadingBody .wrap .plug:before, .loadingBody .wrap .plug:after {
  content: '';
  position: absolute;
  top: 2px;
  width: 5px;
  height: 3px;
  background: #bbb;
  border: 2px solid #222;
  left: -7px;
}
.loadingBody .wrap .plug:after {
  top: 10px;
}
@keyframes plug {
  0% {
    transform: translateY(0px);
  }
  100% {
    transform: translateY(-25px);
  }
}
.loadingBody .wrap:after {
  top: 225px;
  left: -100px;
  transform: rotate(-90deg);
  z-index: -1;
  content: '';
  position: absolute;
  width: 35px;
  height: 200px;
  background: radial-gradient(circle at 100% 50%, transparent 20%, #222 21%, #222 34%, transparent 35%, transparent), radial-gradient(circle at 0% 50%, transparent 20%, #222 21%, #222 34%, transparent 35%, transparent) 0px -25px;
  background-size: 37.5px 50px;
  background-position: -20px -25px, -20px -50px;
  animation: cord 2s linear infinite;
}
@keyframes cord {
  0% {
    background-position: -20px -25px, -20px -50px;
  }
  100% {
    background-position: -20px -225px, -20px -250px;
  }
}
.loadingBody .wrap .cube {
  width: 100%;
  height: 100%;
  position: absolute;
  transform-style: preserve-3d;
  animation: run 0.35s ease-in-out infinite alternate;
}
@keyframes run {
  0% {
    transform: rotateY(45deg) rotateX(-10deg) rotate(15deg);
  }
  100% {
    transform: rotateY(40deg) rotateX(-20deg) rotate(10deg);
  }
}
.loadingBody .wrap .cube .face {
  margin: 0;
  width: 200px;
  height: 400px;
  display: block;
  position: absolute;
  background: #d8ebff;
  box-shadow: inset 0 0 0 3px #222;
}
.loadingBody .wrap .cube .face:nth-of-type(1) {
  transform: rotateY(0deg) translateZ(100px);
  background: transparent;
  transform-style: preserve-3d;
}
.loadingBody .wrap .cube .face:nth-of-type(1):before {
  content: '';
  position: absolute;
  width: 100%;
  height: 100%;
  box-shadow: inset 0 0 0 3px #222, inset 0 0 0 15px #bfdeff, inset 0 0 0 18px #222;
}
.loadingBody .wrap .cube .face:nth-of-type(1) .topdoor, .loadingBody .wrap .cube .face:nth-of-type(1) .bottomdoor {
  overflow: hidden;
  box-shadow: inset 0 0 0 3px #222;
}
.loadingBody .wrap .cube .face:nth-of-type(1) .topdoor:before, .loadingBody .wrap .cube .face:nth-of-type(1) .bottomdoor:before {
  content: '';
  background: #bbb;
  width: 50px;
  height: 10px;
  position: absolute;
  left: 15px;
  top: 60px;
  box-shadow: inset 0 0 0 3px #222;
}
.loadingBody .wrap .cube .face:nth-of-type(1) .topdoor:after, .loadingBody .wrap .cube .face:nth-of-type(1) .bottomdoor:after {
  content: '';
  position: absolute;
  width: 100%;
  height: 10px;
  bottom: 0;
  left: 0;
  background: #bbb;
  box-shadow: inset 0 0 0 3px #222;
}
.loadingBody .wrap .cube .face:nth-of-type(1) .topdoor {
  position: absolute;
  width: calc(100% - 25px);
  background: #cbe4ff;
  height: 100px;
  top: 12.5px;
  left: 12.5px;
  transform-origin: 100% 50%;
  border-radius: 10px;
  animation: swingopen 1s ease-in-out infinite alternate;
}
@keyframes swingopen {
  0% {
    transform: rotateY(0deg);
  }
  20% {
    transform: rotateY(5deg);
  }
  70% {
    transform: rotateY(0deg);
  }
  80% {
    transform: rotateY(2.5deg);
  }
  100% {
    transform: rotateY(0deg);
  }
}
.loadingBody .wrap .cube .face:nth-of-type(1) .bottomdoor {
  position: absolute;
  width: calc(100% - 25px);
  height: 275px;
  bottom: 12.5px;
  left: 12.5px;
  border-radius: 10px;
  background: #cbe4ff;
  transform-origin: 100% 50%;
  transform: rotateY(0deg);
  animation: swingopen 1s ease-in-out infinite alternate;
  animation-delay: 0.25s;
}
.loadingBody .wrap .cube .face:nth-of-type(1) .bottomdoor .smile {
  position: absolute;
  width: 30px;
  height: 15px;
  bottom: 30px;
  left: calc(50% - 7.5px);
  background: #000;
  border-radius: 0 0 50px 50px;
}
.loadingBody .wrap .cube .face:nth-of-type(1) .bottomdoor .smile:before {
  content: '';
  position: absolute;
  left: -10px;
  top: -15px;
  background: #222;
  border-radius: 100%;
  width: 10px;
  height: 10px;
  box-shadow: 40px 0 0 0 #222;
}
.loadingBody .wrap .cube .face:nth-of-type(1) .bottomdoor:after {
  bottom: auto;
  top: 0;
}
.loadingBody .wrap .cube .face:nth-of-type(2) {
  transform: rotateX(180deg) translateZ(100px);
  background: #ddd;
}
.loadingBody .wrap .cube .face:nth-of-type(3) {
  transform: rotateY(90deg) translateZ(100px);
  background: #a5d1ff;
}
.loadingBody .wrap .cube .face:nth-of-type(3):before {
  content: '';
  position: absolute;
  width: 100%;
  height: 100%;
  left: 0;
  top: 0;
  background: #bbb;
  box-shadow: inset 0 0 0 3px #222;
}
.loadingBody .wrap .cube .face:nth-of-type(4) {
  transform: rotateY(-90deg) translateZ(100px);
  background: #a5d1ff;
}
.loadingBody .wrap .cube .face:nth-of-type(5) {
  height: 200px;
  transform: rotateX(90deg) translateZ(100px);
  background: #d8ebff;
  box-shadow: inset -5px 5px 0 10px #222;
}
.loadingBody .wrap .cube .face:nth-of-type(6) {
  height: 200px;
  transform: rotateX(-90deg) translateZ(300px);
  background: #8cc4ff;
  box-shadow: inset 0 0 0 10px #222;
}

</style>