from flask import Flask, request
from flask_cors import CORS
from flask_restx import Api, Resource, fields
import sqlite3
import os

# 初始化 Flask 应用
app = Flask(__name__)
CORS(app)  # 允许跨域请求
DB_FILE = "book_db.sqlite"

# 初始化 Flask-RESTX
api = Api(
    app,
    version='1.0',
    title='图书管理系统 API',
    description='基于 Flask-RESTX 的图书管理接口（含查询/添加/删除功能）',
    doc='/swagger/'  # Swagger 文档访问路径，访问 http://localhost:5000/swagger/ 即可查看
)

# 定义命名空间（接口分组）
book_ns = api.namespace('books', description='图书相关操作')

# 定义数据模型（请求/响应格式校验）
book_model = api.model('Book', {
    'book_name': fields.String(required=True, description='图书名称'),
    'author': fields.String(required=True, description='图书作者')
})

book_response_model = api.model('BookResponse', {
    'id': fields.Integer(description='图书ID'),
    'book_name': fields.String(description='图书名称'),
    'author': fields.String(description='图书作者')
})

# 数据库初始化（与原逻辑一致）
def init_db():
    if not os.path.exists(DB_FILE):
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS book (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            book_name TEXT NOT NULL,
            author TEXT NOT NULL
        );
        """)
        # 初始化测试数据
        init_data = [("三体", "刘慈欣"), ("活着", "余华"), ("解忧杂货店", "东野圭吾")]
        cursor.executemany("INSERT INTO book (book_name, author) VALUES (?, ?)", init_data)
        conn.commit()
        conn.close()
        print("数据库初始化成功")
    else:
        print("数据库已存在")

# 数据库连接工具（与原逻辑一致）
def get_db_connection():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn

# 初始化数据库
init_db()

# 接口1：查询所有图书 + 添加图书（GET/POST）
@book_ns.route('', methods=['GET', 'POST'])
class BookListAndAdd(Resource):
    # GET - 获取所有图书
    @book_ns.doc('get_all_books')
    @book_ns.response(200, '查询成功', api.model('GetBooksResponse', {
        'code': fields.Integer(default=200),
        'data': fields.List(fields.Nested(book_response_model)),
        'msg': fields.String(default='查询成功')
    }))
    def get(self):
        """获取所有图书列表"""
        conn = get_db_connection()
        books = conn.execute('SELECT id, book_name, author FROM book').fetchall()
        conn.close()
        return {
            "code": 200,
            "msg": "查询成功",
            "data": [dict(book) for book in books]
        }

    # POST - 添加新图书
    @book_ns.doc('add_book')
    @book_ns.expect(book_model, validate=True)  # 校验请求格式
    @book_ns.response(200, '添加成功', api.model('AddBookResponse', {
        'code': fields.Integer(default=200),
        'msg': fields.String,
        'data': fields.Nested(book_response_model)
    }))
    @book_ns.response(400, '参数错误')
    @book_ns.response(500, '服务器错误')
    def post(self):
        """添加新图书"""
        data = request.get_json()
        book_name = data.get('book_name')
        author = data.get('author')

        if not book_name or not author:
            return {"code": 400, "msg": "书名和作者不能为空"}, 400

        conn = get_db_connection()
        try:
            cursor = conn.execute(
                'INSERT INTO book (book_name, author) VALUES (?, ?)',
                (book_name, author)
            )
            conn.commit()
            new_book = {
                "id": cursor.lastrowid,
                "book_name": book_name,
                "author": author
            }
            return {
                "code": 200,
                "msg": f"《{book_name}》添加成功！",
                "data": new_book
            }
        except Exception as e:
            conn.rollback()
            return {"code": 500, "msg": f"添加失败：{str(e)}"}, 500
        finally:
            conn.close()

# 接口2：删除图书（DELETE）
@book_ns.route('/<int:book_id>', methods=['DELETE'])
class BookDelete(Resource):
    @book_ns.doc('delete_book', params={'book_id': '图书ID'})
    @book_ns.response(200, '删除成功', api.model('DeleteBookResponse', {
        'code': fields.Integer(default=200),
        'msg': fields.String
    }))
    @book_ns.response(404, '图书不存在')
    @book_ns.response(500, '服务器错误')
    def delete(self, book_id):
        """根据ID删除指定图书"""
        conn = get_db_connection()
        try:
            # 先检查图书是否存在
            book = conn.execute('SELECT id, book_name FROM book WHERE id = ?', (book_id,)).fetchone()
            if not book:
                return {"code": 404, "msg": f"ID为{book_id}的图书不存在"}, 404
            
            # 执行删除操作
            conn.execute('DELETE FROM book WHERE id = ?', (book_id,))
            conn.commit()
            return {
                "code": 200,
                "msg": f"《{book['book_name']}》删除成功！"
            }
        except Exception as e:
            conn.rollback()
            return {"code": 500, "msg": f"删除失败：{str(e)}"}, 500
        finally:
            conn.close()

# 注册命名空间（接口路径前缀为 /api/books）
api.add_namespace(book_ns, path='/api/books')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)