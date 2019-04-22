<template>
    <v-container class="mt-5">
        <v-layout row class="mt-5">
            <v-flex xs12 sm12 md12 lg12>
                <v-img :src="blog.cover_photo"></v-img>
                <div class="px-5 py-4">
                    <h1 class="display-2 font-weight-bold" style="font-family: 'Montserrat', sans-serif!important;">{{blog.heading}}</h1><br/>
                    <v-layout row>
                        <!-- <v-flex md1 lg1>
                            <v-list-tile-avatar>
                                <img src="https://cdn.vuetifyjs.com/images/lists/2.jpg">
                            </v-list-tile-avatar>
                        </v-flex>
                        <v-flex md11 lg11>
                            <span class="mr-2">John Doe</span>
                            <v-icon size="7px" class="mx-2 pb-1">lens</v-icon>
                            <span class="mx-2">24 Mar'2019</span>
                            <v-icon size="7px" class="mx-2 pb-1">lens</v-icon>
                            <span class="mx-2">7 Min Read</span>
                        </v-flex> -->
                        <v-list-tile-avatar>
                            <img src="https://cdn.vuetifyjs.com/images/lists/2.jpg">
                        </v-list-tile-avatar>
                        
                        <span class="mr-2 pt-1">{{blog.author.username}}</span>
                        <v-icon size="7px" class="mx-2 pb-3 pt-1">lens</v-icon>
                        <span class="mx-2 pt-1">{{blog.post_date}}</span>
                        <v-icon size="7px" class="mx-2 pb-3 pt-1">lens</v-icon>
                        <span class="mx-2 pt-1">7 Min Read</span>
                        <v-icon size="7px" class="mx-2 pb-3 pt-1">lens</v-icon>
                        <v-btn small outline color="indigo">Follow</v-btn>

                    </v-layout>

                    <p class="pt-5 headline font-weight-light post-content">{{blog.content}}</p>
                         
                </div>
            </v-flex>
        </v-layout>
    </v-container>
</template>

<script>

export default {
    name:'Post',
    data(){
        return{
            id: this.$route.params.id,
            interest_name: this.$route.params.interest_name,
            blog: {}
        }
    },

    async created() {
        var url = 'http://localhost:8000/api/Blog/'+this.id;
        var req = new Request(url)
        this.blog = await fetch(req)
                            .then(function (response) {
                                return response.json();
                            })
    },
}
</script>


<style lang="css">
    .post-content{
        line-height:2.7rem!important;
    }
    p.post-content::first-letter {
    font-size: 200%;
    color: #3F51B5;
    }
</style>