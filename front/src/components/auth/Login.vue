<template>
  <div class="login">
    <v-container class="text-xs-center" pt-1>
      <v-layout row justify-center>
        <v-flex xs12 sm6>
          <v-card flat id="card" color="transparent">
            <v-card-text primary-title>
              <div class="text">
                <v-btn block v-on:click="login" id="connect">Log in</v-btn>
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

  export default {
    name: 'Login',
    data() {
      return {
        email: "",
        password: ""
      }
    },
    mounted() {
      let login = this;

      auth.checkAuth().then(() => {
        login.$router.replace('/home');
      }).catch(() => {
      });
    },
    methods: {
      login() {
        auth.login(this);
      }
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

  #connect {
    margin-top: 2em;
    margin-bottom: 2em;
  }
</style>