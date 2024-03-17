<script setup lang="ts">
import Title from '@/components/atomic/atoms/table/Title.vue'
import Search from '@/components/atomic/molecules/table/Search.vue'
</script>

<template>
  <div class="myTable--wrapper">
    <div class="myTable">
      <div class="myTable__header">
        <Title>Lista de medicamentos</Title>
        <Search id="myTable__search"/>
      </div>

      <div class="myTable__body">
        <table>
          <thead>
            <tr>
              <th>id</th>
              <th>Substância</th>
              <th>Laboratório</th>
              <th>Cnpj</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>1</td>
              <td>atenolol</td>
              <td>Butantan</td>
              <td>12.123.123/0001-32</td>
            </tr>
            <tr>
              <td>1</td>
              <td>atenolol</td>
              <td>Butantan</td>
              <td>12.123.123/0001-32</td>
            </tr>
            <tr>
              <td>1</td>
              <td>atenolol</td>
              <td>Butantan</td>
              <td>12.123.123/0001-32</td>
            </tr>
            <tr>
              <td>1</td>
              <td>atenolol</td>
              <td>Butantan</td>
              <td>12.123.123/0001-32</td>
            </tr>
            <tr>
              <td>1</td>
              <td>atenolol</td>
              <td>Butantan</td>
              <td>12.123.123/0001-32</td>
            </tr>
            <tr>
              <td>1</td>
              <td>atenolol</td>
              <td>Butantan</td>
              <td>12.123.123/0001-32</td>
            </tr>
            <tr>
              <td>1</td>
              <td>atenolol</td>
              <td>Butantan</td>
              <td>12.123.123/0001-32</td>
            </tr>
            <tr>
              <td>1</td>
              <td>atenolol</td>
              <td>Butantan</td>
              <td>12.123.123/0001-32</td>
            </tr>
          </tbody>
          <tfoot></tfoot>
        </table>
      </div>
    </div>
  </div>
</template>

<style scoped>
.myTable--wrapper {
  display: flex;
  justify-content: center;
  align-items: center;
  padding-top: var(--padding-lg);
}

.myTable {
  width: 80%;
  display: flex;
  flex-direction: column;
  gap: var(--padding-md);

  .myTable__header {
    display: flex;
    justify-content: space-between;
  }

  .myTable__body {
    table {
      width: 100%;

      th, td {
        text-align: center;
      }
    }
  }
}
</style>