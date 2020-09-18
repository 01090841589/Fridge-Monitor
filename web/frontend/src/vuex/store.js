import Vue from "vue";
import Vuex from "vuex";
import router from "../routes";
import jwtDecode from 'jwt-decode'
import createPersistedState from "vuex-persistedstate";
Vue.use(Vuex);
import http from "@/utils/http-require.js";
// import axios from "axios"
export default new Vuex.Store({
  plugins: [
    createPersistedState()
  ],
  state: {
    isLogin: false,
    isLoginError:false,
    isLoading: false,
    token : null,
    test : [ 
   ]
  },
  mutations:{
    // 로그인이 성공했을때,
    loginSuccess(state) {
      state.isLogin = true
      state.isLoginError = false
      console.log(state.isLogin)
      console.log("로그인성공")
      console.log(state)
    },
    signOut(state){
      state.isLogin= false
      state.token = null
    },
    // 로그인이 실패했을때
    loginError(state) {
      state.isLogin = false
      state.isLoginError = true
      console.log(state.isLogin)
      console.log("로그인실패")

    },

    loadingSet(state){
      state.isLoading = !state.isLoading
    }

  },
  getters :{
    requestHeader: function(state) {
      return {
        headers: {
          Authorization: 'JWT '+ state.token
        }
      }
    },
    userId: function(state) {
      return state.token ? jwtDecode(state.token).user_id : null
    }
  },

  actions: {
    login({commit}, loginObj) {
      console.log(loginObj)
      http.post(`api-token-auth/`, loginObj)
      .then(res => {
        if (res.status === 200){
          let token = res.data.token
          this.state.token = token
          //토큰을 로컬스토리지에 저장
          localStorage.setItem("access_token", token)
          commit('loginSuccess')
          // this.dispatch("getMemberInfo")
          console.log(token)
          router.push({name:'list'})
        } else{
          alert("로그인 실패");
        }
      })
      .catch((err) => {
        console.log(err)
        alert(`서버 접속 오류`);
        commit('loginError')
      })

    },

    getMemberInfo({commit}) {
      // 로컬 스토리지에 저장되어 있는 토큰을 불러옴
      let token = localStorage.getItem("access_token")
      let config = {
        headers: {
          "access-token": token
        }
      }
      // 토큰 -> 멤버 정보를 반환
      // 새로 고침 -> 토큰만 가지고 멤버정보를 요청
      http
        .get("/api-token-auth/", config)
        .then(res =>{
          let userInfo = {
            username: res.data.username
          }
          commit("loginSuccess", userInfo)
        })
        .catch(()=>
        alert("아이디와 비밀번호를 확인하세요"))
    },
    logout({commit}){
      console.log("로그아웃버튼 누름")
      commit("signOut")
      router.push({name : "login"})
    },

    loading({state,commit}){
      if(state.isLoading){
        console.log("로딩이 끝난다.")
        commit("loadingSet")
        
      }
      else{
        console.log("로딩이 시작된다.")
        commit("loadingSet")

      }
      

    },

    },
  }
);
