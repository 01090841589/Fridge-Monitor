import Vue from "vue";
import Router from "vue-router";
import signUp from "./views/user/signUp";
import leave from "./views/leave";
import NotFound from "./views/NotFound";
import frontPage from "./views/user/frontPage"
import List from "./views/refrigeratorList/list"
import ingreDetail from "./views/refrigeratorList/ingreDetail"
import Main from "./views/refrigiratorList/main"
import FloorDetail from "./views/refrigiratorList/FloorDetail"
import ProductAdd from "./views/refrigiratorList/productAdd";
import ProductAddInfo from "./views/refrigiratorList/productAddInfo";
import findPassword from "./views/user/findPassword"
import test from "./views/test";
import store from "./vuex/store"

Vue.use(Router);

const rejectAuthUser =(to, from, next) =>{
  if (store.state.isLogin === true){
    alert("로그인되어 있습니다.")
    console.log(store.state)
    next('/list')
  }else{
    next()
  }
}

const rejectNotAuthUser =(to, from, next) =>{
  if (store.state.isLogin === false){
    alert("로그인해주세요.")
    next('/login')
  }else{
    next()
  }
}


const router = new Router({
  mode: "history",
  routes: [
    {
      path: "/",
      redirect: "/login"
    },

    {
      path: "/login",
      name: "login",
      beforeEnter: rejectAuthUser,
      component: frontPage,
    },

    {
      path: "/signUp",
      name: "signUp",
      component: signUp,
    },

    {
      path: "/leave",
      name: "leave",
      component: leave,
    },
    {
      path: "*",
      redirect: "/404",
    },
    {
      path: "/404",
      name: "NotFound",
      component: NotFound,
    },
    {
      path: "/main",
      name: "main",
      component: Main,
    },
    {
      path: "/floorDetail",
      name: "floorDetail",
      component: FloorDetail,
    },
    {
      path: "/productAdd",
      name: "productAdd",
      component: ProductAdd,
    },
    {
      path: "/productAddInfo",
      name: "productAddInfo",
      component: ProductAddInfo,
    },
    {
      path: "/ingreDetail",
      name: "ingreDetail",
      component: ingreDetail,
    },
    {
      path: "/list",
      name: "list",
      beforeEnter: rejectNotAuthUser,
      component: List,
    },
    {
      path: "/findPassword",
      name: "findPassword",
      component: findPassword,
    },
    {
      path: "/test",
      name: "test",
      component: test,
    },
  ],
});


export default router;
