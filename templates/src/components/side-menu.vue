<template>
    <div>
      <v-navigation-drawer permanent>
            <v-list class="pt-0 pl-2">
                <v-flex  v-for="item in items" :key="item.title" @click="showProfile()">
                    <p class="headline font-weight-bold">{{ item.title }}</p>
                </v-flex>
            </v-list>
        </v-navigation-drawer>  
    </div>
</template>

<script>
export default {
    name:'SideMenu',
    props:{
      items:Array
    },
    data () {
      return {
        right: null
      }
    }
}
</script>

<style lang="css">
  .route{
    cursor:pointer;
  }
</style>