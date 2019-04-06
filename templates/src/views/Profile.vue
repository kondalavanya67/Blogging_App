<template>
  <v-container>
      <v-layout row class="mt-5 pt-5">
          <v-flex md2 lg2>
               <SideMenu v-bind:items="profile"/>
          </v-flex>
          <v-flex md10 lg10>

          </v-flex>
      </v-layout>
  </v-container>
</template>


<script>
import SideMenu from '../components/side-menu'

export default {
    name:'Profile',
    components:{
        SideMenu
    },
    data: () => ({
      width: 300,
      profile:[
          {title:'Profile'},
          {title:'Posts'},
          {title:'Likes'},
          {title:'Bookmarks'},
          {title:'Followers'},
          {title:'Following'},
      ]
    })
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
</style>