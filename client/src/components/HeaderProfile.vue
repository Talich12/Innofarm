<template>
  <div class="container">
    <vs-avatar @click="onRoute()" size="60" class="avatar">
      <img src="../assets/images/sample1.png" alt="">
    </vs-avatar>
    <div class="content" style="width: 25vw;">
      <h1 class="break-word" style="font-weight: 900;">{{ $props.name }}</h1>
    </div>
  </div>
</template>


<script>

export default {
  name: "index",
  props: ['name'],
  data() {
      return {
        Data: [],
      };
  },
  methods:{
    onRoute(){
      this.$router.push('/profile')
    }
  }
};
</script>

<style scoped>
.break-word {
  font-weight: 900;
  word-break:keep-all;
}
.container {
  position: sticky;
  z-index: 10;
  top: 0;
  height: 14vh;
  background-color: #3b513e;
  opacity: 80%;
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0px 7px 12px rgba(0, 0, 0, 0.35);
}

.avatar {
  position: absolute;
  left: 4vw;
  top: 50%;
  transform: translateY(-50%);
}
</style>