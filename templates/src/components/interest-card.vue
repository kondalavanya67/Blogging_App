
<template>

    <v-flex xs12 sm12 md4 lg4>
      <v-card >
        <v-card-title primary-title>
          <div>
            <div class="headline">Top western 
                <v-btn outline fab color="indigo" small>
                <v-icon>add</v-icon>
            </v-btn>
            </div>
            <span class="grey--text pr-1">1,000 Followers</span>
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
    data: () => ({
     
    })
  }
</script>