#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Chương trình Quản lý Công việc Hàng ngày (To-Do List)
Author: Python Developer
Date: 2025-11-16
"""

import json
import os
from datetime import datetime
from typing import List, Dict


class TodoManager:
    """Lớp quản lý danh sách công việc"""
    
    def __init__(self, filename: str = "todos.json"):
        """
        Khởi tạo TodoManager
        
        Args:
            filename: Tên file để lưu trữ dữ liệu
        """
        self.filename = filename
        self.todos: List[Dict] = []
        self.load_todos()
    
    def load_todos(self):
        """Tải danh sách công việc từ file"""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r', encoding='utf-8') as f:
                    self.todos = json.load(f)
                print(f"✓ Đã tải {len(self.todos)} công việc từ file.")
            except json.JSONDecodeError:
                print("⚠ Lỗi đọc file, khởi tạo danh sách mới.")
                self.todos = []
        else:
            print("✓ Khởi tạo danh sách công việc mới.")
            self.todos = []
    
    def save_todos(self):
        """Lưu danh sách công việc vào file"""
        try:
            with open(self.filename, 'w', encoding='utf-8') as f:
                json.dump(self.todos, f, ensure_ascii=False, indent=2)
            print("✓ Đã lưu danh sách công việc.")
        except Exception as e:
            print(f"✗ Lỗi khi lưu file: {e}")
    
    def add_todo(self, title: str, description: str = ""):
        """
        Thêm công việc mới
        
        Args:
            title: Tiêu đề công việc
            description: Mô tả chi tiết (tùy chọn)
        """
        todo = {
            'id': len(self.todos) + 1,
            'title': title,
            'description': description,
            'completed': False,
            'created_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'completed_at': None
        }
        self.todos.append(todo)
        self.save_todos()
        print(f"✓ Đã thêm công việc: '{title}'")
    
    def view_todos(self, show_completed: bool = True):
        """
        Hiển thị danh sách công việc
        
        Args:
            show_completed: Hiển thị cả công việc đã hoàn thành
        """
        if not self.todos:
            print("\n📋 Danh sách công việc trống!")
            return
        
        print("\n" + "="*70)
        print("📋 DANH SÁCH CÔNG VIỆC")
        print("="*70)
        
        incomplete_count = 0
        completed_count = 0
        
        for todo in self.todos:
            if todo['completed']:
                completed_count += 1
                if not show_completed:
                    continue
                status = "✓"
                status_text = "Hoàn thành"
            else:
                incomplete_count += 1
                status = "○"
                status_text = "Chưa hoàn thành"
            
            print(f"\n[{todo['id']}] {status} {todo['title']}")
            if todo['description']:
                print(f"    Mô tả: {todo['description']}")
            print(f"    Trạng thái: {status_text}")
            print(f"    Tạo lúc: {todo['created_at']}")
            if todo['completed_at']:
                print(f"    Hoàn thành lúc: {todo['completed_at']}")
        
        print("\n" + "-"*70)
        print(f"Tổng số: {len(self.todos)} | Chưa xong: {incomplete_count} | Đã xong: {completed_count}")
        print("="*70)
    
    def complete_todo(self, todo_id: int):
        """
        Đánh dấu công việc là hoàn thành
        
        Args:
            todo_id: ID của công việc
        """
        for todo in self.todos:
            if todo['id'] == todo_id:
                if todo['completed']:
                    print(f"⚠ Công việc '{todo['title']}' đã được hoàn thành trước đó.")
                else:
                    todo['completed'] = True
                    todo['completed_at'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    self.save_todos()
                    print(f"✓ Đã đánh dấu hoàn thành: '{todo['title']}'")
                return
        print(f"✗ Không tìm thấy công việc với ID: {todo_id}")
    
    def uncomplete_todo(self, todo_id: int):
        """
        Đánh dấu công việc là chưa hoàn thành
        
        Args:
            todo_id: ID của công việc
        """
        for todo in self.todos:
            if todo['id'] == todo_id:
                if not todo['completed']:
                    print(f"⚠ Công việc '{todo['title']}' chưa được đánh dấu hoàn thành.")
                else:
                    todo['completed'] = False
                    todo['completed_at'] = None
                    self.save_todos()
                    print(f"✓ Đã đánh dấu chưa hoàn thành: '{todo['title']}'")
                return
        print(f"✗ Không tìm thấy công việc với ID: {todo_id}")
    
    def delete_todo(self, todo_id: int):
        """
        Xóa công việc
        
        Args:
            todo_id: ID của công việc
        """
        for i, todo in enumerate(self.todos):
            if todo['id'] == todo_id:
                title = todo['title']
                self.todos.pop(i)
                # Cập nhật lại ID cho các công việc sau
                for j in range(i, len(self.todos)):
                    self.todos[j]['id'] = j + 1
                self.save_todos()
                print(f"✓ Đã xóa công việc: '{title}'")
                return
        print(f"✗ Không tìm thấy công việc với ID: {todo_id}")
    
    def delete_completed(self):
        """Xóa tất cả công việc đã hoàn thành"""
        initial_count = len(self.todos)
        self.todos = [todo for todo in self.todos if not todo['completed']]
        # Cập nhật lại ID
        for i, todo in enumerate(self.todos):
            todo['id'] = i + 1
        deleted_count = initial_count - len(self.todos)
        self.save_todos()
        print(f"✓ Đã xóa {deleted_count} công việc đã hoàn thành.")


def print_menu():
    """Hiển thị menu chính"""
    print("\n" + "="*70)
    print("           📝 QUẢN LÝ CÔNG VIỆC HÀNG NGÀY 📝")
    print("="*70)
    print("1. Thêm công việc mới")
    print("2. Xem danh sách công việc")
    print("3. Xem công việc chưa hoàn thành")
    print("4. Đánh dấu công việc hoàn thành")
    print("5. Đánh dấu công việc chưa hoàn thành")
    print("6. Xóa công việc")
    print("7. Xóa tất cả công việc đã hoàn thành")
    print("0. Thoát chương trình")
    print("="*70)


def main():
    """Hàm chính của chương trình"""
    manager = TodoManager()
    
    while True:
        print_menu()
        choice = input("\n➤ Chọn chức năng (0-7): ").strip()
        
        if choice == '1':
            print("\n--- THÊM CÔNG VIỆC MỚI ---")
            title = input("Nhập tiêu đề công việc: ").strip()
            if not title:
                print("✗ Tiêu đề không được để trống!")
                continue
            description = input("Nhập mô tả (có thể bỏ qua): ").strip()
            manager.add_todo(title, description)
        
        elif choice == '2':
            manager.view_todos(show_completed=True)
        
        elif choice == '3':
            manager.view_todos(show_completed=False)
        
        elif choice == '4':
            manager.view_todos(show_completed=False)
            try:
                todo_id = int(input("\nNhập ID công việc cần đánh dấu hoàn thành: ").strip())
                manager.complete_todo(todo_id)
            except ValueError:
                print("✗ ID không hợp lệ!")
        
        elif choice == '5':
            manager.view_todos(show_completed=True)
            try:
                todo_id = int(input("\nNhập ID công việc cần đánh dấu chưa hoàn thành: ").strip())
                manager.uncomplete_todo(todo_id)
            except ValueError:
                print("✗ ID không hợp lệ!")
        
        elif choice == '6':
            manager.view_todos(show_completed=True)
            try:
                todo_id = int(input("\nNhập ID công việc cần xóa: ").strip())
                confirm = input(f"Bạn có chắc muốn xóa công việc ID {todo_id}? (y/n): ").strip().lower()
                if confirm == 'y':
                    manager.delete_todo(todo_id)
            except ValueError:
                print("✗ ID không hợp lệ!")
        
        elif choice == '7':
            confirm = input("Bạn có chắc muốn xóa TẤT CẢ công việc đã hoàn thành? (y/n): ").strip().lower()
            if confirm == 'y':
                manager.delete_completed()
        
        elif choice == '0':
            print("\n👋 Cảm ơn bạn đã sử dụng chương trình. Hẹn gặp lại!")
            break
        
        else:
            print("✗ Lựa chọn không hợp lệ. Vui lòng chọn từ 0-7.")
        
        input("\n⏎ Nhấn Enter để tiếp tục...")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Chương trình đã bị dừng. Hẹn gặp lại!")
    except Exception as e:
        print(f"\n✗ Lỗi không mong đợi: {e}")
