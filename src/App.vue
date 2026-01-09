<template>
  <div class="app-container">
    <h1>📚 图书管理系统</h1>
    <BookForm @add-success="handleAddSuccess" />
    <BookList 
      :books="books" 
      :success-msg="successMsg" 
      @close-msg="successMsg = ''"
      @delete-book="handleDeleteBook"
    />
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import BookForm from './components/BookForm.vue'
import BookList from './components/BookList.vue'
import axios from 'axios'

// 响应式数据
const books = ref([])
const successMsg = ref('')

// 页面加载时获取图书列表
const fetchBooks = async () => {
  try {
    // RESTX返回的是直接的图书数组（无外层code/data）
    const res = await axios.get('http://localhost:5000/api/books')
    books.value = res.data  // 直接赋值，无需res.data.data
  } catch (err) {
    console.error('获取图书失败：', err)
  }
}

onMounted(() => {
  fetchBooks()
})

// 处理添加成功事件
const handleAddSuccess = (newBook, msg) => {
  books.value.push(newBook)
  successMsg.value = msg
  // 3秒后自动关闭提示
  setTimeout(() => successMsg.value = '', 3000)
}

// 处理删除图书事件
const handleDeleteBook = async (bookId) => {
  try {
    const res = await axios.delete(`http://localhost:5000/api/books/${bookId}`)
    successMsg.value = res.data.msg
    // 重新获取图书列表
    fetchBooks()
    // 3秒后自动关闭提示
    setTimeout(() => successMsg.value = '', 3000)
  } catch (err) {
    alert(err.response?.data?.msg || '删除失败，请重试')
  }
}
</script>

<style scoped>
.app-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
}
h1 {
  color: #333;
  text-align: center;
  margin: 30px 0;
  border-bottom: 2px solid #2c3e50;
  padding-bottom: 10px;
}
</style>