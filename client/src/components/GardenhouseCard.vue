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