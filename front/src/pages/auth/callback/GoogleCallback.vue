<template>
  <div class="callback">
    <v-container class="text-xs-center" style="height: 100%">
      <v-layout row justify-center fill-height align-center>
            <v-progress-circular indeterminate></v-progress-circular>
      </v-layout>
    </v-container>
  </div>
</template>

<script>
  import auth from "@/modules/auth";

  export default {
    name: 'GoogleCallback',
    mounted() {
      const code = this.$route.query.code;
      const state = this.$route.query.state;
      auth.authorizeGoogle(code, state);
    }
  }
</script>

<style scoped>
  .callback {
    width: 100%;
    height: 100%
  }
</style>