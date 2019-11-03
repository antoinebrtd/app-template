<template>
  <div class="callback">
    <v-container class="text-xs-center" pt-1>
      <v-layout row justify-center>
        <v-flex xs12>
          <div v-if="!error">
            <v-progress-circular indeterminate></v-progress-circular>
          </div>
          <div v-else>
            {{ errorMessage }}<br/>
            <v-btn to="/" color="error">Go to the home page</v-btn>
          </div>
        </v-flex>
      </v-layout>
    </v-container>
  </div>
</template>

<script>
  import auth from "../../modules/auth/index";

  export default {
    name: 'Callback',
    data() {
      return {
        error: false,
        errorMessage: ''
      }
    },
    mounted() {
      const code = this.$route.query.code;
      const state = this.$route.query.state;
      auth.authorize(this, code, state);
    }
  }
</script>

<style scoped>
  .callback {
    width: 100%;
    text-align: center;
  }
</style>