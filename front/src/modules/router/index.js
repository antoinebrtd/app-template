import Vue from "vue";
import Router from "vue-router";

const Login = () => import("@/components/auth/Login");
const Callback = () => import("@/components/auth/Callback");
const Main = () => import("@/components/Main");

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: "/",
      name: "login",
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
    },
    {
      path: '*',
      redirect: '/'
    }
  ]
});
