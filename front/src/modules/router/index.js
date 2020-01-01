import Vue from "vue";
import Router from "vue-router";

const Login = () => import("../../pages/Login");
const GoogleCallback = () => import("../../components/auth/callback/GoogleCallback");
const FacebookCallback = () => import("../../components/auth/callback/FacebookCallback");
const Main = () => import("../../pages/Home");

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
      meta: {
        hideHeader: true,
      },
      component: Login
    },
    {
      path: "/login/:token",
      name: "activate-account",
      meta: {
        hideHeader: true,
      },
      component: Login
    },
    {
      path: "/auth/google/callback",
      name: "google-callback",
      meta: {
        hideHeader: true,
      },
      component: GoogleCallback
    },
    {
      path: "/auth/facebook/callback",
      name: "facebook-callback",
      meta: {
        hideHeader: true,
      },
      component: FacebookCallback
    },
    {
      path: "/home",
      name: "home",
      meta: {},
      component: Main
    }
  ]
});