<template>
  <div class="container">
    <vs-avatar size="60" class="avatar">
      <img src="../assets/images/sample1.png" alt="">
    </vs-avatar>
    <div class="content">
      <h1 style="margin-left: 10vw; font-weight: 900;">Талалуев Денис Сергеевич</h1>
    </div>
  </div>
</template>

<style scoped>
.container {
  position: sticky;
  z-index: 10;
  top: 0;
  height: 14vh;
  background-color: #233325;
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