<template>
    <v-card class="elevation-0" style="background-color: transparent">
        <v-layout row wrap justify-center>
            <v-flex xs12>
                <v-form ref="form" lazy-validation>
                    <v-layout row wrap>
                        <v-flex xs12>
                            <v-card-text class="py-0 mt-3">
                                <v-text-field
                                        :rules="[rules.emptyEmail, rules.emailNotValid, rules.emailIssue]"
                                        outline
                                        label="Email"
                                        append-icon="mail"
                                        v-model="email"
                                        required
                                ></v-text-field>
                            </v-card-text>
                        </v-flex>
                        <v-flex xs12>
                            <v-card-text class="py-0 mt-2">
                                <v-text-field
                                        v-model="password"
                                        :rules="[rules.emptyPassword, rules.incorrectPassword]"
                                        :append-icon="showPassword ? 'visibility_off' : 'visibility'"
                                        :type="showPassword ? 'text' : 'password'"
                                        name="input-10-1"
                                        label="Password"
                                        outline
                                        @click:append="showPassword = !showPassword"
                                        required
                                ></v-text-field>
                            </v-card-text>
                        </v-flex>
                    </v-layout>
                </v-form>
            </v-flex>
            <v-flex xs11>
                <v-btn color="secondary" block class="login mt-5" @click="validate()">Log in</v-btn>
            </v-flex>
        </v-layout>
    </v-card>
</template>

<script>
    import auth from '../../../modules/auth';

    export default {
        name: "EmailLogin",
        data() {
            return {
                errorType: undefined,
                errorMessage: undefined,
                showPassword: false,
                email: undefined,
                password: '',
                rules: {
                    emptyEmail: v => !!v || 'Please enter your email',
                    emailNotValid: v => /.+@.+/.test(v) || 'This email is not valid.',
                    emptyPassword: v => !!v || 'Please enter your password.',
                    incorrectPassword: () => {
                        if (this.errorType === 'password') return this.errorMessage;
                        else return false
                    },
                    emailIssue: () => {
                        if (this.errorType === 'email') return this.errorMessage;
                        else return false
                    }
                }
            }
        },
        watch: {
            email() {
                this.$refs.form.resetValidation();
                this.errorType = undefined;
                this.errorMessage = undefined;
            },
            password() {
                if (this.errorType === 'password') {
                    this.errorType = undefined;
                    this.errorMessage = undefined
                }
            }
        },
        methods: {
            validate() {
                if (this.$refs.form.validate()) {
                    auth.loginWithEmail(this).then(() => {
                    }).catch(error => {
                        this.errorMessage = error.message;
                        if (this.errorMessage === 'Email and password don\'t match') {
                            this.errorType = 'password'
                        } else {
                            this.errorType = 'email'
                        }
                        this.$refs.form.validate()
                    })
                }
            }
        }
    }
</script>

<style scoped>
    .login {
        border-radius: 4px;
        text-transform: none !important;
    }
</style>