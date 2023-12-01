<template>
    <v-text-field
      clearable
      label="Search"
      prepend-icon="mdi-magnify"
      variant="outlined"
      v-model="search"
      @keyup.enter="searchData"
    ></v-text-field>
  
    <!-- Display search results -->
    <!-- <div v-if="searchResults.length">
      <ul>
        <li v-for="result in searchResults" :key="result.id">
          {{ result.name }}
        </li>
      </ul>
    </div> -->
  
    <!-- Show an error message if there's an issue -->
    <p v-if="error">{{ error }}</p>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    name: 'searchBar',
    data() {
      return {
        search: '',
        searchResults: [],
        error: '',
      };
    },
    methods: {
      async searchData() {
        try {
          const response = await axios.get(`search?query=${this.search}`);
          
          this.searchResults = response.data;
          this.error = '';
          this.$emit('search-results', this.searchResults);
        } catch (error) {
          console.error('Error fetching data:', error);
          this.error = 'Error fetching data. Please try again.'; // Display an error message
        }
      },
    },
  };
  </script>
  