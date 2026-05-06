import random
from faker import Faker
from app.database import SessionLocal
from app.models import User, Document

fake = Faker()

def seed_users_and_docs():
    db = SessionLocal()
    try:
        for _ in range(50):
            # Tạo User giả
            new_user = User(
                username=fake.user_name(),
                email=fake.email(),
                password_hash="hashed_password",
                full_name=fake.name()
            )
            db.add(new_user)
            db.commit()
            db.refresh(new_user)
            
            # Tạo 2-5 Document ngẫu nhiên cho User này
            num_docs = random.randint(2, 5)
            for _ in range(num_docs):
                new_doc = Document(
                    file_name=fake.file_name(extension='pdf'),
                    user_id=new_user.id
                )
                db.add(new_doc)
            db.commit()
        print("Đã tạo xong 50 người dùng và tài liệu ngẫu nhiên!")
    except Exception as e:
        print("Lỗi:", e)
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    seed_users_and_docs()