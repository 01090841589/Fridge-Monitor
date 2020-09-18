<template>
  <div id="notFound">
    
    <h1 style="text-align:center; font-family: 'Stylish', sans-serif;">The FridgeMonitor NotFound Page</h1>
    <h5>(냉장고 문을 클릭해보세요)</h5>
    <v-btn @click="back" style="margin-bottom:10px">
      <v-icon>mdi-arrow-left</v-icon>
      <p id="notFoundText" style="margin-left:15px"> 돌아가기 </p>
    </v-btn>
    <div class="fridge--container">
      <div id="notFoundText">404 NOT FOUND <br>
      안타깝지만 <br> 당신의 잘못입니다.</div>
      <input type="checkbox" id="freezer-toggle"/>
      <label for="freezer-toggle"></label>


      <input type="checkbox" id="fridge-toggle"/>
      <label for="fridge-toggle"></label>
    </div>
    <!-- <v-layout justify-center style="padding-top:5%">
      <img :src="imgSrc" height="300px" alt="" />
    </v-layout>
    <v-layout justify-center>
      <div id="notFoundText">404 Not Found
        <br>
        페이지를 찾을 수 없습니다.
        <br>
        It's all your fault!
      </div>
    </v-layout>
    <v-layout justify-center>
      <v-btn @click="back">
        <v-icon>mdi-arrow-left</v-icon>
        Back
      </v-btn>
    </v-layout> -->
  </div>
</template>

<script>
export default {
  name: "NotFound",
  data: () => ({
    imgSrc: require("../assets/images/gora.png"),
  }),
  methods: {
    back() {
      this.$router.go(-1);
    },
  },
};
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Stylish&display=swap');
/* #notFound {
  padding: 5%;
}

#notFoundText{
  margin: 2%;
  text-align: center;
} */

#notFoundText{
  color: black;
  text-align: center;
  padding-top:15px;
  font-weight: 700;
  font-family: 'Stylish', sans-serif;
}
#notFound {
  background-color: #f39c12;
  color: white;
  display: -webkit-box;
  display: flex;
  -webkit-box-orient: vertical;
  -webkit-box-direction: normal;
          flex-direction: column;
  -webkit-box-pack: center;
          justify-content: center;
  -webkit-box-align: center;
          align-items: center;
  min-height: 100vh;
  font-family: monospace;
  /* background-image: url('data:image/svg+xml,%3Csvg width="128" height="128" viewBox="0 0 64 64" xmlns="http://www.w3.org/2000/svg"%3E%3Cpath d="M8 16c4.418 0 8-3.582 8-8s-3.582-8-8-8-8 3.582-8 8 3.582 8 8 8zm0-2c3.314 0 6-2.686 6-6s-2.686-6-6-6-6 2.686-6 6 2.686 6 6 6zm33.414-6l5.95-5.95L45.95.636 40 6.586 34.05.636 32.636 2.05 38.586 8l-5.95 5.95 1.414 1.414L40 9.414l5.95 5.95 1.414-1.414L41.414 8zM40 48c4.418 0 8-3.582 8-8s-3.582-8-8-8-8 3.582-8 8 3.582 8 8 8zm0-2c3.314 0 6-2.686 6-6s-2.686-6-6-6-6 2.686-6 6 2.686 6 6 6zM9.414 40l5.95-5.95-1.414-1.414L8 38.586l-5.95-5.95L.636 34.05 6.586 40l-5.95 5.95 1.414 1.414L8 41.414l5.95 5.95 1.414-1.414L9.414 40z" fill="rgba(255,255,255,1)" fill-opacity="0.1" fill-rule="evenodd"/%3E%3C/svg%3E'); */
}

h1 {
  margin: 10px 0px;
}

h5 {
  margin-bottom: 10px;
}

.fridge--container {
  width: 200px;
  height: 400px;
  background-color: #e3f2fd;
  border-radius: 20px;
  border: 8px solid #c62828;
  box-shadow: 0px 0px 70px white;
  position: relative;
}
.fridge--container{
  background-position: center center;
  background-image: url('../assets/images/gora.png');
  background-size: contain;
}
.fridge--container input[type="checkbox"] {
  -webkit-appearance: none;
     -moz-appearance: none;
          appearance: none;
  /* display: block;
  width: 200px;
  background-color: #e3f2fd;
  border: 8px solid #64b5f6;
  outline: 0; */
}
.fridge--container input[type="checkbox"]#freezer-toggle {
  border-radius: 10px 10px 0px 0px;
  height: 130px;
  margin-bottom: 8px;
}
.fridge--container input[type="checkbox"]#freezer-toggle:after {
  content: "";
  display: block;
  width: 100%;
  height: 4px;
  box-shadow: 0px 30px 0px #64b5f6, 0px 80px 0px #64b5f6;
}
.fridge--container input[type="checkbox"]#freezer-toggle + label {
  top: -8px;
  right: -8px;
  height: 130px;
  border-radius: 20px 20px 0px 0px;
  background-color: #ef5350;
}
.fridge--container input[type="checkbox"]#freezer-toggle + label:after {
  content: "";
  display: block;
  height: 40px;
  position: absolute;
  left: 20px;
  width: 0px;
  border: 4px solid white;
  border-radius: 10px;
  bottom: 20px;
}
.fridge--container input[type="checkbox"]#freezer-toggle:checked + label {
  right: -66px;
  width: 50px;
  border-radius: 10px 20px 20px 10px;
}
.fridge--container input[type="checkbox"]#freezer-toggle:checked + label:after {
  border: 8px solid white;
  border-left: 0px;
  width: 10px;
  left: 50px;
  z-index: -1;
}
.fridge--container input[type="checkbox"]#fridge-toggle {
  border-radius: 0px 0px 10px 10px;
  height: 262px;
}
.fridge--container input[type="checkbox"]#fridge-toggle:after {
  content: "";
  height: 4px;
  display: block;
  width: 100%;
  box-shadow: 0px 40px 0px #64b5f6, 0px 100px 0px #64b5f6, 0px 160px 0px #64b5f6;
}
.fridge--container input[type="checkbox"]#fridge-toggle + label {
  border-radius: 0px 0px 20px 20px;
  top: 130px;
  height: 262px;
  background-color: #ef5350;
  right: -8px;
}
.fridge--container input[type="checkbox"]#fridge-toggle + label:after {
  content: "";
  display: block;
  position: absolute;
  top: 20px;
  left: 20px;
  border: 4px solid white;
  height: 80px;
  border-radius: 10px;
}
.fridge--container input[type="checkbox"]#fridge-toggle:checked + label {
  right: -66px;
  width: 50px;
  border-radius: 0px 20px 20px 10px;
}
.fridge--container input[type="checkbox"]#fridge-toggle:checked + label:after {
  top: 20px;
  left: 50px;
  width: 2px;
  border: 8px solid white;
  border-left: 0;
  padding-left: 8px;
  z-index: -1;
}
.fridge--container input[type="checkbox"] + label {
  position: absolute;
  border: 8px solid #c62828;
  border-radius: 20px;
  width: 100%;
}
.fridge--container input[type="checkbox"] + label:before {
  content: "";
  display: none;
  position: absolute;
  left: -100px;
  top: 8px;
  width: 60px;
  height: 30px;

  -webkit-clip-path: polygon(25% 0, 75% 0, 100% 100%, 0% 100%);
          clip-path: polygon(25% 0, 75% 0, 100% 100%, 0% 100%);
}
.fridge--container input[type="checkbox"]:checked + label:before {
  display: block;
}

</style>
