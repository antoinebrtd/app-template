import Vue from "vue";
import Router from "vue-router";

const Login = () => import("../../components/auth/Login");
const Callback = () => import("../../components/auth/Callback");
const Main = () => import("../../components/Main");

Vue.use(Router);

export default new Router({
  routes: [

    {
      path: '*',
      redirect: '/login'
    },
    {
      path: "/login",
      name: "login",
      component: Login
    },
    {
      path: "/login/:token",
      name: "activate-account",
      component: Login
    },
    {
      path: "/auth/callback",
      name: "callback",
      component: Callback
    },
    {
      path: "/home",
      name: "home",
      component: Main
    }
  ]
});