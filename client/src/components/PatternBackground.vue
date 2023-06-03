<template>
    <div class="patterncontainer">
        <div class="rad"></div>
        <div class="rad-right"></div>
    </div>
</template>

<style scoped>
    .rad {
    position: fixed;
    z-index: 0;
    left: 40%;
    top: 0;
    transform: translateX(-100%);
    background-color: #49522DA8;
    width: 100vh;
    height: 100vh;
    border-radius: 50%;
    filter: blur(100px);
    opacity: 1;
  }

  .rad-right {
    position: fixed;
    z-index: 0;
    right: 40%;
    margin-top: 60vh;
    transform: translateX(100%);
    background-color: #49522DA8;
    width: 100vh;
    height: 100vh;
    border-radius: 50%;
    filter: blur(100px);
    opacity: 1;
  }
</style>