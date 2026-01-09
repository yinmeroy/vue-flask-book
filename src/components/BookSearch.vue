<template>
  <div class="search-container">
    <input
      type="text"
      v-model="keyword"
      placeholder="搜索书名或作者..."
      @keyup.enter="handleSearch"  <!-- 回车触发搜索 -->
    >
    <button @click="handleSearch">搜索</button>
    <button @click="handleReset" v-if="keyword">清空</button>
  </div>
</template>

<script setup>
import { ref } from 'vue'

// 搜索关键词
const keyword = ref('')

// 定义事件（向父组件传递搜索关键词）
const emit = defineEmits(['search'])

// 处理搜索
const handleSearch = () => {
  emit('search', keyword.value.trim())  // 传递trim后的关键词（去除首尾空格）
}

// 清空搜索
const handleReset = () => {
  keyword.value = ''
  emit('search', '')  // 传递空字符串表示取消搜索
}
</script>

<style scoped>
.search-container {
  margin: 20px 0;
  display: flex;
  gap: 10px;
  max-width: 600px;
  margin-left: auto;
  margin-right: auto;
}

input {
  flex: 1;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 16px;
}

button {
  padding: 0 20px;
  background: #2c3e50;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

button:hover {
  background: #34495e;
}

button:nth-child(3) {  /* 清空按钮样式 */
  background: #7f8c8d;
}

button:nth-child(3):hover {
  background: #6c7a7d;
}
</style>