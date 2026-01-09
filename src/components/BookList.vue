<template>
  <div class="book-list">
    <h2>图书列表</h2>
    <!-- 成功提示 -->
    <div class="success-msg" v-if="successMsg">
      {{ successMsg }}
      <button class="close-btn" @click="$emit('close-msg')">×</button>
    </div>
    <!-- 图书卡片 -->
    <div class="book-container">
      <div class="book-card" v-for="book in books" :key="book.id">
        <div class="book-id">ID: {{ book.id }}</div>
        <div class="book-name">{{ book.book_name }}</div>
        <div class="book-author">作者: {{ book.author }}</div>
        <button class="delete-btn" @click="handleDelete(book.id, book.book_name)">
          删除
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
// 接收父组件传递的参数
const props = defineProps({
  books: {
    type: Array,
    required: true
  },
  successMsg: {
    type: String,
    default: ''
  }
})

// 定义自定义事件
const emit = defineEmits(['close-msg', 'delete-book'])

// 处理删除确认（新增方法）
const handleDelete = (bookId, bookName) => {
  if (confirm(`确定要删除《${bookName}》吗？`)) {
    emit('delete-book', bookId)
  }
}
</script>

<style scoped>
.book-list {
  margin-top: 20px;
}
.book-container {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 20px;
  margin-top: 20px;
}
.book-card {
  background: white;
  border-radius: 8px;
  padding: 20px;
  box-shadow: 0 2px 5px rgba(0,0,0,0.1);
  transition: transform 0.3s;
  position: relative;
}
.book-card:hover {
  transform: translateY(-5px);
}
.book-id {
  color: #666;
  font-size: 14px;
}
.book-name {
  font-size: 20px;
  font-weight: bold;
  color: #2c3e50;
  margin: 10px 0;
}
.book-author {
  color: #7f8c8d;
  font-style: italic;
  margin-bottom: 15px;
}
.success-msg {
  color: #27ae60;
  background: #eafaf1;
  padding: 10px 15px;
  border-radius: 4px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.close-btn {
  width: auto;
  padding: 2px 8px;
  background: transparent;
  color: #27ae60;
  font-size: 16px;
}
.close-btn:hover {
  background: transparent;
  color: #219653;
}
/* 删除按钮样式（新增） */
.delete-btn {
  background: #e74c3c;
  color: white;
  border: none;
  padding: 8px 15px;
  border-radius: 4px;
  cursor: pointer;
  font-size: 14px;
  width: 100%;
  margin-top: 10px;
}
.delete-btn:hover {
  background: #c0392b;
}
</style>