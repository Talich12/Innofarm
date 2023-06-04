<template>
    <div class="container">
      <vs-avatar size="40" class="avatar">
        <img src="../assets/images/sample1.png" alt="">
      </vs-avatar>
      <div class="content">
        <div class="image-container">
          <img src="../assets/images/logo.png">
        </div>
      </div>
    </div>
  </template>
  
  <style scoped>
  .image-container img {
    max-width: 100%;
    height: 6vh;
    margin: 0 auto;
  }
  .container {
    position: sticky;
    top: 0;
    height: 14vh;
    background-color: #23332599;
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