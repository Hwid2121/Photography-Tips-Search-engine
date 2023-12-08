<template>
  <v-container fluid>
    <v-row>
      <!-- Main Content -->
      <v-col class="fill-height">
        <v-responsive class="align-center text-center fill-height">
          <v-img height="300" src="@/assets/logo-photo.png" />
          <div class="text-body-2 font-weight-light mb-n1">Your portal for photography tips</div>
          <h1 class="text-h2 font-weight-bold">PhotoLand</h1>
          <div class="py-14" />
          <v-row class="d-flex align-center justify-center">
            <v-col>
              <searchBar @search-results="updateResults" />
            </v-col>
          </v-row>
          <div class="py-14" />

          <div>
            <resultCard v-for="result in results" :key="result.id" :result="result" class="result-card" />
          </div>
        </v-responsive>
      </v-col>

      <v-col v-if="getCookie().length !== 0" cols="3">
        <h1>Recommended for you</h1>
        <resultCard v-for="result in adverts" :key="result.id" :result="result" class="result-card" />
      </v-col>      
    </v-row>

  </v-container>
</template>


<script>
import searchBar from '@/components/searchBar.vue';
import resultCard from '@/components/resultCard.vue';
import axios from 'axios';


export default {
  name: 'searchEngine',
  components: {
    searchBar,
    resultCard,
  },
  data() {
    return {
      results: [],
      adverts: [],
    };
  },
  methods: {
    updateResults(newResults) {
      this.results = newResults;
    },

    updateReccomendations(newResults) {
      this.reccomendations = newResults;
    },
    async getCookie() {
      const userToken = this.$cookies.get('recommender');
        console.log('User Token:', JSON.stringify(userToken));

      // JSON.stringify(userToken)

        if (userToken != null) {
          const response = await axios.post('http://localhost:8000/rec', 
          {'history': JSON.stringify(userToken) })
              .then(function(result) { 
                console.log(result);
                return result;
              })
              .catch(function(error) {
                console.error(error);
              });
          this.handleSuccess(response.data);
        } else {
          console.log('Token not found');
          return [];
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
      this.adverts = results;

    },
    deleteCookie() {
      this.$cookies.remove('recommender');
    },
  },
};
</script>


<style scoped>
.result-card {
  margin-bottom: 20px;
}
</style>