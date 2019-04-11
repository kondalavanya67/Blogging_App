<template>

    <v-dialog v-model="dialog" fullscreen hide-overlay transition="dialog-bottom-transition">
      <template v-slot:activator="{ on }">
        
            <v-btn flat outline color="primary" v-on="on" class="mx-2">
                Create Post
            </v-btn>
            
      </template>
      
      <v-card>
        <v-toolbar flat color="white">
          <v-btn icon @click="dialog = false">
            <v-icon color="primary">close</v-icon>
          </v-btn>
          
          <v-spacer></v-spacer>
       
        <v-btn outline color="primary" flat @click="dialog = false">Draft</v-btn>
        <v-btn outline color="primary" flat @click="addPost">Post</v-btn>
        
        </v-toolbar>

        <v-container class="px-5">

        <v-layout row wrap>
            <v-flex xs12 sm6 md12 lg12>
                <v-flex xs12 sm6 md6 lg6>
                   <input v-model="heading" type="text" id="title" placeholder="Untitled Post" class="title">{{heading}}
                </v-flex>
            </v-flex>
            <v-layout row>
                <v-dialog v-model="file"  width="600px">
                    <template v-slot:activator="{ on }">
                        <v-flex class="my-4 picture-box py-5" xs12 sm12 md12 lg12 v-on="on">
                            <p class="text-xs-center"><v-icon>camera_alt</v-icon>    Set Cover Photo ( displays as 760 x 300 )</p>
                        </v-flex>
                    </template>
                    <v-card>
                          <v-navigation-drawer
                            floating
                            permanent
                            stateless
                            value="true"
                            >
                            <v-list dense>
                            <v-list-tile
                                v-for="item in items"
                                :key="item.title"
                            >
                                <v-list-tile-action>
                                <v-icon>{{ item.icon }}</v-icon>
                                </v-list-tile-action>

                                <v-list-tile-content>
                                <v-list-tile-title>{{ item.title }}</v-list-tile-title>
                                </v-list-tile-content>
                            </v-list-tile>
                            </v-list>
                        </v-navigation-drawer>
                        <v-flex>
                            
                        </v-flex>
                    </v-card>
                </v-dialog>
            </v-layout>
            <v-flex lg12 md12 sm12 xs12 class="py-3">
                <ckeditor :editor="editor" v-model="editorData" :config="editorConfig"></ckeditor>
            </v-flex>
        </v-layout>

        </v-container>
   
      </v-card>
    </v-dialog>
         

</template>


<script>
import ClassicEditor from '@ckeditor/ckeditor5-build-classic';
import axios from 'axios'

export default {
    name:'Blog',
    data:()=>({
        dialog: false,
        file:false,

        items: [
          { title: 'Home', icon: 'dashboard' },
          { title: 'About', icon: 'question_answer' }
        ],
        right: null,

        heading: '',
        notifications: false,
        sound: true,
        widgets: false,
        editor: ClassicEditor,
        editorData: '',
        editorConfig: {
            // The configuration of the editor.
        }
    }),

    methods: {
        async addPost(){
            axios.post('http://localhost:8000/api/post', {
                heading: this.heading,
                content: this.editorData
            } )
            .then(
                this.dialog = false
            )
        }
    },
}
</script>


<style lang="css">
    .picture-box{
        border-style: dotted;
        height: 130px;
        cursor: pointer;
    }
    .title{
        font-size: 2.7rem!important;
        height:50px;
        border:none;
        outline:none;
    }
</style>