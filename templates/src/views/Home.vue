<template>
<div class="home">
  <SubNav/>
  <v-container>
    <!--  Second layout -->
    <v-layout row>
      <v-flex xs12 sm12 md12 lg8>
        <!-- {{getBlogData.articles}} -->
        <BlogCard v-for="blog in getBlogData" :key="blog.title" v-bind:blog="blog" />
        <!-- <div v-for="blog in blogData.articles" :key="blog.title">
          {{blog.urlToImage}}
        </div> -->
       
      </v-flex>
      <v-flex xs12 sm12 md12 lg4 class="px-5 pb-5">
        <h2 class="pb-3">Latest Posts</h2>
        <FeaturedBlogCard />
        <FeaturedBlogCard />
        <FeaturedBlogCard />
      
      <div class="mb-5">
        <v-chip color="primary" v-for="tag in getTags" :key="tag" text-color="white">{{tag}}</v-chip>
      </div>
        
      </v-flex>
    </v-layout> 
  </v-container>
</div>
</template>

<script>
  import FeaturedBlogCard from '../components/featured-blog-card'
  import BlogCard from '../components/blog-card'
  import SubNav from '../components/SubNav'
  import {mapGetters} from 'vuex'
  // import axios from 'axios'

  export default {
    name:'Home',
    
    components: {
     BlogCard,
     FeaturedBlogCard, 
     SubNav
    },
   
   data: ()=>({
      
    }),

    computed:{
      ...mapGetters([
        'getTags',
        'getBlogData',
      ])
    },

  async mounted(){
    var prop = this.$store.state.feed
    // var url = 'https://newsapi.org/v2/everything?' +
    //       'q=' + prop + '&'+
    //       'from=2019-03-29&' +
    //       'sortBy=popularity&' +
    //       'apiKey=ed7767f07ae745dd9a229ca0b63d3a92';

    //   var req = new Request(url);
    //   this.$store.state.blogData = await fetch(req)
    //                       .then(function(response) {
    //                       return response.json();
    //                   })
    
    var url = 'http://localhost:8000/api/Blog/'+prop;
    var req = new Request(url)
    this.$store.state.blogData = await fetch(req)
                                  .then(function (response) {
                                    return response.json();
                                  })
                                

  },

    methods: {
      // ...mapActions([
      //   'getTopicArticle'
      // ])
    },

    
  }
</script>

<style scoped> 
    .router-link-active{
        text-decoration: none;
    }
</style>
