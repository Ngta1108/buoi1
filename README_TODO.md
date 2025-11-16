# 📝 Chương trình Quản lý Công việc Hàng ngày (To-Do List)

Một ứng dụng dòng lệnh đơn giản và tiện lợi để quản lý công việc hàng ngày bằng Python.

## ✨ Tính năng

- ✅ **Thêm công việc mới** với tiêu đề và mô tả
- 📋 **Xem danh sách công việc** (tất cả hoặc chỉ chưa hoàn thành)
- ✓ **Đánh dấu hoàn thành** công việc
- ↺ **Đánh dấu chưa hoàn thành** công việc
- 🗑️ **Xóa công việc** đơn lẻ hoặc tất cả công việc đã hoàn thành
- 💾 **Lưu trữ tự động** vào file JSON
- 🎨 **Giao diện đẹp mắt** với emoji và màu sắc
- 📊 **Thống kê** số lượng công việc

## 📋 Yêu cầu hệ thống

- Python 3.6 trở lên
- Không cần thư viện bên ngoài (chỉ sử dụng thư viện chuẩn)

## 🚀 Cách sử dụng

### 1. Chạy chương trình

```bash
python3 todo_manager.py
```

hoặc

```bash
python todo_manager.py
```

### 2. Menu chính

Khi chạy chương trình, bạn sẽ thấy menu với các tùy chọn:

```
📝 QUẢN LÝ CÔNG VIỆC HÀNG NGÀY 📝
1. Thêm công việc mới
2. Xem danh sách công việc
3. Xem công việc chưa hoàn thành
4. Đánh dấu công việc hoàn thành
5. Đánh dấu công việc chưa hoàn thành
6. Xóa công việc
7. Xóa tất cả công việc đã hoàn thành
0. Thoát chương trình
```

### 3. Các chức năng chi tiết

#### Thêm công việc mới (1)
- Nhập tiêu đề công việc (bắt buộc)
- Nhập mô tả chi tiết (tùy chọn)
- Công việc sẽ được lưu tự động

#### Xem danh sách (2 hoặc 3)
- Tùy chọn 2: Xem tất cả công việc
- Tùy chọn 3: Chỉ xem công việc chưa hoàn thành
- Hiển thị đầy đủ thông tin: ID, tiêu đề, mô tả, trạng thái, thời gian

#### Đánh dấu hoàn thành (4)
- Nhập ID của công việc cần đánh dấu
- Thời gian hoàn thành sẽ được ghi lại tự động

#### Đánh dấu chưa hoàn thành (5)
- Nhập ID của công việc cần đánh dấu lại là chưa hoàn thành
- Hữu ích khi đánh dấu nhầm

#### Xóa công việc (6)
- Nhập ID của công việc cần xóa
- Xác nhận trước khi xóa
- ID sẽ được tự động cập nhật lại

#### Xóa tất cả công việc đã hoàn thành (7)
- Xóa hàng loạt các công việc đã hoàn thành
- Xác nhận trước khi xóa

## 💾 Lưu trữ dữ liệu

- Dữ liệu được lưu trong file `todos.json`
- File được tạo tự động khi thêm công việc đầu tiên
- Dữ liệu được lưu sau mỗi thao tác
- Có thể xem/chỉnh sửa file JSON trực tiếp nếu cần

## 📊 Cấu trúc dữ liệu

Mỗi công việc bao gồm:
- `id`: ID duy nhất
- `title`: Tiêu đề công việc
- `description`: Mô tả chi tiết
- `completed`: Trạng thái hoàn thành (true/false)
- `created_at`: Thời gian tạo
- `completed_at`: Thời gian hoàn thành (nếu có)

## 🎯 Ví dụ sử dụng

```
➤ Chọn chức năng (0-7): 1

--- THÊM CÔNG VIỆC MỚI ---
Nhập tiêu đề công việc: Học Python
Nhập mô tả (có thể bỏ qua): Hoàn thành khóa học Python cơ bản
✓ Đã thêm công việc: 'Học Python'

➤ Chọn chức năng (0-7): 2

📋 DANH SÁCH CÔNG VIỆC
======================================================================

[1] ○ Học Python
    Mô tả: Hoàn thành khóa học Python cơ bản
    Trạng thái: Chưa hoàn thành
    Tạo lúc: 2025-11-16 10:30:45

----------------------------------------------------------------------
Tổng số: 1 | Chưa xong: 1 | Đã xong: 0
======================================================================
```

## 🛠️ Tùy chỉnh

Bạn có thể tùy chỉnh:
- Tên file lưu trữ: Thay đổi tham số `filename` trong `TodoManager()`
- Định dạng hiển thị: Chỉnh sửa hàm `view_todos()`
- Thêm tính năng mới: Mở rộng class `TodoManager`

## 📝 Ghi chú

- Dữ liệu được lưu dưới dạng JSON với encoding UTF-8, hỗ trợ tiếng Việt
- Chương trình tự động xử lý lỗi và hiển thị thông báo rõ ràng
- Có thể dừng chương trình bất kỳ lúc nào với Ctrl+C

## 🤝 Đóng góp

Mọi đóng góp và góp ý đều được chào đón!

## 📄 Giấy phép

Chương trình này được phát hành dưới giấy phép MIT - bạn có thể tự do sử dụng và chỉnh sửa.

---

**Chúc bạn quản lý công việc hiệu quả! 🎉**
