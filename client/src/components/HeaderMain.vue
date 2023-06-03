<template>
    <div class="container">
      <vs-avatar size="40" class="avatar">
        <img src="../assets/images/sample1.png" alt="">
      </vs-avatar>
      <div class="content">
        <img src="../assets/images/logo.png">
      </div>
    </div>
  </template>
  
  <style scoped>
  .container {
    position: sticky;
    top: 0;
    height: 14vh;
    background-color: #23332599;
    color: white;
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: 0 0px 8px rgba(0, 0, 0, 0.7); /* Add shadow */
  }
  
  .avatar {
    position: absolute;
    left: 4vw;
    top: 50%;
    transform: translateY(-50%);
  }
  </style>