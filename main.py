"""Entry for make.fun news-image-20261118.

Decodes the pre-rendered front-page image (entry.png.b64, in this
repository; the image is stored as base64 so the repo stays text-only)
and writes it to the grader output directory as entry.png.
No network, stdlib only. The output directory is MAKEFUN_OUTPUT_DIR
when set, else /output.
"""

import base64
import os
from pathlib import Path

SOURCE = Path(__file__).resolve().parent / "entry.png.b64"


def main() -> None:
    if not SOURCE.is_file():
        raise FileNotFoundError(f"entry image missing: {SOURCE}")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    # base64.b64decode is a pure function of the file bytes, so repeated
    # runs are byte-identical by construction. The decoded bytes are the
    # original JPEG (1024x1024, ~264 KB), written out as entry.png.
    data = base64.b64decode(SOURCE.read_text(encoding="ascii"))
    (out_dir / "entry.png").write_bytes(data)


if __name__ == "__main__":
    main()
