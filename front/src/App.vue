<template>
  <v-app>
    <v-app-bar
      app
      color="primary"
      dark
    >
      <div class="d-flex align-center">
        <v-btn
          to="/"
          light
        >
          Homeland console
          <v-icon class="ml-2">mdi-console</v-icon>
        </v-btn>
      </div>

      <v-spacer></v-spacer>
      <Messages/>
      <Tasks/>
      <Account/>
    </v-app-bar>api

    <v-main>
      <router-view/>
    </v-main>

    <v-footer
      padless
      color="primary lighten-1"
      vvariant="text"
    >
      <v-row
        no-gutters
        justify="center"
      >
        <v-col
          class="primary lighten-2 py-4 text-center white--text"
          cols="12"
        >{{ new Date().getFullYear() }} - <strong>Homeland.social</strong></v-col>
      </v-row>
    </v-footer>
  </v-app>
</template>

<script>
import Account from '@/components/Account.vue'
import Tasks from '@/components/Tasks.vue'
import Messages from '@/components/Messages.vue'

export default {
  name: 'App',

  components: {
    Account,
    Tasks,
    Messages,
  }
}
</script>

<style>
</style>
