<template>
  <div class="main">
    <v-container fluid class="pa-0">
      <v-row no-gutters justify="center" align="center">

        <v-col cols="12">
          <v-parallax dark src="../assets/grey_background.jpeg" class="mb-5 bottom-slant" height="500">
          <v-row align="center" justify="center">
            <v-col class="text-center" cols="12">
              <v-row justify="center" align="center" :class="!build && translateUp ? 'translate-up' : ''">
                <v-fade-transition>
                  <div
                          v-if="greetings"
                          :class="greetings && !translateLeft ? 'appear' : (!welcome && translateLeft ? 'translate-left' : '')"
                          style="width: 180px"
                  >
                  <span class="display-1 font-weight-thin mb-4 primary--text">
                    Hi <span class="font-weight-bold">{{ username }}</span>,
                  </span>
                  </div>
                </v-fade-transition>
                <v-fade-transition>
                  <div v-if="welcome" class="appear" style="width: 320px">
                    <span class="display-1 font-weight-thin mb-4 primary--text">welcome to your app!</span>
                  </div>
                </v-fade-transition>
              </v-row>
              <v-fade-transition>
                <h4 class="subheading appear mt-4" style="width: 100%" v-if="build">
                  Now the fun begins, develop your first feature!
                </h4>
              </v-fade-transition>
            </v-col>
          </v-row>
        </v-parallax>
        </v-col>

        <v-col cols="12">
          <v-card class="elevation-0 mt-5" color="transparent">
            <v-card-text class="text-center display-1 font-weight-bold">
              Launch your app in less than an hour!
            </v-card-text>
            <v-card-text>
              <v-hover v-slot:default="{ hover }">
                <v-row align="center" justify="center">
                  <v-col align-self="end" cols="3">
                    <v-img src="../assets/logos/vue.png" alt="vue" class="logo"></v-img>
                  </v-col>
                  <v-col class="text-start" cols="4">
                    <span class="subtitle-1 font-weight-bold">VueJs for performance and handiness</span>
                    <v-divider color="primary" style="width: 30%" class="mt-2 mb-5"></v-divider>
                    <span>An incrementally adoptable ecosystem that scales between a library and a full-featured framework</span>
                    <a href="https://vuejs.org/" target="_blank" class="link">
                      <v-row align="center" justify="center" class="mt-5">
                        <v-slide-x-reverse-transition hide-on-leave>
                          <span :class="hover ? 'primary--text ease hover-discover' : 'ease'">discover</span>
                        </v-slide-x-reverse-transition>
                        <v-slide-x-transition hide-on-leave>
                          <v-icon color="primary" v-if="hover">arrow_right_alt</v-icon>
                        </v-slide-x-transition>
                      </v-row>
                    </a>
                  </v-col>
                </v-row>
              </v-hover>
              <v-hover v-slot:default="{ hover }">
                <v-row align="center" justify="center">
                  <v-col class="text-start" cols="4">
                    <span class="subtitle-1 font-weight-bold">Vuetify for design and user experience</span>
                    <v-divider color="primary" style="width: 30%" class="mt-2 mb-5"></v-divider>
                    <span>
                    A Vue UI Library with beautifully handcrafted Material Components. No design skills required —
                    everything you need to create amazing applications is at your fingertips
                  </span>
                    <a href="https://vuetifyjs.com/en/" target="_blank" class="link">
                      <v-row align="center" justify="center" class="mt-5">
                        <v-slide-x-reverse-transition hide-on-leave>
                          <span :class="hover ? 'primary--text ease hover-discover' : 'ease'">discover</span>
                        </v-slide-x-reverse-transition>
                        <v-slide-x-transition hide-on-leave>
                          <v-icon color="primary" v-if="hover">arrow_right_alt</v-icon>
                        </v-slide-x-transition>
                      </v-row>
                    </a>
                  </v-col>
                  <v-col cols="3">
                    <v-img src="https://cdn.vuetifyjs.com/images/logos/v-alt.svg" alt="vue" class="logo"></v-img>
                  </v-col>
                </v-row>
              </v-hover>
              <v-hover v-slot:default="{ hover }">
                <v-row align="center" justify="center">
                  <v-col cols="3">
                    <v-img src="http://flask.palletsprojects.com/en/1.1.x/_static/flask-icon.png" alt="vue"
                           class="logo"></v-img>
                  </v-col>
                  <v-col class="text-start" cols="4">
                    <span class="subtitle-1 font-weight-bold">Flask for speed and completeness</span>
                    <v-divider color="primary" style="width: 30%" class="mt-2 mb-5"></v-divider>
                    <span>A well designed Python framework that offers a wide range of possibilities to build an efficient api that meets your needs</span>
                    <a href="http://flask.palletsprojects.com/en/1.1.x/" target="_blank" class="link">
                      <v-row align="center" justify="center" class="mt-5">
                        <v-slide-x-reverse-transition hide-on-leave>
                          <span :class="hover ? 'primary--text ease hover-discover' : 'ease'">discover</span>
                        </v-slide-x-reverse-transition>
                        <v-slide-x-transition hide-on-leave>
                          <v-icon color="primary" v-if="hover">arrow_right_alt</v-icon>
                        </v-slide-x-transition>
                      </v-row>
                    </a>
                  </v-col>
                </v-row>
              </v-hover>
            </v-card-text>
          </v-card>
        </v-col>

        <v-col cols="12">
          <v-parallax dark src="../assets/grey_background.jpeg" class="mb-5 double-slant" height="800">
            <v-container fluid>
              <v-row dense align="center" justify="center">
                <v-col cols="12" align-self="center" class="mb-5 pb-5">
                  <v-row justify="center" class="display-1">The backend stacks</v-row>
                </v-col>
                <v-col class="text-center mt-5" cols="2" v-for="stack in stacks" :key="stack.name">
                  <v-hover v-slot:default="{ hover }">
                    <a :href="stack.link" target="_blank" class="link">
                      <v-card :class="hover ? 'hover mx-2' : 'ease mx-2'" color="transparent" elevation="0">
                        <v-layout justify-center column align-center>
                          <v-card-text class="title font-weight-bold primary--text">{{ stack.name }}</v-card-text>
                          <v-img :src="stack.logo" :alt="stack.name" class="small-logo"></v-img>
                          <h4 class="subheading white--text font-weight-thin mt-5">{{ stack.text }}</h4>
                          <v-row align="center" justify="center" class="mt-5">
                            <v-slide-x-reverse-transition hide-on-leave>
                              <span :class="hover ? 'tertiary--text ease hover-discover' : 'white--text ease'">discover</span>
                            </v-slide-x-reverse-transition>
                            <v-slide-x-transition hide-on-leave>
                              <v-icon color="tertiary" v-if="hover">arrow_right_alt</v-icon>
                            </v-slide-x-transition>
                          </v-row>
                        </v-layout>
                      </v-card>
                    </a>
                  </v-hover>
                </v-col>
              </v-row>
            </v-container>
          </v-parallax>
        </v-col>

        <v-col cols="12" style="margin-bottom: 5em">
          <v-card class="elevation-0 mt-5 mb-5" color="transparent">
            <v-card-text class="text-center display-1 font-weight-bold">
              Already secure
            </v-card-text>
            <v-row align="center" justify="center">
              <v-col cols="2">
                <v-card color="transparent" elevation="0">
                  <v-layout justify-center column align-center>
                    <v-card-text class="title font-weight-bold text-center primary--text">
                      Facebook Login
                    </v-card-text>
                    <v-img src="../assets/logos/facebook_blue.png" alt="vue" class="small-logo"></v-img>
                  </v-layout>
                </v-card>
              </v-col>
              <v-col cols="2">
                <v-card color="transparent" elevation="0">
                  <v-layout justify-center column align-center>
                    <v-card-text class="title font-weight-bold text-center primary--text">
                      Google Login
                    </v-card-text>
                    <v-img src="../assets/logos/google.png" alt="vue" class="small-logo"></v-img>
                  </v-layout>
                </v-card>
              </v-col>
              <v-col cols="2">
                <v-card color="transparent" elevation="0">
                  <v-layout justify-center column align-center>
                    <v-card-text class="title font-weight-bold text-center primary--text">
                      Email Login
                    </v-card-text>
                    <v-img src="../assets/logos/email.png" alt="vue" class="small-logo"></v-img>
                  </v-layout>
                </v-card>
              </v-col>
            </v-row>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
  import auth from "@/modules/auth";

  export default {
    name: 'Main',
    data() {
      return {
        username: auth.user.profile.first_name,
        stacks: [
          {
            name: 'Elasticsearch',
            logo: require('../assets/logos/elastic.png'),
            text: 'You know, for search — and logging, and analytics, and more',
            link: 'https://www.elastic.co/'
          },
          {
            name: 'PostgreSQL',
            logo: require('../assets/logos/postgre.png'),
            text: 'The World\'s Most Advanced Open Source Relational Database',
            link: 'https://www.postgresql.org/'
          },
          {
            name: 'Redis',
            logo: require('../assets/logos/redis.png'),
            text: 'An open source in-memory data structure store',
            link: 'https://redis.io/'
          },
          {
            name: 'Minio',
            logo: require('../assets/logos/minio.png'),
            text: 'A pioneering high performance object storage',
            link: 'https://min.io/'
          }
        ],
        greetings: false,
        translateLeft: false,
        translateUp: false,
        welcome: false,
        build: false
      }
    },
    mounted() {
      setTimeout(() => {
        this.greetings = true
      }, 500);
      setTimeout(() => {
        this.translateLeft = true
      }, 1200);
      setTimeout(() => {
        this.welcome = true
      }, 2000);
      setTimeout(() => {
        this.translateUp = true
      }, 3200);
      setTimeout(() => {
        this.build = true
      }, 3500)
    }
  }
