<template>
    

</template>


<script>

export default {
    name: 'reccomenderBar',
    data() {
        return {
            reccomendations: [],
        };
    },
    methods: {
    updateResults(newResults) {
      this.reccomendations = newResults;
    },
    setCookie() {
      this.$cookies.set('reccomender', [] , '3d');
    },
    getCookie() {
      const userToken = this.$cookies.get('reccomender');
      if (userToken) {
        console.log('User Token:', userToken);
        
      } else {
        console.log('Token not found');
      }
    },
    deleteCookie() {
      this.$cookies.remove('reccomender');
    },
    }
}
</script>