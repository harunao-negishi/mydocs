import sys
from pathlib import Path
from pdfminer.high_level import extract_text


def main():
    if len(sys.argv) < 2:
        print("Usage: pdf_to_text.py <pdf_path> [output_txt_path]", file=sys.stderr)
        sys.exit(1)
    pdf_path = Path(sys.argv[1])
    if not pdf_path.exists():
        print(f"PDF not found: {pdf_path}", file=sys.stderr)
        sys.exit(2)
    try:
        text = extract_text(str(pdf_path))
    except Exception as e:
        print(f"Failed to extract text: {e}", file=sys.stderr)
        sys.exit(3)
    if len(sys.argv) >= 3:
        out_path = Path(sys.argv[2])
        out_path.write_text(text, encoding="utf-8")
    else:
        # Print to stdout
        print(text)


if __name__ == "__main__":
    main()
