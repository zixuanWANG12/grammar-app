#!/usr/bin/env python3
"""Extract text from scanned PDFs using pymupdf + tesseract OCR."""
import pymupdf, subprocess, tempfile, os, sys
from pathlib import Path

BOOKS = [
    ("趣味英语语法 第1册", "/Users/a123/广州大学/小论文工作空间文献/趣味英语语法 第1册 ( etc.) (z-library.sk, 1lib.sk, z-lib.sk).pdf"),
    ("趣味英语语法 第2册", "/Users/a123/广州大学/小论文工作空间文献/趣味英语语法 第2册 ( etc.) (z-library.sk, 1lib.sk, z-lib.sk).pdf"),
    ("趣味英语语法 第3册", "/Users/a123/广州大学/小论文工作空间文献/趣味英语语法 第3册 ( etc.) (z-library.sk, 1lib.sk, z-lib.sk).pdf"),
    ("趣味英语语法 第4册", "/Users/a123/广州大学/小论文工作空间文献/趣味英语语法 第4册 ( etc.) (z-library.sk, 1lib.sk, z-lib.sk).pdf"),
]
OUT_DIR = "/Users/a123/grammar-app"

def ocr_image(img_path):
    """Run tesseract OCR on an image file, return text."""
    try:
        r = subprocess.run(
            ["tesseract", img_path, "stdout", "-l", "chi_sim+eng", "--psm", "6"],
            capture_output=True, text=True, timeout=30
        )
        return r.stdout.strip()
    except Exception as e:
        return f"[OCR Error: {e}]"

def extract_book(name, pdf_path, out_path):
    print(f"\n{'='*60}")
    print(f"处理: {name}")
    print(f"{'='*60}")
    doc = pymupdf.open(pdf_path)
    total = len(doc)
    print(f"总页数: {total}")
    
    all_text = []
    for i in range(total):
        page = doc[i]
        # Try direct text extraction first
        text = page.get_text().strip()
        
        if len(text) > 20:
            # Has real text
            all_text.append(f"=== 第{i+1}页 (文字) ===\n{text}")
            if i % 10 == 0:
                print(f"  第{i+1}/{total}页: 文字模式 ({len(text)}字符)")
        else:
            # OCR needed - render page as image
            if i % 5 == 0:
                print(f"  第{i+1}/{total}页: OCR识别中...")
            
            # Render page at 300 DPI
            pix = page.get_pixmap(dpi=200)
            img_bytes = pix.tobytes("png")
            
            # Save temp image and OCR
            with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as f:
                f.write(img_bytes)
                tmp_path = f.name
            
            ocr_text = ocr_image(tmp_path)
            os.unlink(tmp_path)
            
            if ocr_text:
                all_text.append(f"=== 第{i+1}页 (OCR) ===\n{ocr_text}")
            else:
                all_text.append(f"=== 第{i+1}页 (空) ===\n[无文字内容]")
    
    doc.close()
    
    # Write output
    content = "\n\n".join(all_text)
    Path(out_path).write_text(content, encoding="utf-8")
    lines = content.count("\n")
    chars = len(content)
    print(f"\n✅ 完成: {out_path}")
    print(f"   行数: {lines}, 字符数: {chars}")

if __name__ == "__main__":
    for name, pdf_path in BOOKS:
        out_path = os.path.join(OUT_DIR, f"{name}.txt")
        extract_book(name, pdf_path, out_path)
    print("\n🎉 全部完成!")
