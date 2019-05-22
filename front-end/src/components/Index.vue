<template>
  <div>
    <p>{{ msg }}</p>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'idnex',
  data() {
    return {
      msg: ''
    }
  },
  methods: {
    // 创建获取数据的方法
    getMessage() {
      const path = "http://127.0.0.1:5000/"
      axios.get(path)
      .then((response) => {
        this.msg = response.data;
      })
      .catch((error) => {
        console.error(error);
      })
      }
    },
    // 组件一调用就调用该方法
  created() {
      this.getMessage();
    }
  }
</script>

