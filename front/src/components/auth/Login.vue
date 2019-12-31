<template>
  <div class="login">
    <v-container class="text-xs-center" pt-1>
      <v-layout row justify-center>
        <v-flex xs12 sm6>
          <v-card flat id="card" color="transparent">
            <v-card-text primary-title>
              <v-layout column align-center v-if="!signUpView">
                <email-login :token="$route.params.token"></email-login>
                <v-btn text class="button mt-2" color="primary" @click="signUpView = !signUpView">
                  Don't have an account ? Sign up!
                </v-btn>
              </v-layout>
              <v-layout column align-center v-else>
                <email-sign-up></email-sign-up>
                <v-btn text class="button mt-2" color="primary" @click="signUpView = !signUpView">
                  Already have an account ? Log in.
                </v-btn>
              </v-layout>
              <v-card-text class="mt-5">
                <span>Or</span>
              </v-card-text>
              <v-card-text class="mt-5">
                <google-login></google-login>
                <facebook-login class="mt-5"></facebook-login>
              </v-card-text>
            </v-card-text>
          </v-card>
        </v-flex>
      </v-layout>
     </v-container>
  </div>
</template>

<script>
  import auth from "@/modules/auth";
  import notifications from '@/modules/notifications';
  import GoogleLogin from "./util/GoogleLogin";
  import EmailLogin from "./util/EmailLogin";
  import EmailSignUp from "./util/EmailSignUp";
  import FacebookLogin from "./util/FacebookLogin";

  export default {
    name: 'Login',
    components: {FacebookLogin, EmailSignUp, EmailLogin, GoogleLogin},
    data() {
      return {
        signUpView: false
      }
    },
    created() {
      auth.checkAuth().then(() => {
        if (this.$route.params.token) {
          auth.activateAccount(this.$route.params.token).then(() => {
            this.$router.replace('/home');
          }).catch(error => {
            this.$router.replace('/home');
          })
        } else {
          this.$router.replace('/home');
        }
      }).catch(() => {
        if (this.$route.params.token) {
          notifications.addNotification('Please login to confirm your email address')
        }
      });
    }
  }
</script>

<style scoped>
  .login {
    width: 100%;
    text-align: center;
  }

  #card {
    margin: 4em;
  }

  .button {
    text-transform: None !important;
    text-decoration: underline;
  }
</style>