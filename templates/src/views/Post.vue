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
                        
                        <span class="mr-2 pt-1">{{blog.author}}</span>
                        <v-icon size="7px" class="mx-2 pb-3 pt-1">lens</v-icon>
                        <span class="mx-2 pt-1">{{blog.post_date}}</span>
                        <v-icon size="7px" class="mx-2 pb-3 pt-1">lens</v-icon>
                        <span class="mx-2 pt-1">{{blog.readtime}} min read</span>
                        <v-icon size="7px" class="mx-2 pb-3 pt-1">lens</v-icon>
                        <v-btn small outline color="indigo">Follow</v-btn>

                    </v-layout>


                    <!-- Icons for bookmark, share and like  -->

                    <v-layout row class="pt-5">
                        <v-flex lg1>
                            <!-- Bookmark icon -->
                            <v-icon large class="icon py-2">bookmark_border</v-icon><br/> 

                            <!-- Like icons -->
                            <v-icon large class="icon py-2" @click="favorite()">favorite_border</v-icon><br/>

                            <!-- Icons for facebook - start -->
                            <svg xmlns="http://www.w3.org/2000/svg" x="0px" y="0px"  
                                width="35" height="35"
                                viewBox="0 0 24 24"
                                class="my-2 icon"
                            >    
                                <path d="M17.525,9H14V7c0-1.032,0.084-1.682,1.563-1.682h1.868v-3.18C16.522,2.044,15.608,1.998,14.693,2 C11.98,2,10,3.657,10,6.699V9H7v4l3-0.001V22h4v-9.003l3.066-0.001L17.525,9z"></path>
                            </svg>

                            <!-- Icons for facebook - end -->

                        </v-flex>

                        <v-flex lg11>
                            <p class="headline font-weight-light post-content px-3">{{blog.content}}</p>
                        </v-flex>
                    </v-layout>
                    
                         
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
        var url = 'http://localhost:8000/api/Blog_id/'+this.id;
        var req = new Request(url)
        this.blog = await fetch(req)
                            .then(function (response) {
                                return response.json();
                            })
    },

    methods:{
        favorite(){
            
        }
    }
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
    .icon{
        cursor: pointer;
        fill:#757575;
        transition:transform 0s;
    }
    .icon:hover{
        transform:scale(1.1);
        color:blueviolet;
        fill:blueviolet;
    }
</style>