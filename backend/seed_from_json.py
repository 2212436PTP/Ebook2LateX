import json
from app.database import SessionLocal
from app.models import FormulaEntry

def seed_formulas():
    db = SessionLocal()
    try:
        with open('data.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            
            for item in data:
                new_formula = FormulaEntry(
                    document_id=item['document_id'],
                    latex_content=item['latex_content'],
                    order_index=item['order_index']
                )
                db.add(new_formula)
            db.commit()
        print("Đã import dữ liệu công thức từ JSON thành công!")
    except Exception as e:
        print("Lỗi:", e)
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    seed_formulas()