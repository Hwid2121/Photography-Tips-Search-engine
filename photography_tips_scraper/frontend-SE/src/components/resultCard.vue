<template>
  <v-card class="mx-auto text-left" :href="result.url" @click="handleClick" max-width="1200" elevation="5" link>


  <div>
    <v-img
      :src="takeImage()"
      height="200px"
      cover
    ></v-img>
    <v-card-title>
      {{result.title }}
    </v-card-title>

  </div>

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
      async handleClick() {
        console.log('clicked');
        const history = this.$cookies.get('recommender') || [];
        const links = this.$cookies.get('recommender-links') || [];

        let tags = this.result.article_tags;
        console.log(tags);
        tags = tags.map(tag => tag.replace(/[^a-zA-Z\s]/g, '').trim());
        let link = this.result.url;
        history.push(tags);
        links.push(link);

        if(history.length > 10) {
          history.shift();
        }
        if(links.length > 10) {
          links.shift();
        }
        this.$cookies.set('recommender-links', links, '3d');
        this.$cookies.set('recommender', history, '3d');
        this.$emit('card-click');
      },
      takeImage() {
      if (!this.result.images_url || this.result.images_url.length === 0) {
        console.warn('No images available for:', this.result.title);
        return 'https://www.example.com/default-image.jpg';
      } else {
        return this.result.images_url[0];
      }
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
  