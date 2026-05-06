from sqlalchemy import func
from app.database import SessionLocal
from app.models import User, Document

def print_user_document_stats():
    db = SessionLocal()
    try:
        # Truy vấn kết hợp User và Document, gom nhóm theo tên User và đếm số Document
        results = db.query(User.full_name, func.count(Document.id).label('doc_count')) \
                    .outerjoin(Document, User.id == Document.user_id) \
                    .group_by(User.id).all()
        
        print("--- THỐNG KÊ TÀI LIỆU ---")
        for user_name, count in results:
            print(f"Người dùng: {user_name} - Số tài liệu: {count}")
    finally:
        db.close()

if __name__ == "__main__":
    print_user_document_stats()