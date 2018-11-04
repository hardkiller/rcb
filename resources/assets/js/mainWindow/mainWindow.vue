<template>
  <div class="main-window">

    <h5>
       Список деталей
       <a class="fa fa-refresh cursor-pointer" @click="getPartsList()"> </a>
     </h5>

    <table class="table">
      <thead>
        <tr>
          <th>Название детали</th>
          <th>Тип детали</th>
          <th>Описание</th>
          <th>Параметры</th>
       </tr>
      </thead>
      <tbody>
        <tr v-for="part in partsList">
          <td>{{part.name}}</td>
          <td>{{part.type}}</td>
          <td>{{part.description}}</td>
          <td>{{part.parameters}}</td>
       </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
  import axios from 'axios';

  export default {
    data() {
      return {partsList: []}
    },
    methods: {
      getPartsList() {
        axios
          .get("/parts_list")
          .then(response => {
            this.partsList = response.data
          });
      }
    },
    mounted() {
      this.getPartsList();
    },
    components: {}
  }
</script>

