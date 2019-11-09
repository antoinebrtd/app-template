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
                                        :append-icon="showPassword ? 'visibility_off' : 'visibility'"
                                        :rules="[rules.emptyPassword, rules.nonValidPassword, rules.passwordLength]"
                                        :type="showPassword ? 'text' : 'password'"
                                        name="input-10-1"
                                        label="Password"
                                        hint="At least 8 characters"
                                        counter outline
                                        @click:append="showPassword = !showPassword"
                                        required
                                ></v-text-field>
                            </v-card-text>
                        </v-flex>
                        <v-flex xs12>
                            <v-card-text class="py-0">
                                <v-text-field
                                        :disabled="this.password.length < 8"
                                        v-model="confirmPassword"
                                        :append-icon="showConfirmPassword ? 'visibility_off' : 'visibility'"
                                        :rules="[rules.match, rules.nonValidPassword]"
                                        :type="showConfirmPassword ? 'text' : 'password'"
                                        name="input-10-1"
                                        label="Confirm password"
                                        outline
                                        @click:append="showConfirmPassword = !showConfirmPassword"
                                        required
                                ></v-text-field>
                            </v-card-text>
                        </v-flex>
                    </v-layout>
                </v-form>
            </v-flex>
            <v-flex xs11>
                <v-btn color="secondary" block class="sign-up mt-5" @click="validate()">Sign up</v-btn>
            </v-flex>
        </v-layout>
    </v-card>
</template>

<script>
    import auth from '@/modules/auth';

    export default {
        name: "EmailSignUp",
        data() {
            return {
                errorType: undefined,
                errorMessage: undefined,
                showPassword: false,
                showConfirmPassword: false,
                email: undefined,
                password: '',
                confirmPassword: '',
                rules: {
                    emptyEmail: v => !!v || 'E-mail is required',
                    emailNotValid: v => /.+@.+/.test(v) || 'E-mail must be valid',
                    emptyPassword: v => !!v || 'Password is required.',
                    passwordLength: v => v.length >= 8 || 'Min 8 characters',
                    match: v => v === this.password || "Passwords don't match",
                    nonValidPassword: () => {
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
                this.$refs.form.resetValidation()
            }
        },
        methods: {
            validate() {
                if (this.$refs.form.validate()) {
                    auth.signUpWithEmail(this).then(() => {
                    }).catch(error => {
                        this.errorMessage = error.message;
                        if (this.errorMessage === 'Password is not valid') {
                            this.errorType = 'password'
                        } else {
                            this.errorType = 'email'
                        }
                        this.$refs.form.validate()
                    });
                }
            }
        }
    }
</script>

<style scoped>
    .sign-up {
        border-radius: 4px;
        text-transform: none !important;
    }
</style>