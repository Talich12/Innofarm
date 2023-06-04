<template>
<vs-card @click="onRoute()" type="4">
    <template #title>
      <h3><slot name="title"></slot></h3>
    </template>
    <template #img>
          <slot name="img"></slot>
      </template>
    <template #text>
      <p>
        <slot name="text"></slot>
      </p>
    </template>
  </vs-card>
</template>

<script>
export default {
  name: "index",
  props:['id'],
  data() {
      return {

      };
  },
  methods:{
    onRoute(){
      this.$router.push('/gardenhouse/' + this.$props.id)
    }
  }
}
</script>

<style>
  .vs-card-content.type-4 .vs-card {
    box-shadow: 8px 14px 16px rgba(0, 0, 0, 0.25);
  }
</style>