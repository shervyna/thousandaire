<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-12">
        <h1>Simulation</h1>
        <hr>
        <br>
        <br>
        <alert
          v-if="showMessage"
          :message="message"
          :is-error="isErrorMessage"
        />

        <br>
        <br>
        <label>Alpha Settings</label>
        <input
          id="file"
          ref="file"
          type="file"
          @change="handleAlphaSettings()"
        >
      </div>
    </div>
    <div class="row">
      <div class="col-sm-12">
        <label>Alpha Formula</label>
        <input
          id="file"
          ref="file"
          type="file"
          @change="handleAlphaFormula()"
        >
      </div>
    </div>
    <div class="row">
      <div class="col-sm-12">
        <button
          id="simulate"
          type="button"
          class="btn btn-info btn-sm"
          @click="onSimulateAlpha(alpha)"
        >
          Simulate
        </button>
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
      alphaSettings: '',
      alphaFormula: '',
      message: '',
      showMessage: false,
      isErrorMessage: false,
    };
  },
  methods: {
    handleAlphaSettings() {
      [this.alphaSettings] = this.$refs.file.files;
    },
    handleAlphaFormula() {
      [this.alphaFormula] = this.$refs.file.files;
    },
    async simulateAlpha() {
      const formData = new FormData();
      formData.append('files[0]', this.alphaSettings);
      formData.append('files[1]', this.alphaFormula);

      try {
        await axios.post('/simulate',
          formData,
          {
            headers: {
              'Content-Type': 'multipart/form-data',
            },
          });
      } catch (err) {
        this.message = 'Error sending alpha to simulation.';
        this.showMessage = true;
        this.isErrorMessage = true;
      }
    },
    onSimulateAlpha() {
      this.simulateAlpha();
    },
  },
};
</script>

<style scoped>
label {
  margin: 1rem 2rem;
}
input {
  margin-left: 1rem;
}
#simulate {
  padding: 1rem 2rem;
  margin: 2rem;
}
</style>
