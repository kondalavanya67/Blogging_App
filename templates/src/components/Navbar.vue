<template>
    <div>
        <nav>
            <v-toolbar flat app color="white">
                <v-toolbar-title>
                <span class="font-weight-bold text-uppercase">
                    OASP
                </span>
                </v-toolbar-title>
                <v-spacer></v-spacer>
                <v-text-field
                        hide-details
                        prepend-icon="search"
                        single-line
                ></v-text-field>
                <v-btn flat color="black">Sign Up</v-btn>
                <v-btn flat color="black">Log In</v-btn>
            </v-toolbar>
        </nav>
    </div>
</template>

<script>
export default {
    name:'Navbar',
    data(){
        return{
        }
    },

    methods: {
    }
    
}
</script>

<style scoped> 

</style>

