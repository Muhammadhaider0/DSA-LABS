import pytest
import hashlib
from Question5 import *

question5_testcases = [
([("temp", "data"),(98,1),(532,324)],[532],["temp"], 10, "c76565b7367b583109cd17c16f60544c8201f619d3d5f2ef7c0d3a62c0d0f959"),
([("temp", "data"),(98,1),(532,324)],[532, 98],["temp"], 10,'a0c2f68d0692d037024c8115ad0b12b2f482d733672e515bc5943a955bfc7965'),
([(143,"some string"),("key", "value"),(4,2),(0, 65)],[143],[0, "key"], 1000,'a3b1a0202abd7bdc5f4a477d5fcfd0153b21976515ad8c041f5d6d60d443fd1b'),
]

def hashcode(n: int) -> str:
    return hashlib.sha256(str(n).encode('utf-8')).hexdigest()

@pytest.mark.parametrize("to_put, to_delete, to_get, size, result",question5_testcases)
def test_question3(to_put, to_delete, to_get, size, result):
    assert hashcode(main(to_put, to_delete, to_get, size)) == result