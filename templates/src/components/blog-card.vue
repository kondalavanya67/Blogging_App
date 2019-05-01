<template>
    <v-layout row class="mb-5">
        <v-flex xs12 sm12 md12 lg12 class="mx-auto">
            <v-card flat hover>
                <v-layout row>
                    <v-flex xs12 sm12 lg4 md3>
                        <skeleton-box
                            v-if="!loaded"
                            width="250px"
                            height="100%"
                        />
                        <v-img
                            v-if="loaded"
                            :src="blog.urlToImage"
                            height="100%"
                        ></v-img>
                    </v-flex>


                    <v-flex xs12 sm12 lg7 md9>
                        <v-card-title primary-title>
                            <div class="">
                                <skeleton-box
                                    v-if="!loaded"
                                    width="380px"
                                    height="50px"
                                />
                                <h3 v-if="loaded" class="display-1 font-weight-bold md-0">{{blog.title | truncate(60) }}</h3>

                                <v-layout row>
                                    <span class="mr-2">{{blog.author | truncate(20)}}</span>
                                    <v-icon size="7px" class="mx-2">lens</v-icon>
                                    <span class="mx-2">{{blog.post_date}}</span>
                                    <v-icon size="7px" class="mx-2">lens</v-icon>
                                    <span class="mx-2">7 Min Read</span>
                                </v-layout>

                                <div v-if="!loaded">
                                    <skeleton-box />
                                    <skeleton-box />
                                    <skeleton-box />
                                    <skeleton-box />
                                </div>
                                
                                <div v-if="loaded" class="py-4">{{blog.description | truncate(170) }}</div>

                                <v-layout row align-items-start>

                                    <!-- <v-icon size="27px">visibility</v-icon>
                                    <span class="headline">533</span> -->

                                    <!-- <v-icon size="27px" class="ml-4">thumb_up</v-icon>
                                    <span class="headline">533</span> -->

                                    <v-icon size="25px" class="mr-4 icon">share</v-icon>
                                    <v-icon size="25px" class="mr-4 icon">bookmark_border</v-icon>
                                    <v-icon v-if="this.$route.path == '/profile'" size="25px" class="mr-4 icon">delete</v-icon>

                                </v-layout>

                            </div>
                        </v-card-title>
                    </v-flex>


                    <v-flex lg1 md1>
                        <v-icon class="py-2">
                            arrow_forward
                        </v-icon>
                    </v-flex>
                </v-layout>
            </v-card>
        </v-flex>
    </v-layout>
</template>

<script>
import SkeletonBox from './SkeletonBox.vue';

export default {
    name:'BlogCard',
    components:{
        'skeleton-box':SkeletonBox
    },
    props:{
        blog:{
            author:String,
            content:String,
            post_date:String,
            heading:String,
            cover_photo:String
        }
    }
}
</script>

<style lang="css" scoped>
    .icon{
        transition: transform 0s;
    }
    .icon:hover{
        transform: scale(1.1);
        fill:blueviolet;
        color:blueviolet;
    }
    .blog-card{
        list-style-type: none;
    }
</style>