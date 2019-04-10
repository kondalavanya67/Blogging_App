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
        <v-btn outline color="primary" flat @click="dialog = false">Post</v-btn>
        
        </v-toolbar>
        <v-container class="">
        <v-layout row wrap class="">
            <v-flex xs12 sm6 md12 lg12>
                <v-flex xs12 sm6 md6 lg6>
                    <v-text-field
                    label="Title"
                ></v-text-field>
                </v-flex>
            </v-flex>
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

export default {
    name:'Blog',
    data:()=>({
        dialog: false,
        notifications: false,
        sound: true,
        widgets: false,
        editor: ClassicEditor,
        editorData: '',
        editorConfig: {
            // The configuration of the editor.
        }
    })
}
</script>