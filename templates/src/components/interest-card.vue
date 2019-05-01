
<template>

    <v-flex xs12 sm12 md3 lg3>
      <v-card >
        <v-card-title primary-title>
          <div>
            <div class="headline">{{topic.interest_name}} 
                <v-btn outline fab color="indigo" small>
                <v-icon>add</v-icon>
            </v-btn>
            </div>
            <span class="grey--text pr-1">{{topic.followers}} Followers</span>
          </div>
        </v-card-title>
        <v-img
          src="https://cdn.vuetifyjs.com/images/cards/sunshine.jpg"
          height="200px"
        >
        </v-img>
        
      </v-card>
    </v-flex>

</template>

<script>
  export default {
    name:'InterestCard',
    props:{
      topic:{
        interest_name:String,
        followers:Number
      }
    },
    data: () => ({
     
    })
  }
</script>