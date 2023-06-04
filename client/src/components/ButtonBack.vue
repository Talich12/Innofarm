<template>
    <div class="bckbtn">
    <vs-button 
        color="#76816f"
        size="mini"
        circle
        icon
        floating
        @click="goBack()"
      >
        <img src="../assets/images/left.svg" style="height: 3vh; width: 3vh;">
      </vs-button>
      </div>
</template>

<script>
export default {
  methods:{
    goBack(){
      this.$router.go(-1)
    }
  }
}
</script>

<style>
    .bckbtn {
        position: absolute;
        bottom: 11vh;
        right: 3vw;
        z-index: 100;
    }
</style>