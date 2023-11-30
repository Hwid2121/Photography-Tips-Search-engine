<template>
  <v-container class="fill-height">
    <v-responsive class="align-center text-center fill-height">
      <v-img height="300" src="@/assets/logo-photo.png" />

      <div class="text-body-2 font-weight-light mb-n1">Your portal for the photography tips</div>

      <h1 class="text-h2 font-weight-bold">PhotoLand</h1>

      <div class="py-14" />

      <v-row class="d-flex align-center justify-center">
        <v-col cols="">
          <!-- <v-btn
            color="primary"
            href="https://vuetifyjs.com/introduction/why-vuetify/#feature-guides"
            min-width="228"
            rel="noopener noreferrer"
            size="x-large"
            target="_blank"
            variant="flat"
          >
            <v-icon
              icon="mdi-speedometer"
              size="large"
              start
            />
            Search
          </v-btn> -->

          <searchBar />

        </v-col>
      </v-row>

      <div class="py-14" />
     
    </v-responsive>
  </v-container>
</template>

<script setup>
  import searchBar from '@/components/searchBar.vue'
</script>
