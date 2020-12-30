<template>
  <div>
    <b-alert
      :variant="variant"
      show
    >
      {{ message }}
    </b-alert>

    <br>
  </div>
</template>

<script>
export default {
  props: {
    message: {
      type: String,
      default: 'Welcome to Thousandaire',
    },
    isError: {
      type: Boolean,
      default: false,
    },
  },
  computed: {
    variant() {
      return this.isError ? 'danger' : 'success';
    },
  },
};
</script>
