import pytest
import hashlib
from Question1 import *

question1_testcases = [
(5,'2d306edc2414f00cfbf138304485e091c84a84e0a1bcb861f8fdfe21ce9a068f'),
(15,'5b2efec98fb66f7492fbebed644dab2c268ed8c235eb0ec61eb1876bf886f676'),
(1000,'c13d5a1ba8f31a1d9d229a99cdbe20b266ed5b0e41894b953dbed8aca831b6a0'),
(0, '1391876e63685b7da0e6a923dc6c4c106590930a70cdf4665088614cae243c44')
]

def hashcode(n: int) -> str:
    return hashlib.sha256(str(n).encode('utf-8')).hexdigest()

@pytest.mark.parametrize("size,result",question1_testcases)
def test_question1(size, result):
    assert hashcode(create_hashtable(size)) == result
