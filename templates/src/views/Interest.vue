<template>
    <div class="interest">
        <SubNav/>
        <v-container>
            <v-layout row>
                <v-flex lg3 md3>
                    <SideMenu v-bind:items="getTopics"/>
                </v-flex>
                <v-flex lg9 md9>
                    <v-layout row wrap class="">
                        <InterestCard v-for="(i) in 6" :key="i"  class="mx-5 my-3"/>
                    </v-layout>
                </v-flex>
            </v-layout>
        </v-container>
         
    </div>
</template>

<script>
import InterestCard from '../components/interest-card'
import SideMenu from '../components/side-menu'
import SubNav from '../components/SubNav'
import { mapGetters } from 'vuex';

export default {
    name: 'Interest',

    components:{
        InterestCard,
        SideMenu,
        SubNav
    },

    data: () => ({
    }),

    computed: {
         ...mapGetters([
            'getTopics'
        ])
    },
       
    

}
</script>
