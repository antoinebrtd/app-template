<template>
  <div class="header">
    <transition name="fade" appear>
      <v-toolbar fixed class="menu-header elevation-1">
        <v-toolbar-items>
          <v-btn flat class="logo" to="/home">
          </v-btn>
        </v-toolbar-items>
        <v-spacer></v-spacer>
        <v-toolbar-items class="pr-4" v-if="user.profile">
          <transition name="slide-x-transition" mode="out-in">
            <v-menu v-model="menu" :close-on-content-click="false" :nudge-width="300" offset-x>
              <template v-slot:activator="{ on }">
                <v-btn v-on="on" fab icon small>
                  <v-avatar :size="36">
                    <img :src="user.profile.picture" :alt="user.profile.name">
                  </v-avatar>
                </v-btn>
              </template>

              <v-card>
                <v-list>
                  <v-list-tile avatar>
                    <v-list-tile-avatar>
                      <img :src="user.profile.picture" :alt="user.profile.name">
                    </v-list-tile-avatar>

                    <v-list-tile-content>
                      <v-list-tile-title>{{ user.profile.name }}</v-list-tile-title>
                    </v-list-tile-content>
                  </v-list-tile>
                </v-list>

                <v-divider></v-divider>

                <v-list>
                  <v-list-tile>
                    <v-list-tile-action>
                      <v-switch v-model="jobs" color="primary" class="mt-2 ml-3"></v-switch>
                    </v-list-tile-action>
                    <v-list-tile-title class="text-xs-right">Enable jobs</v-list-tile-title>
                  </v-list-tile>
                </v-list>

                <v-card-actions class="pa-3">
                  <v-spacer></v-spacer>
                  <v-btn color="grey" flat @click="logout">Logout</v-btn>
                </v-card-actions>
              </v-card>
            </v-menu>
          </transition>
        </v-toolbar-items>
        <div v-else style="height: 100%;" class="pa-3">
          <v-progress-circular indeterminate></v-progress-circular>
        </div>
      </v-toolbar>
    </transition>

    <jobs v-if="jobs"></jobs>
  </div>
</template>

<script>
  import auth from "../../modules/auth/index";

  import Jobs from './Jobs';

  export default {
    name: 'AdvancedHeader',
    components: {Jobs},
    data() {
      return {
        jobs: false,
        menu: false,
        user: auth.user
      }
    },
    methods: {
      logout() {
        auth.logout();
      }
    }
  }
</script>

<style scoped>
  .logo {
    width: 221px;
    text-align: center;
    display: block;
    padding: 0;
  }

  .logo img {
    width: 221px;
  }

  .menu-header {
    z-index: 15;
  }

  .subheader-items div {
    height: 100%;
  }
</style>

<style>
  .v-toolbar__content {
    padding: 0 !important;
  }

  .v-toolbar .v-input__slot {
    background: transparent !important;
  }

  .v-content {
    padding-top: 120px !important;
  }

  .list-complete-enter, .list-complete-leave-to {
    opacity: 0;
    transform: translateX(30px);
  }

  .list-complete-leave-active {
    position: absolute;
  }
</style>
