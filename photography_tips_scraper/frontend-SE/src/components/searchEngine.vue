<template>
  <v-container class="fill-height">
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
      <resultCard v-for="result in results" :key="result.id" :result="result" />
    </v-responsive>
  </v-container>
</template>

<script>
import searchBar from '@/components/searchBar.vue';
import resultCard from '@/components/resultCard.vue';

export default {
  name: 'searchEngine',
  components: {
    searchBar,
    resultCard,
  },
  data() {
    return {
      results: [],
    };
  },
  methods: {
    updateResults(newResults) {
      this.results = newResults;
    },
  },
};
</script>
