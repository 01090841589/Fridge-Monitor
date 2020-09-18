<template>
  <div id="loginPage">
    <div id="loginColor">
      <div id="banner">
        <span>
          <img id="logo" src="../../assets/images/logo.png" >
          <p id="projectName">FrigeMonitor</p>
        </span>
      </div>

      <div class="w3-center">
        <form action="#" target="_blank" id="loginForm" @submit.prevent>
          <p>
            <input
              class="w3-input w3-padding-16"
              type="text"
              placeholder="ID"
              required
              name="ID"
              v-model="username"
            />
          </p>
          <p>
            <input
              class="w3-input w3-padding-16"
              type="password"
              placeholder="Password"
              required
              name="password"
              v-model="password"
            />
          </p>
          <div class>
            <p id="buttons">
              <v-btn color="info" @click="login({username:username, password:password})">로그인</v-btn>
              <v-btn color="info" @click="$router.push('/SignUp')">회원가입</v-btn>
              <v-btn color="info" @click="$router.push(`/FindPassword`)">비밀번호 찾기</v-btn>

            </p>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import {mapActions, mapState} from "vuex"
export default {
  components: {
  },
    data: () => {
    return {
      username: "",
      password: "",
    };
  },
  methods : {
    ...mapActions(["login"]),
    back() {
      this.$router.go(-1);
        },
    },
  
  computed: {
    ...mapState(["isLogin"])

  }

};


</script>

<style>
#loginForm{
  text-align: center;
  margin-top: 5%;
  padding-left: 20%;
  padding-right: 20%;
  padding-bottom: 20%;
}
#buttons{
  margin:0 30%;
  display: flex;
  justify-content: space-around;
  /* background-color: skyblue; */

}

#loginColor{
  margin: auto;
  min-width: 350px;
  max-width: 800px;
  /* padding-top: 5%; */
  background-color: rgba( 255, 255, 255, 0.8 );
  

}

#projectName{
  font-size: 40px;
}

#logo{
  display: flex;
  width: 100px;
  height: auto;

}
</style>