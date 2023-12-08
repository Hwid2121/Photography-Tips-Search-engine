<template>
  <v-card class="mx-auto text-left" :href="result.url" @click="handleClick" max-width="1200" elevation="5" link>
    <v-card-title>
      {{result.title }}
    </v-card-title>

    <v-card-subtitle>
      {{result.url }}
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
    methods: {
      handleClick() {
        const history = this.$cookies.get('recommender') || [];
        let query = this.result.title.trim().replace(/\s+/g, '+');
        history.push(query);
        this.$cookies.set('recommender', history, '3d');
      
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
  