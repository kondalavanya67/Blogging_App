import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export const store = new Vuex.Store({
  state: {

    interests:[
        {name:'Technology'}, 
        {name:'Fitness'}, 
        {name:'Health'}, 
        {name:'Art'}, 
        {name:'Business'}, 
        {name:'Food'}, 
        {name:'Gaming'},
        ],

    tags: ['html', 'css', 'vue', 'laravel', 'react', 'angular'],

    blogData: null,

    feed: 'Technology'

  },


  getters:{
    getInterest: state => state.interests,

    getTags: state => state.tags,

    getBlogData: state => state.blogData
  },


  mutations: {
    updateBlogData(state,prop){
      state.blogData = prop;
    }
  },
  
  actions: {
  
    async queryTopic({commit}, prop ){
      // var url = 'https://newsapi.org/v2/everything?' +
      //     'q=' + prop + '&'+
      //     'from=2019-04-04&' +
      //     'sortBy=popularity&' +
      //     'apiKey=ed7767f07ae745dd9a229ca0b63d3a92';

      // var req = new Request(url);
      // var dataBlog = await fetch(req)
      //                     .then(function(response) {
      //                     return response.json();
      //                 })
      var url = 'http://localhost:8000/api/Blog/'+prop;
      var req = new Request(url)
      var dataBlog = await fetch(req)
                                    .then(function (response) {
                                      return response.json();
                                    });
      commit('updateBlogData',dataBlog)
      
      }
    }
  
})
