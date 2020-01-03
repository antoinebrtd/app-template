<template>
  <div class="main">
    <v-layout justify-center fill-height row wrap>
      <v-flex xs12>
        <v-parallax dark src="../assets/grey_background.jpeg" class="mb-5">
          <v-row align="center" justify="center">
            <v-col class="text-center" cols="12">
              <h1 class="title font-weight-thin mb-4 primary--text">
                Congratulations <span class="font-weight-bold">{{ username }}</span>, you've made it all the way!
              </h1>
              <h4 class="subheading">Now the fun begins, develop your first feature!</h4>
            </v-col>
          </v-row>
        </v-parallax>
      </v-flex>
      <v-flex xs12>
        <v-card class="elevation-0 mt-5" color="transparent">
          <v-card-text class="text-center display-1 font-weight-bold">
            Launch your app in less than an hour!
          </v-card-text>
          <v-card-text>
            <v-row align="center" justify="center">
              <v-col align-self="end" cols="3">
                <v-img src="../assets/vue.png" alt="vue" class="logo"></v-img>
              </v-col>
              <v-col class="text-start" cols="4">
                <span class="subtitle-1 font-weight-bold">VueJs for performance and handiness</span>
                <v-divider color="primary" style="width: 30%" class="mt-2 mb-5"></v-divider>
                <span>An incrementally adoptable ecosystem that scales between a library and a full-featured framework</span>
              </v-col>
            </v-row>
            <v-row align="center" justify="center">
              <v-col class="text-start" cols="4">
                <span class="subtitle-1 font-weight-bold">Vuetify for design and user experience</span>
                <v-divider color="primary" style="width: 30%" class="mt-2 mb-5"></v-divider>
                <span>
                  A Vue UI Library with beautifully handcrafted Material Components. No design skills required —
                  everything you need to create amazing applications is at your fingertips
                </span>
              </v-col>
              <v-col cols="3">
                <v-img src="https://cdn.vuetifyjs.com/images/logos/v-alt.svg" alt="vue" class="logo"></v-img>
              </v-col>
            </v-row>
            <v-row align="center" justify="center">
              <v-col cols="3">
                <v-img src="http://flask.palletsprojects.com/en/1.1.x/_static/flask-icon.png" alt="vue"
                       class="logo"></v-img>
              </v-col>
              <v-col class="text-start" cols="4">
                <span class="subtitle-1 font-weight-bold">Flask for speed and completeness</span>
                <v-divider color="primary" style="width: 30%" class="mt-2 mb-5"></v-divider>
                <span>A well designed Python framework that offers a wide range of possibilities to build an efficient api that meets your needs</span>
              </v-col>
            </v-row>
          </v-card-text>
        </v-card>
      </v-flex>
    </v-layout>
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
  .main{
    width: 100%;
    height: 100%
  }

  .v-parallax {
    position: relative;
    overflow: hidden;
    z-index: 0;
    -webkit-clip-path: polygon(0 0, 100% 0, 100% 75%, 0 100%);
    clip-path: polygon(0 0, 100% 0, 100% 75%, 0 100%);
    height: 100vh;
  }

  .logo {
    width: 320px;
  }
</style>