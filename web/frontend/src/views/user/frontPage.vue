
<template>
  <div id="front" class="w3-center">
    <SignIn></SignIn>
  </div>
</template>

<script>
import SignIn from "@/components/frontPage/signIn.vue";
export default {
  name: "FrontPage",
  components: {
    SignIn
  },
  mounted() {}
};
</script>

<style>
#front {
  background-image: url("../../../src/assets/images/refriger.jpg");
  background-size: contain;
  background-position: center;
  padding-top: 10%;
  max-height: 800px;
  height: 100%;
}
</style>