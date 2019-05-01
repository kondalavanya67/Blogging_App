import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)


axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'

export const store = new Vuex.Store({
  state: {
    authUser: {},
    isAuthenticated: false,
    jwt: localStorage.getItem('t'),
    endpoints: {
      obtainJWT: 'http://localhost:8000/auth/obtain_token/',
      refreshJWT: 'http://localhost:8000/auth/refresh_token/'
    },

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

    feed: 'Technology',

    profile:[
      {title:'Profile'},
      {title:'Posts'},
      {title:'Drafts'},
      {title:'Likes'},
      {title:'Bookmarks'},
      {title:'Followers'},
      {title:'Following'},
   ],

    topics: null,
    tab:null
  },


  getters:{
    getInterest: state => state.interests,

    getTags: state => state.tags,

    getBlogData: state => state.blogData,

    getTopics: state => state.topics
  },


  mutations: {
    updateBlogData(state,prop){
      state.blogData = prop;
    },
    updateTab(state, value){
      state.tab = value
    },
    setAuthUser(state, {
      authUser,
      isAuthenticated
    }) {
      Vue.set(state, 'authUser', authUser)
      Vue.set(state, 'isAuthenticated', isAuthenticated)
    },
    updateToken(state, newToken) {
      // TODO: For security purposes, take localStorage out of the project.
      localStorage.setItem('token', newToken);
      state.jwt = newToken;
    },
    removeToken(state) {
      // TODO: For security purposes, take localStorage out of the project.
      localStorage.removeItem('token');
      state.jwt = null;
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
      
      },

     
      
    }
})
