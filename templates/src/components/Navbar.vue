<template>
    <div>
        <nav>
            <v-toolbar flat app color="white">
                <v-toolbar-title>
                <span class="font-weight-bold text-uppercase">
                    <router-link class="logo" tag="span" to="/">
                        OASP
                    </router-link>
                </span>
                </v-toolbar-title>
                <v-spacer></v-spacer>
                <v-text-field
                        hide-details
                        prepend-icon="search"
                        single-line
                        class="mx-2"
                ></v-text-field>
                
                <Blog />
               

                <v-dialog v-model="dialog" persistent max-width="600px">
                    <template v-slot:activator="{ on }">
                        <v-btn outline color="primary" flat v-on="on">Sign Up</v-btn>
                    </template>
                    <v-card>
                        <v-card-title>
                        <span class="display-1 font-weight-bold pl-3">Sign Up</span>
                        <v-spacer></v-spacer>
                        <v-btn fab color="blue darken-1" flat @click="dialog = false"><v-icon>cancel</v-icon></v-btn>
                        </v-card-title>
                        <v-card-text>
                        <v-container grid-list-md>
                            <v-layout wrap>
                            <v-flex xs12>
                                <v-text-field v-model="fullName" label="Full name*" required></v-text-field>
                            </v-flex>
                            
                            <v-flex xs12>
                                <v-text-field v-model="email" label="Email*" required></v-text-field>
                            </v-flex>
                            <v-flex xs6>
                                <v-text-field v-model="password" label="Password*" type="password" required></v-text-field>
                            </v-flex>
                            <v-flex xs6>
                                <v-text-field v-model="password1" label="Confirm Password*" type="password" required></v-text-field>
                            </v-flex>
                            </v-layout>
                        </v-container>
                        <small class="pl-3">*indicates required field</small>
                        </v-card-text>
                        <v-card-actions>
                        
                        <v-btn large dark color="blue darken-1 ml-3 mb-3" flat @click="sendData">Next</v-btn>
                        <v-dialog v-model="dialog2" max-width="500px">
                            <v-card>
                                <v-card-title class="headline font-weight-bold">
                                    Please Enter Your Six Digit OTP
                                </v-card-title>
                                <v-card-text>
                                <v-flex xs6>
                                    <v-text-field v-model="otp" label="Enter OTP Here*" type="text" required></v-text-field>
                                </v-flex>
                                </v-card-text>
                                <v-card-actions>
                                <v-btn color="primary" flat @click="sendOTP">Next</v-btn>
                                </v-card-actions>
                            </v-card>
                        </v-dialog>
                        </v-card-actions>
                    </v-card>
                </v-dialog>


                <v-btn outline color="primary" flat >Log In</v-btn>

            </v-toolbar>
        </nav>
    </div>
</template>

<script>
import Blog from './Blog'
import axios from 'axios'

export default {
    name:'Navbar',

    components:{
        Blog
    },

    data(){
        return{
            dialog: false,
            dialog2: false,
            fullName: '',
            email: '',
            password: '',
            password1: '',
            otp: ''
        }
    },

    methods: {
        async sendData(){
            
            axios.post('http://localhost:8000/api/register/', {
                fullname: this.fullName,
                email: this.email,
                password: this.password,
                password1: this.password1
            })
            .then(
                this.dialog2 = true
            )
        },


        async sendOTP(){
            
            axios.post('http://localhost:8000/api/register/', {
                otp: this.otp
            })
            .then(
                this.dialog2 = false,
                this.dialog = false
            )
        }
    }
    
}
</script>

<style> 
    .logo{
        cursor:pointer;
    }
</style>

