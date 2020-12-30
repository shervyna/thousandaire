<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-12">
        <h1>Alphas</h1>
        <hr>
        <br>
        <br>
        <alert
          v-if="showMessage"
          :message="message"
          :is-error="isErrorMessage"
        />
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">
                Id
              </th>
              <th scope="col">
                Author
              </th>
              <th scope="col">
                Description
              </th>
              <th scope="col">
                Alpha Setting
              </th>
              <th scope="col">
                Alpha Formula
              </th>
              <th scope="col">
                Submitted to alpha pool
              </th>
              <th scope="col" />
            </tr>
          </thead>
          <tbody>
            <tr
              v-for="(alpha, index) in alphas"
              :key="index"
            >
              <td>{{ alpha.id }}</td>
              <td>{{ alpha.author }}</td>
              <td>{{ alpha.description }}</td>
              <td>{{ alpha.settings }}</td>
              <td>{{ alpha.formula }}</td>
              <td>{{ alpha.submitted }}</td>
              <td>
                <div
                  class="btn-group"
                  role="group"
                >
                  <button
                    type="button"
                    class="btn btn-success btn-sm"
                    @click="onSubmitAlpha(alpha)"
                  >
                    Submit to Alpha pool
                  </button>
                  <button
                    type="button"
                    class="btn btn-danger btn-sm"
                    @click="onDeleteAlpha(alpha)"
                  >
                    Delete
                  </button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import Alert from './Alert.vue';

export default {
  components: {
    alert: Alert,
  },
  data() {
    return {
      alphas: [],
      message: '',
      showMessage: false,
      isErrorMessage: false,
    };
  },
  created() {
    this.getAlphas();
  },
  methods: {
    async getAlphas() {
      const path = 'http://localhost:5000/alpha';
      try {
        const res = await axios.get(path);
        this.alphas = res.data.alphas;
      } catch (error) {
        this.message = 'Error getting alphas.';
        this.showMessage = true;
        this.isErrorMessage = true;
      }
    },

    async removeAlpha(id) {
      const path = `http://localhost:5000/alpha/${id}`;
      try {
        await axios.delete(path);
        this.message = `Alpha ${id} removed!`;
        this.showMessage = true;
        this.isErrorMessage = false;
      } catch (err) {
        this.message = `Error deleting alpha ${id}`;
        this.showMessage = true;
        this.isErrorMessage = true;
      }
      this.getAlphas();
    },

    async submitAlpha(id) {
      const path = `http://localhost:5000/submit?id=${id}`;
      try {
        await axios.post(path);
        this.message = `Alpha ${id} submitted to alpha pool.`;
        this.showMessage = true;
        this.isErrorMessage = false;
      } catch (err) {
        this.message = `Error submitting alpha ${id}`;
        this.showMessage = true;
        this.isErrorMessage = true;
      }
      this.getAlphas();
    },

    onDeleteAlpha(alpha) {
      this.removeAlpha(alpha.id);
    },

    onSubmitAlpha(alpha) {
      this.submitAlpha(alpha.id);
    },
  },
};
</script>
