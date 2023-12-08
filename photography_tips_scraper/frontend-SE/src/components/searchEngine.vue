<template>
  <v-container fluid>
    <v-row>
      <!-- Main Content -->
      <v-col :md="adverts.length === 0 ? 12 : 9" xs="12" class="align-self-start mb-4">
        <v-responsive class="align-center text-center fill-height">
          <v-img height="300" src="@/assets/logo-photo.png" />
          <div class="text-body-2 font-weight-light mb-n1">Your portal for photography tips</div>
          <h1 class="text-h2 font-weight-bold">PhotoLand</h1>
          <v-tooltip text="The search engine is optimized for world of photography and tips and tricks on that.">
            <template v-slot:activator="{ props }">
              <v-chip v-bind="props" prepend-icon="mdi-information">
                What to search?
              </v-chip>
            </template>
          </v-tooltip> 
          <div class="py-14" />
          <v-row class="d-flex align-center justify-center">
            
            <v-col>
              <searchBar @search-results="updateResults" />
            </v-col>
           </v-row>
          <v-btn
            v-if="results.length!=0"
            class="mt-4"
            color=""
            dark
            @click="clearSpace"
          >
            <v-icon>mdi-close</v-icon>
            Clear
          </v-btn>

          <div class="py-14" />
          <div>
            <resultCard v-for="result in paginatedResults" :key="result.id" :result="result" class="result-card" @card-click="getCookie" />
          </div>

          <v-pagination v-if="results.length > 0" :length="totalPages" @input="changePage" v-model="currentPage" />


        </v-responsive>
      </v-col>

      <v-col v-if="adverts.length != 0" cols="12" md="3">
        <h1>Recommended for you</h1>
        <adCard v-for="result in adverts" :key="result.id" :result="result" class="result-card" />
      </v-col>      
    </v-row>

  </v-container>
</template>


<script>
import searchBar from '@/components/searchBar.vue';
import resultCard from '@/components/resultCard.vue';
import adCard from '@/components/adCard.vue';
import axios from 'axios';


export default {
  name: 'searchEngine',
  components: {
    searchBar,
    resultCard,
    adCard  
  },
  watch: {
    results(newResults) {
      if (newResults.length > 0) {
        this.getCookie();
      }

    },
  },
  data() {
    return {
      results: [],
      adverts: [],
      currentPage: 1,
      perPage: 5,
    };
  },
  mounted() {
    this.getCookie();
  },
  computed: {
    paginatedResults() {
      const startIndex = (this.currentPage - 1) * this.perPage;
      const endIndex = startIndex + this.perPage;
      return this.results.slice(startIndex, endIndex);
    },
    totalPages() {
      return Math.ceil(this.results.length / this.perPage);
    },
  },
  methods: {
    clearSpace() {
      this.results = [];
      // clear search bar 

    },
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
      const urls = this.$cookies.get('recommender-links');  
      this.error = '';
      let results = data.results;      
      this.adverts = results.filter(element => !urls.includes(element.url)).slice(0, 4);
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