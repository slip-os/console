<template>
  <div>
    <v-btn
      v-if="!isAuthenticated"
      to="/authentication"
    >
      Login
      <v-icon>mdi-login-variant</v-icon>
    </v-btn>
    <v-btn
      v-else
      @click.prevent="onLogout"
    >
      Logout
      <v-icon class="ml-2">mdi-logout-variant</v-icon>
    </v-btn>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'

export default {
  name: 'Account',

  data () {
    return {
      user: null
    }
  },

  computed: {
    ...mapGetters({
      isAuthenticated: 'auth/isAuthenticated',
      userCount: 'auth/userCount'
    })
  },

  methods: {
    ...mapActions({
      whoami: 'auth/whoami'
    }),

    onLogout() {
      this.$store
        .dispatch('auth/logout')
        .then(() => {
          this.$router.push('/authentication')
        })
        .catch(console.error)
    }
  },

  mounted () {
    this.whoami()
  }
}
</script>

<style scoped>

</style>
