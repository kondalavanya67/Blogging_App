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
                        </v-card-title>
                        <v-card-text>
                        <v-container grid-list-md>
                            <v-layout wrap>
                            <v-flex xs12 sm6 md4>
                                <v-text-field label="First name*" required></v-text-field>
                            </v-flex>
                            
                            <v-flex xs12 sm6 md4>
                                <v-text-field label="Last name*" required></v-text-field>
                            </v-flex>

                            <v-flex xs12>
                                <v-text-field label="Email*" required></v-text-field>
                            </v-flex>
                            <v-flex xs12>
                                <v-text-field label="Password*" type="password" required></v-text-field>
                            </v-flex>
                            <v-flex xs12 sm6>
                                <v-select
                                :items="['0-17', '18-29', '30-54', '54+']"
                                label="Age*"
                                required
                                ></v-select>
                            </v-flex>
                            <v-flex xs12 sm6>
                                <v-autocomplete
                                :items="['Skiing', 'Ice hockey', 'Soccer', 'Basketball', 'Hockey', 'Reading', 'Writing', 'Coding', 'Basejump']"
                                label="Interests"
                                multiple
                                ></v-autocomplete>
                            </v-flex>
                            </v-layout>
                        </v-container>
                        <small>*indicates required field</small>
                        </v-card-text>
                        <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn color="blue darken-1" flat @click="dialog = false">Close</v-btn>
                        <v-btn color="blue darken-1" flat @click="dialog = false">Save</v-btn>
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

export default {
    name:'Navbar',

    components:{
        Blog
    },

    data(){
        return{
            dialog: false
        }
    },

    methods: {
    }
    
}
</script>

<style> 
    .logo{
        cursor:pointer;
    }
</style>

