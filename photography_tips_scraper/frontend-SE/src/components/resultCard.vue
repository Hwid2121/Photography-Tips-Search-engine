<template>
    <v-card width="auto">

        <v-card-item class="d-flex p-2">
          <a :href="result.link" class="no-link"> <v-card-title>{{ result.title }}</v-card-title> 
        <v-card-subtitle>{{ result.link }}</v-card-subtitle> </a>
          <v-card-text>{{  result.snippet }}</v-card-text>
        </v-card-item>
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
  