<template>
  <v-card class="mx-auto text-left" max-width="1200" elevation="5" link>
    <v-card-title>
      <a :href="result.url" class="text-h6 no-link">{{ result.title }}</a>
    </v-card-title>

    <v-card-subtitle>
      <a :href="result.url" class="subtitle-link no-link">{{ result.url }}</a>
    </v-card-subtitle>

    <v-card-text>{{ result.content }}</v-card-text>
  </v-card>
  </template>
  
  <script>
  export default {
    name: 'resultCard',
    props: {
      result: {
        type: Object,
        required: true,
      },
    },
  };
  </script>
  
  <style scoped>
  
  .no-link{
    text-decoration: none;
    color: inherit;
  }
  </style>
  