<template>
  <div class="login">
    <v-container class="text-xs-center" pt-1>
      <v-layout row justify-center>
        <v-flex xs12 sm6>
          <v-card flat id="card" color="transparent">
            <v-card-text primary-title>
              <div class="text">
                <google-login></google-login>
              </div>
            </v-card-text>
          </v-card>
        </v-flex>
      </v-layout>
     </v-container>
  </div>
</template>

<script>
  import auth from "../../modules/auth/index";
  import GoogleLogin from "./util/GoogleLogin";

  export default {
    name: 'Login',
    components: {GoogleLogin},
    mounted() {
      auth.checkAuth().then(() => {
        this.$router.replace('/home');
      }).catch(() => {
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

  .text {
    width: 500px;
    max-width: 90%;
    margin: auto;
    text-align: left;
  }
</style>