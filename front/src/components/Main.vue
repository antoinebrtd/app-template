<template>
  <div class="main">
    <v-responsive class="my-5">
      <v-container class="text-xs-center">
        <v-layout justify-center>
          <v-flex pt-4>
            <span class="title">{{ username }}</span>
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
        username: auth.user.profile.name,
      }
    },
  }
</script>

<style scoped>
</style>