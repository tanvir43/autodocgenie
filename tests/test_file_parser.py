import os
from app.utils.file_parser import parse_file

def test_parse_txt():
    with open("testfile.txt", "w") as f:
        f.write("This is a test file.\nSecond line.")
    content = parse_file("testfile.txt")
    assert "Second line" in content
    os.remove("testfile.txt")