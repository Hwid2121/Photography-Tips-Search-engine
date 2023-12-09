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


<!-- TODO: clear the query text from symbols! -->
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
        // let query = this.search.trim().replace(/\s+/g, '+');
        let query = this.search
        if(query == '') {
          this.error = 'Please enter a search query.';
          return;
        }
        // const query = this.parseQuery(this.search);
        query = query.replace(/[^\w\s]/gi, ' ');
        const response = await axios.get('http://localhost:8000/search?query=' + query);
        this.handleSuccess(response.data);
        // console.log(response.results);
      } catch (error) {
        this.handleError(error);
      }
    },
    handleSuccess(data) {
      this.error = '';
      let results = data.results;
      for (let i = 0; i < results.length; i++) {
        if (results[i].content.length > 340) {
          results[i].content = results[i].content.substring(0, 340) + '...';
        }
      }
      if (results.length == 0) {
        this.error = 'No results found for this query.';
      }
      this.$emit('search-results', results);
    },
    handleError(error) {
      console.error('Error fetching data:', error);
      this.error = 'Error fetching data. Please try again.';
    },
  },
};
</script>
