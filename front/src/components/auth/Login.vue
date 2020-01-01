<template>
  <div class="login">
    <v-container class="text-xs-center" v-if="loaded">
      <v-layout row justify-center>
        <v-flex xs12 sm6>
          <v-card flat id="card" color="transparent">
            <v-card-text primary-title>
              <email-login :token="$route.params.token"></email-login>
              <v-card-text class="mt-5">
                <span>Or</span>
              </v-card-text>
              <google-login class="mt-5"></google-login>
              <facebook-login class="mt-5"></facebook-login>
            </v-card-text>
          </v-card>
        </v-flex>
      </v-layout>
     </v-container>
  </div>
</template>

<script>
  import auth from "@/modules/auth";
  import GoogleLogin from "./util/GoogleLogin";
  import EmailLogin from "./util/EmailLogin";
  import FacebookLogin from "./util/FacebookLogin";

  export default {
    name: 'Login',
    components: {FacebookLogin, EmailLogin, GoogleLogin},
    data() {
      return {
        loaded: false,
        token: this.$route.params.token
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
        this.loaded = true;
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
</style>