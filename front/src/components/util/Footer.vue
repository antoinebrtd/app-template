<template>
    <v-footer color="transparent" padless style="width: 100%">
        <v-card flat tile class="white--text text-center" color="transparent" style="width: 100%">
            <v-card-text>
                <a v-for="link in links" :key="link.icon" :href="link.link" target="_blank" class="link">
                    <v-btn :class="white ? 'mx-4 white--text text-center' : 'mx-4 text-center'" icon>
                        <v-icon size="24px">{{ link.icon }}</v-icon>
                    </v-btn>
                </a>
            </v-card-text>
        </v-card>
    </v-footer>
</template>

<script>
    export default {
        name: "Footer.vue",
        props: {
            white: Boolean
        },
        data: () => ({
            links: [
                {icon: 'fab fa-vuejs', link: 'https://vuejs.org'},
                {icon: 'fab fa-python', link: 'http://flask.palletsprojects.com/en/1.1.x'},
                {icon: 'fab fa-github-square', link: 'https://github.com/antoinebrtd'},
                {icon: 'fab fa-linkedin', link: 'https://www.linkedin.com/in/antoine-bertrand-5906a5133/'}
            ]
        })
    }
</script>

<style scoped>
    .link {
        text-decoration: none
    }
</style>