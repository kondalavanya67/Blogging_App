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
               
                <v-btn outline color="primary" flat >Sign Up</v-btn>
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
        }
    },

    methods: {
    }
    
}
</script>

<style scoped> 
    .logo{
        cursor:pointer;
    }
</style>

