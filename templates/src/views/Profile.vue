<template>
  <v-container>
      <v-layout row class="mt-5 pt-5">
          <v-flex md2 lg2>
               <SideMenu v-bind:items="getProfile"/>
          </v-flex>
          <v-flex md10 lg10 class="px-3">  
          
            <div v-if="this.$store.state.tab == 'Profile'">
              <v-layout row>
                    <v-flex xs12 sm12 lg4 md3>
                        <v-img
                                :src="`http://picsum.photos/100`"
                                height="100%"
                                class="user-avatar"
                        ></v-img>
                    </v-flex>


                    <v-flex xs12 sm12 lg7 md9>
                        <v-card-title primary-title class="pl-5">
                            <h1 class="display-2 font-weight-bold md-0">John Doe</h1>
                        </v-card-title>
                    </v-flex>
                    
                </v-layout>
            </div>

            
            <div v-if="this.$store.state.tab == 'Posts'">
              <BlogCard v-for="blog in getBlogData" :key="blog.title" v-bind:blog="blog"  />
            </div>

            <div v-if="this.$store.state.tab == 'Drafts'">
              <BlogCard v-for="blog in getBlogData" :key="blog.title" v-bind:blog="blog"  />
            </div>

            <div v-if="this.$store.state.tab == 'Followers'">
              <v-list>
                <v-list-tile
                  v-for="item in items"
                  :key="item.title"
                  avatar
                >

                <v-list-tile-avatar>
                  <img :src="item.avatar" class="follower-avatart">
                </v-list-tile-avatar>
                <v-list-tile-content>
                  <v-list-tile-title v-text="item.title" class="pl-3"></v-list-tile-title>
                </v-list-tile-content>
                  
                </v-list-tile>
              </v-list>
            </div>

          <div v-if="this.$store.state.tab == 'Following'">
              <v-list>
                <v-list-tile
                  v-for="item in items"
                  :key="item.title"
                  avatar
                >

                <v-list-tile-avatar>
                  <img :src="item.avatar" class="follower-avatart">
                </v-list-tile-avatar>
                <v-list-tile-content>
                  <v-list-tile-title v-text="item.title" class="pl-3"></v-list-tile-title>
                </v-list-tile-content>
                
                </v-list-tile>
              </v-list>
            </div>

          </v-flex>
      </v-layout>
  </v-container>
</template>




<script>
import SideMenu from '../components/side-menu'
import { mapState, mapGetters } from 'vuex';

export default {
    name:'Profile',
    components:{
        SideMenu
    },
    data: () => ({
      width: 300,
      items: [
          { icon: true, title: 'Jason Oner', avatar: 'https://cdn.vuetifyjs.com/images/lists/1.jpg' },
          { title: 'Travis Howard', avatar: 'https://cdn.vuetifyjs.com/images/lists/2.jpg' },
          { title: 'Ali Connors', avatar: 'https://cdn.vuetifyjs.com/images/lists/3.jpg' },
          { title: 'Cindy Baker', avatar: 'https://cdn.vuetifyjs.com/images/lists/4.jpg' }
        ]
    }),

    async created() {
      this.$store.state.tab = 'Profile'

      var url = 'http://localhost:8000/api/profileposts/';
      var req = new Request(url)
      this.$store.state.blogData = await fetch(req)
                                    .then(function (response) {
                                      return response.json();
                                    })

    },

    computed: {
      ...mapGetters([
        'getBlogData',
        'getProfile'
      ])

    },

    
}
</script>



<style scoped>
  .v-navigation-drawer {
    transition: none !important;
  }

  .lightbox {
    box-shadow: 0 0 20px inset rgba(0, 0, 0, 0.2);
    background-image: linear-gradient(to top, rgba(0, 0, 0, 0.4) 0%, transparent 72px);
  }

  .user-avatar{
    border-radius: 50%;
  }


</style>