<template>
  <div class="main">
    <v-responsive class="my-5">
      <v-container class="text-xs-center">
        <v-layout justify-center>
          <v-flex pt-4>
            <span>Congratulations <span class="font-weight-bold">{{ username }}</span>, you've made it all the way!
              Now the fun begins, develop your first feature!</span>
          </v-flex>
        </v-layout>
      </v-container>
    </v-responsive>
  </div>
</template>


<script>
  import auth from "@/modules/auth";

  export default {
    name: 'Main',
    data() {
      return {
        username: auth.user.profile.first_name,
      }
    },
  }
</script>

<style scoped>
</style>