</script>

<style scoped>
  .main{
    width: 100%;
    height: 100%
  }

  .bottom-slant {
    position: relative;
    overflow: hidden;
    z-index: 0;
    -webkit-clip-path: polygon(0 0, 100% 0, 100% 75%, 0 100%);
    clip-path: polygon(0 0, 100% 0, 100% 75%, 0 100%);
  }

  .double-slant {
    position: relative;
    overflow: hidden;
    z-index: 0;
    -webkit-clip-path: polygon(0 0, 100% 15%, 100% 80%, 0 100%);
    clip-path: polygon(0 0, 100% 15%, 100% 80%, 0 100%);
  }

  .logo {
    width: 320px;
  }

  .small-logo {
    width: 40px;
    height: 40px
  }

  .ease {
    transition: transform .3s ease-out;
  }

  .hover {
    transform: translate(0, -20px);
    transition: transform .3s ease-in-out;
  }

  .hover-discover {
    transform: translate(-10px, 0);
    transition: transform .3s ease-in-out;
  }

  .link {
    text-decoration: none;
  }

  .translate-left {
    transform: translate(-160px, 0);
    transition: transform 0.8s ease-in;
  }

  .translate-up {
    transform: translate(0, -20px);
    transition: transform .3s ease-in-out;
  }

  .appear {
    transition: visibility 0s, opacity 0.4s linear;
  }
</style>