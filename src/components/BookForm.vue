<template>
  <div class="add-form">
    <h2>添加新图书</h2>
    <form @submit.prevent="handleSubmit">
      <div class="form-group">
        <label for="bookName">书名*</label>
        <input
          type="text"
          id="bookName"
          v-model="bookName"
          required
          placeholder="请输入书名"
        >
      </div>
      <div class="form-group">
        <label for="author">作者*</label>
        <input
          type="text"
          id="author"
          v-model="author"
          required
          placeholder="请输入作者"
        >
      </div>
      <button type="submit">添加图书</button>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'

// 表单数据
const bookName = ref('')
const author = ref('')

// 定义自定义事件（向父组件传递结果）
const emit = defineEmits(['add-success'])

// 提交表单
const handleSubmit = async () => {
  if (!bookName.value || !author.value) {
    alert('书名和作者不能为空！')
    return
  }

  try {
    const res = await axios.post('http://localhost:5000/api/books', {
      book_name: bookName.value,
      author: author.value
    })
    // 清空表单
    bookName.value = ''
    author.value = ''
    // 通知父组件添加成功（RESTX返回的是直接的图书对象）
    emit('add-success', res.data, `《${res.data.book_name}》添加成功！`)
  } catch (err) {
    alert(err.response?.data?.msg || '添加失败，请重试')
  }
}
</script>

<style scoped>
.add-form {
  background: white;
  padding: 25px;
  border-radius: 8px;
  box-shadow: 0 2px 5px rgba(0,0,0,0.1);
  margin-bottom: 40px;
  max-width: 600px;
  margin-left: auto;
  margin-right: auto;
}
.form-group {
  margin-bottom: 15px;
}
label {
  display: block;
  margin-bottom: 5px;
  color: #555;
  font-weight: bold;
}
input {
  width: 100%;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 16px;
}
button {
  background: #2c3e50;
  color: white;
  border: none;
  padding: 12px 20px;
  border-radius: 4px;
  cursor: pointer;
  font-size: 16px;
  width: 100%;
}
button:hover {
  background: #34495e;
}
</style>