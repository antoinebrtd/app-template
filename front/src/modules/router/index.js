import Vue from "vue";
import Router from "vue-router";

const Login = () => import("../../pages/auth/Login");
const ForgotPassword = () => import("../../pages/auth/ForgotPassword");
const ResetPassword = () => import("../../pages/auth/ResetPassword");
const GoogleCallback = () => import("../../pages/auth/callback/GoogleCallback");
const FacebookCallback = () => import("../../pages/auth/callback/FacebookCallback");
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
      path: "/auth/email/forgot-password",
      name: "forgot-password",
      meta: {
        hideHeader: true,
      },
      component: ForgotPassword
    },
    {
      path: "/auth/email/reset-password/:token",
      name: "reset-password",
      meta: {
        hideHeader: true,
      },
      component: ResetPassword
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