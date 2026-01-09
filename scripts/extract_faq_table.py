import sys
from pathlib import Path

try:
    from bs4 import BeautifulSoup
except ImportError:
    print("Missing dependency: beautifulsoup4. Install it and rerun.")
    sys.exit(2)

# Optional but recommended parser
PREFERRED_PARSERS = ["lxml", "html.parser"]

ROOT = Path(__file__).resolve().parents[1]
SRC_HTML = ROOT / "docs" / "assets" / "images" / "Documentation.Calculateur.CO2_web.htm"
OUT_HTML = ROOT / "docs" / "includes" / "faq-table.html"


def load_html(path: Path) -> BeautifulSoup:
    data = path.read_text(encoding="utf-8", errors="ignore")
    for parser in PREFERRED_PARSERS:
        try:
            return BeautifulSoup(data, parser)
        except Exception:
            continue
    # Fallback
    return BeautifulSoup(data, "html.parser")


def pick_largest_table(soup: BeautifulSoup):
    tables = soup.find_all("table")
    if not tables:
        return None
    # Choose table with max <tr> count; tie-breaker by length
    def score(tbl):
        trs = tbl.find_all("tr")
        return (len(trs), len(str(tbl)))
    return max(tables, key=score)


def ensure_out_dir(path: Path):
    path.parent.mkdir(parents=True, exist_ok=True)


def main():
    if not SRC_HTML.exists():
        print(f"Source HTML not found: {SRC_HTML}")
        sys.exit(1)

    soup = load_html(SRC_HTML)
    table = pick_largest_table(soup)
    if table is None:
        print("No <table> tags found in source HTML.")
        sys.exit(1)

    # Write the table outer HTML verbatim
    ensure_out_dir(OUT_HTML)
    OUT_HTML.write_text(str(table), encoding="utf-8")

    print(f"Extracted table written to: {OUT_HTML}")


if __name__ == "__main__":
    main()
