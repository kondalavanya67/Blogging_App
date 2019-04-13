<template>
    <v-container class="mt-5">
        <v-layout row class="mt-5">
            <v-flex xs12 sm12 md12 lg12>
                <v-img src="https://picsum.photos/350/165?random" height="350"></v-img>
                <div class="px-5 py-4">
                    <h1 class="display-2 font-weight-bold" style="font-family: 'Montserrat', sans-serif!important;">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Corrupti cupiditate</h1><br/>
                    <v-layout row>
                        <!-- <v-flex md1 lg1>
                            <v-list-tile-avatar>
                                <img src="https://cdn.vuetifyjs.com/images/lists/2.jpg">
                            </v-list-tile-avatar>
                        </v-flex>
                        <v-flex md11 lg11>
                            <span class="mr-2">John Doe</span>
                            <v-icon size="7px" class="mx-2 pb-1">lens</v-icon>
                            <span class="mx-2">24 Mar'2019</span>
                            <v-icon size="7px" class="mx-2 pb-1">lens</v-icon>
                            <span class="mx-2">7 Min Read</span>
                        </v-flex> -->
                        <v-list-tile-avatar>
                            <img src="https://cdn.vuetifyjs.com/images/lists/2.jpg">
                        </v-list-tile-avatar>
                        
                        <span class="mr-2 pt-1">John Doe</span>
                        <v-icon size="7px" class="mx-2 pb-3 pt-1">lens</v-icon>
                        <span class="mx-2 pt-1">24 Mar'2019</span>
                        <v-icon size="7px" class="mx-2 pb-3 pt-1">lens</v-icon>
                        <span class="mx-2 pt-1">7 Min Read</span>
                        <v-icon size="7px" class="mx-2 pb-3 pt-1">lens</v-icon>
                        <v-btn small outline color="indigo">Follow</v-btn>

                    </v-layout>

                    <p class="pt-5 headline font-weight-light post-content">Lorem ipsum dolor, sit amet consectetur adipisicing elit. Voluptatum quo dignissimos veniam, delectus, pariatur, quam nobis id magnam necessitatibus eveniet ex autem quia animi! Repellat cumque provident ea magnam, error optio illum aperiam, maxime nobis qui dolor vero reiciendis, culpa placeat pariatur. Doloribus rerum magnam nisi a optio iusto cupiditate odit. Commodi minima assumenda maiores odio, eveniet nulla possimus quo natus ex voluptates sint ullam doloremque excepturi. Deleniti itaque in ad, cumque maiores, omnis velit officiis quod vero et laboriosam expedita consequuntur consequatur possimus id nisi similique incidunt, natus harum eos. Temporibus ipsam et dolorem ipsa fugiat nobis quo quos accusantium neque ab iure, ad, accusamus, voluptatem suscipit. Facere, praesentium nemo? Commodi quibusdam magni aliquid exercitationem dolor odit eos, modi at aliquam ipsum eius pariatur nostrum officiis quasi rerum ducimus nihil voluptatem amet ea enim in? Id debitis, dolores dicta laudantium optio totam cupiditate. Rerum ut inventore, accusantium, facere odit veniam quasi praesentium, id voluptatum minus adipisci harum. Facilis aliquam corporis nemo aspernatur quo ipsum ad nam temporibus magnam sapiente libero iste ipsa dolore, expedita possimus a, accusantium dolores fuga laboriosam architecto totam repellendus inventore! Eligendi at voluptate sunt numquam sapiente aliquam itaque eveniet debitis. Voluptatum quisquam fuga voluptates soluta maxime aliquam ex non exercitationem, quidem dolorem deserunt id facere neque expedita! Repudiandae, modi incidunt! Eaque cum vel nihil harum? Reprehenderit hic architecto laudantium? Dignissimos molestiae modi, reprehenderit ratione nemo eligendi error consequatur a ipsa fugiat, temporibus laboriosam impedit animi dolores itaque facilis vero quod delectus pariatur. Quae voluptatum magni ex nulla, deleniti cupiditate quis saepe beatae ratione itaque harum a corporis ipsa commodi libero numquam nemo, perferendis ipsum cum aut. Consequuntur ducimus porro, deserunt suscipit inventore veniam iure non a deleniti minima corrupti odio voluptatum doloremque laboriosam accusamus aliquid voluptate labore sunt? Quisquam doloribus asperiores harum aspernatur? Repudiandae minima alias in beatae itaque incidunt temporibus, a ipsum quos, vero atque autem iure eveniet reprehenderit sapiente, tenetur officiis repellendus neque rerum eligendi architecto cumque quisquam quam. Expedita similique ea eligendi, error, inventore, quasi sint dolorem voluptates deserunt repellendus fugiat nisi? Earum quibusdam hic totam. Doloremque quam dolores voluptatibus, ducimus molestiae harum, recusandae sed minus veniam, fugit maiores nostrum omnis nesciunt vel blanditiis tempore natus a commodi temporibus eaque incidunt atque labore? Dolorem id repellendus doloremque explicabo ea odit optio recusandae modi magnam sit ad alias vero, officia, libero vitae reprehenderit harum sequi, impedit tempora aperiam quos sapiente. Distinctio dolorum sapiente blanditiis debitis nam error eos impedit delectus dolorem, expedita asperiores quis assumenda amet explicabo eaque doloremque voluptates exercitationem consequatur quasi iure beatae molestias ipsum voluptatibus. Praesentium molestias maiores neque aliquid. Aut sit tempore, nemo facere officiis ducimus qui velit excepturi dicta illo odio facilis vitae illum id possimus architecto reprehenderit, aliquid quisquam ipsam vel iste. Provident repellendus, tenetur quaerat optio nam a iste enim quos dolores nostrum suscipit beatae ullam qui temporibus velit illo quisquam. Deleniti, nobis exercitationem quasi alias dolore doloribus, ea corporis sunt assumenda repudiandae natus, ab consequuntur. Eveniet, vel! Tenetur incidunt velit asperiores odit ea nemo porro?</p>
                         
                </div>
            </v-flex>
        </v-layout>
    </v-container>
</template>

<script>
export default {
    name:'Post',
    data(){
        return{
            
        }
    }
}
</script>


<style lang="css">
    .post-content{
        line-height:2.7rem!important;
    }
    p.post-content::first-letter {
    font-size: 200%;
    color: #3F51B5;
    }
</style>