<template>
  <v-text-field
    clearable
    label="Search"
    prepend-icon="mdi-magnify"
    variant="outlined"
    v-model="search"
    @keyup.enter="searchData"
  ></v-text-field>

  <p v-if="error">{{ error }}</p>
</template>

<script>
import axios from 'axios';

export default {
  name: 'searchBar',
  data() {
    return {
      search: '',
      error: '',
    };
  },
  emits: ['search-results'], // Declare the emitted event here
  methods: {
    async searchData() {
      try {

        let query = this.search.trim().replace(/\s+/g, '+');
        if(query == '') {
          this.error = 'Please enter a search query.';
          return;
        }
        // const query = this.parseQuery(this.search);
        const response = await axios.get('http://localhost:8000/search?query=' + query);
        // this.handleSuccess(response.data);
        console.log(response.data);
      } catch (error) {
        this.handleError(error);
      }
    },
    parseQuery(query) {
      return query.trim().replace(/\s+/g, '+');
    }, 
    handleSuccess(data) {
      this.error = '';
      this.$emit('search-results', data);
    },
    handleError(error) {
      console.error('Error fetching data:', error);
      this.error = 'Error fetching data. Please try again.';
    },
  },
};
</script>
