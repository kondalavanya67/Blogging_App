<template>
    <v-app class="white">
      <Navbar/>
      <!-- <SubNav></SubNav> -->
      <v-content class="pt-0">
        <router-view></router-view>
      </v-content>
    </v-app>
</template>

<script>
import Navbar from './components/Navbar'
// import SubNav from './components/SubNav'


export default {
  name: 'App',
  components: {
    Navbar, 
    // SubNav
  },
  data () {
    return {
      //
    }
  }
}
</script>

