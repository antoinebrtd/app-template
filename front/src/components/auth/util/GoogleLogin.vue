<template>
    <div>
        <v-btn outlined block class="login" @click="login()">
            <img src="../../../assets/google.png" alt="google-login-icon" class="google-logo">
            <v-spacer style="max-width: 8%"></v-spacer>
            Log in with Google
        </v-btn>
    </div>
</template>

<script>
    import auth from "../../../modules/auth/index";

    export default {
        name: "GoogleLogin",
        methods: {
            login() {
                auth.loginWithGoogle(this);
            }
        }
    }
</script>

<style scoped>
    .login {
        text-transform: None !important;
    }

    .google-logo {
    width: 4%;
  }
</style>