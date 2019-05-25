<template>
  <div id="app">
    <v-app>
      <advanced-header v-if="!forbiddenPath() && loaded"></advanced-header>
      <v-content v-if="loaded">
        <transition name="fade" mode="out-in">
          <router-view :key="$route.fullPath"></router-view>
        </transition>
      </v-content>
      <v-content v-else>
        <v-container class="text-xs-center">
          <v-layout justify-center>
            <v-flex>
              <v-progress-circular color="primary" indeterminate></v-progress-circular>
            </v-flex>
          </v-layout>
        </v-container>
      </v-content>
    </v-app>
  </div>
</template>

<script>
  import AdvancedHeader from '@/components/util/AdvancedHeader';
  import auth from './modules/auth';

  export default {
    name: 'App',
    watch: {
      $route: function (value, old) {
        if (old.name === null) {
          this.loaded = false;
          if (this.forbiddenPath() === false) {
            auth.checkAuth().then(() => {
              this.loaded = true;
            }).catch(() => {
              this.loaded = true;
            });
          } else {
            this.loaded = true;
          }
        }

        if (value.meta.title) {
          document.title = value.meta.title + ' - Template';
        } else {
          document.title = 'Template';
        }
      }
    },
    data() {
      return {
        loaded: false
      }
    },
    components: {
      advancedHeader: AdvancedHeader
    },
    methods: {
      forbiddenPath: function () {
        if (this.$route.name) {
          return (this.$route.name === 'login' || this.$route.name === 'callback');
        } else {
          return false;
        }
      },
    }
  }
</script>

<style>
  #app {
    min-height: 100vh;
  }

  .progress {
    text-align: center;
  }

  .fade-enter-active, .fade-leave-active {
    transition: opacity .3s;
  }

  .fade-enter, .fade-leave-to {
    opacity: 0;
  }

  .v-progress-linear.progress {
    position: fixed;
    top: 0;
    left: 0;
    margin: 0;
  }

  .theme--light.v-card .v-card__title.primary,
  .theme--light.v-card .v-card__title.warning,
  .theme--light.v-card .v-card__title.warning,
  .theme--light.v-card .v-card__title.error {
    color: white;
  }

  .background {
    position: fixed;
    top: 0;
    left: 0;
    min-height: 100%;
    min-width: 100%;
    opacity: 0.7;
  }

  .v-table__overflow {
    width: 100%;
    overflow-x: visible;
    overflow-y: visible;
  }

  .v-small-dialog__content {
    background: #232323;
  }

  table.v-table tbody td {
    font-size: 14px !important;
  }

  table.v-table thead th {
    font-size: 14px !important;
  }
</style>

<style lang="stylus">
  $font-weights := {
      thin: 100,
      light: 100,
      regular: 200,
      medium: 300,
      bold: 500,
      black: 900
  }

  $heading-font-family = 'Quicksand'
  $body-font-family = 'Montserrat'

  $body-bg-dark = '#323232'
  $body-bg-light = '#ffffff'

  @import '../node_modules/vuetify/src/stylus/main'
</style>
