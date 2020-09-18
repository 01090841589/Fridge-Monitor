<template>
  <div>
    <div id="signUpPage">
      <form 
      class="w3-container w3-card-4 w3-round w3-light-grey w3-opacity-min"
      id="signUpForm"
      @submit.prevent="this.signUp()">

        <h2 class="w3-center">회원가입</h2>
      
        <p>
          <label>
            <span style="color:red">*</span> ID
          </label>
            <button
            class="w3-right w3-button w3-white w3-border w3-round-large">
            중복체크
            </button>
            <input 
            class="w3-input w3-border w3-hover-blue"
            type="text"
            v-model="formdata.username">
        </p>
        <p>
          <label>
            <span style="color:red">*</span> Password
          </label>
          <input 
          class="w3-input w3-border w3-hover-blue"
          type="password"
          v-model="formdata.password">
        </p>
        <p>
          <label>
            <span style="color:red">*</span> Password 확인
          </label>
          <label style="color:red" v-show="pagedata.passwordCheck"> Password가 일치하지 않습니다.</label>
          <input 
          class="w3-input w3-border w3-hover-blue"
          type="password"
          v-model="formdata.passwordConfirm">
        </p>
        <p>
          <label>
            <span style="color:red">*</span> Email
          </label>
          <input 
            class="w3-input w3-border w3-hover-blue"
            type="email"
            v-model="formdata.email">
        </p>
        <p id="bntdiv" class="w3-center">
          <v-btn id="btn" color="info" @click="$router.push(`/`)"><i class="fa fa-home"></i> HOME</v-btn>
          <v-btn id="btn" color="info" @click="checkdata()"><i class="fa fa-arrow-right"></i> SignUp</v-btn>
        </p>

      </form>

    </div>
  </div>
</template>

<script>
import {mapState} from "vuex"
// import axios from "axios"
import http from "@/utils/http-require.js";
export default {
  data:() => {
    return{
      formdata: {
        username: "",
        password: "",
        passwordConfirm:"",
        email:"",
      },

      pagedata:{
        passwordCheck: false,
        isOverlap : null

      }
    }
    
  },
  methods:{
    // ...mapActions(["signUp"]),

    checkdata(){
      if(this.formdata.username.length == 0 ){
        alert("ID를 입력해주세요")
      }
      else if (this.pagedata.isOverlap){
        alert("ID 중복여부를 확인해주세요")
      }
      else if (!(this.formdata.password.length >0 && this.formdata.passwordConfirm.length >0 && !this.pagedata.passwordCheck)){
        console.log(this.pagedata.isOverlap)
        alert("password를 확인해주세요")
      }
      else if(!(this.formdata.email.length > 0)){
        console.log(this.formdata.email)
        console.log(this.formdata.email.length)
        alert("Email을 확인해주세요")
      }
      else if(!this.isEmail(this.formdata.email)){
        alert("Email 형식을 확인해주세요")
        console.log("Email 형식을 확인해주세요")
      }

      else{
        console.log("SignUp 요청")
        this.signUp()
      }

      },

        
    
    signUp(){
      console.log(this.formdata)
      http.post(`/userapi/signup/`, this.formdata)
      .then((res) => {
        console.log(res)
        alert("회원가입을 축하합니다.");
        this.$router.push("/")
      }
      )
      .catch((err)=>{
        console.log(err)
        alert("회원가입에 실패하였습니다.");
      })
      .finally(() =>
      this.isLoading = false)

    },
  /* eslint-disable */
    isEmail(email) {
      var regExp = /^[0-9a-zA-Z]([-_\.]?[0-9a-zA-Z])*@[0-9a-zA-Z]([-_\.]?[0-9a-zA-Z])*\.[a-zA-Z]{2,3}$/i;

      return regExp.test(email); // 형식에 맞는 경우 true 리턴	

    }
  /* eslint-enable */
  },

  computed: {
    ...mapState(["isLogin"])

  },

  watch:{
    "formdata.passwordConfirm"(){
      if(this.formdata.password === this.formdata.passwordConfirm){
        this.pagedata.passwordCheck = false
      }
      else{
        this.pagedata.passwordCheck = true
        
      }
    },

    "formdata.password"(){
      this.pagedata.passwordCheck =
      this.formdata.password === this.formdata.passwordConfirm 
        ? false:true

    }

}

}
</script>

<style>
  #signUpPage{
    padding-top: 5%;
    padding-left: 15%;
    padding-right: 15%;
    padding-bottom: 15%;
    background-image: url("https://cdn.pixabay.com/photo/2016/09/04/21/33/bird-1645305_1280.jpg");
    background-position: center;
    background-size: contain;

  }

  #signUpForm{
    margin: auto;
  }
  #btn:hover{
    color: black;
  }

  #bntdiv{
      margin:3% 30%;
    display: flex;
    justify-content: space-around;
  }
</style>