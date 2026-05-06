from app.database import SessionLocal
from app.models import FormulaEntry

def search_formulas(keyword: str):
    db = SessionLocal()
    try:
        # Sử dụng ilike để tìm kiếm không phân biệt hoa thường
        results = db.query(FormulaEntry).filter(FormulaEntry.latex_content.ilike(f"%{keyword}%")).all()
        
        print(f"--- KẾT QUẢ TÌM KIẾM CHO '{keyword}' ---")
        for formula in results:
            print(f"ID: {formula.id} | LaTeX: {formula.latex_content}")
    finally:
        db.close()

if __name__ == "__main__":
    search_formulas("sqrt")