import pytest
import hashlib
from sys import stderr
from Question3 import *

question3_testcases = [
([{"ID": "Rect1", "Length": 40, "Breadth": 25, "Color": "red"}, {"ID": "Rect2", "Length": 30, "Breadth": 20, "Color": "blue"}, {"ID": "Rect3", "Length": 70, "Breadth": 45, "Color": "green"}, {"ID": "Rect4", "Length": 20, "Breadth": 10, "Color": "purple"}],"ID",'134e975da9f7259669546e05cc1a970bf080adf2c92dc86bcad073727001aff6'),
([{"ID": "Rect1", "Length": 40, "Breadth": 25, "Color": "red"}, {"ID": "Rect2", "Length": 30, "Breadth": 20, "Color": "blue"}, {"ID": "Rect3", "Length": 70, "Breadth": 45, "Color": "green"}, {"ID": "Rect4", "Length": 20, "Breadth": 10, "Color": "purple"}],"Length",'2778aca20b3b668d7015d327d6863e4b628cf3c923b5be877d8b931c2ed3ff1d'),
([{"ID": "Rect1", "Length": 40, "Breadth": 25, "Color": "red"}, {"ID": "Rect2", "Length": 30, "Breadth": 20, "Color": "blue"}, {"ID": "Rect3", "Length": 70, "Breadth": 45, "Color": "green"}, {"ID": "Rect4", "Length": 20, "Breadth": 10, "Color": "purple"}],"Breadth",'2778aca20b3b668d7015d327d6863e4b628cf3c923b5be877d8b931c2ed3ff1d'),
([{"ID": "Rect1", "Length": 40, "Breadth": 25, "Color": "red"}, {"ID": "Rect2", "Length": 30, "Breadth": 20, "Color": "blue"}, {"ID": "Rect3", "Length": 70, "Breadth": 45, "Color": "green"}, {"ID": "Rect4", "Length": 20, "Breadth": 10, "Color": "purple"}],"Color",'c72e03a1c7a19902ec68c9246a47f2ee5557c843cdd8613c0e37a224d840f2b6')
]

def hashcode(n: int) -> str:
    return hashlib.sha256(str(n).encode('utf-8')).hexdigest()

@pytest.mark.parametrize("lst, title, result", question3_testcases)
def test_question3(capsys, lst, title, result):
    quick_sort_rectangles(lst, 0, len(lst)-1, title)
    captured, _ = capsys.readouterr()
    assert hashcode(captured[:-1]) == result