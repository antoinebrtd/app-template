<template>
  <div class="header">
    <transition name="fade" appear>
      <v-toolbar fixed class="menu-header elevation-1">
        <v-toolbar-items>
          <v-btn text class="logo" to="/home">
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
                  <v-list-item avatar>
                    <v-list-item-avatar>
                      <img :src="user.profile.picture" :alt="user.profile.name">
                    </v-list-item-avatar>

                    <v-list-item-group>
                      <v-list-item-group>{{ user.profile.name }}</v-list-item-group>
                    </v-list-item-group>
                  </v-list-item>
                </v-list>

                <v-divider></v-divider>

                <v-list>
                  <v-list-item>
                    <v-list-item-action>
                      <v-switch v-model="jobs" color="primary" class="mt-2 ml-3"></v-switch>
                    </v-list-item-action>
                    <v-list-item-group class="text-xs-right">Enable jobs</v-list-item-group>
                  </v-list-item>
                </v-list>

                <v-card-actions class="pa-3">
                  <v-spacer></v-spacer>
                  <v-btn color="grey" text @click="logout">Logout</v-btn>
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
    <v-snackbar v-model="activationReminder" :timeout="0" color="primary">
      Seems like you haven't activated your account yet!
      <v-btn text @click="resendEmail" style="text-transform: none; text-decoration: underline">Resend email</v-btn>
       <v-tooltip right>
          <template v-slot:activator="{ on }">
            <v-btn color="primary" text icon @click="activationReminder = false" v-on="on">
              <v-icon color="white">clear</v-icon>
            </v-btn>
          </template>
          <span>Close</span>
        </v-tooltip>
    </v-snackbar>
  </div>
</template>

<script>
  import axios from 'axios';
  import auth from "@/modules/auth";
  import notifications from "@/modules/notifications";

  import Jobs from './Jobs';

  export default {
    name: 'AdvancedHeader',
    components: {Jobs},
    data() {
      return {
        jobs: false,
        menu: false,
        user: auth.user,
        activationReminder: false
      }
    },
    mounted() {
      if (!this.user.profile.user_confirmed) {
        this.activationReminder = true
      }
    },
    methods: {
      logout() {
        auth.logout();
      },
      resendEmail() {
        this.activationReminder = false;
        axios.post(process.env.VUE_APP_EMAIL_AUTH_URL + '/resend-email').then( response => {
          notifications.addNotification(response.data)
        }).catch(error => {
          notifications.addNotification(error.response.data.error)
        })
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