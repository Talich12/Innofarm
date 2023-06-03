<template>
<vs-card type="4">
    <template #title>
      <h3><slot name="title"></slot></h3>
    </template>
    <template #img>
      <img src="../assets/images/sample2.png" alt="">
    </template>
    <template #text>
      <p>
        <slot name="text"></slot>
      </p>
    </template>
  </vs-card>
</template>

<style>
  .vs-card-content.type-4 .vs-card {
    box-shadow: 8px 14px 16px rgba(0, 0, 0, 0.25);
  }
</style>