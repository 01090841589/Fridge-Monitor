<template>
  <div>
      <!-- <Loading v-if="isLoading"></Loading> -->
      <v-btn @click="loading">LoadingButton</v-btn>
  </div>
</template>

<script>

// import Loading from "@/components/LoadingPage.vue";
import { mapState, mapActions } from 'vuex';
export default {
    components:{
        // Loading
    },
    computed: {
    ...mapState(["isLoading"])
    },
    methods :{
        ...mapActions(["loading"])
    }

}
</script>

<style>

</style>