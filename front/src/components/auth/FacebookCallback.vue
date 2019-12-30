<template>
    <div class="callback">
    </div>
</template>

<script>
    import auth from "@/modules/auth";
    import router from "@/modules/router";
    import notifications from "@/modules/notifications";

    export default {
        name: 'FacebookCallback',
        mounted() {
            const code = this.$route.query.code;
            const error = this.$route.query.error;
            if (!error) {
                auth.authorizeFacebook(this, code);
            } else if (error === 'access_denied') {
                router.replace('/')
            } else {
                notifications.addNotification('This link is invalid or has expired. Please try again');
                router.replace('/')
            }
        }
    }
</script>

<style scoped>
    .callback {
        width: 100%;
        text-align: center;
    }
</style>