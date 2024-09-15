import pytest
import hashlib
from sys import stderr
from Question1 import *

question1_testcases = [
([54, 26, 93, 17, 77, 31, 44, 55, 20], 0, 8, 'fafc7bc58a57966d3f2a2c30e7931f83be490a6e2c8932221ef579a44bd0c4cf'),
(["Aisha", "Nadia", "Waqar", "Saleha", "Hasan", "Shahid", "Shah Jamal", "Abdullah", "Umair", "Taj"], 0, 9, 'a98d2a83ec02958fb62dbbbcb5f374dbffe9b9b6c6bbb3b7c19bb4c8cc93056e'),
([4, 1, 3, 9, 7], 0, 4, 'a62d929bb92007821e130bddda37e1f68346032b2dcf30437c48f226c3cb4bd3'),
([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 0, 9, '8edb1463a317ef28e543c743ea23665c11e0a5a7bcf3f771ad76becc19145269'),
([12, 8, -6, 2, 4, 5, 3, 7, 4, 2], 0, 9, '63d46bd820696eecb6c46f599c129d88042bfcefc09763ea0da922832f740ded'),
(["FunForFun", "Practice.FunForFun", "FunforFun"], 0, 2, '3ee3c707d2bd6462a50283d3414b5d5cd0d87e62b4afc9a9b8d5803e889508b7'),
([37, 23, 0, 17, 12, 72, 31, 46, 100, 88, 54], 0, 10, '6374040206781eb4fc0df0c0840b90daea30b0910ff50f137f9239085ce08b36'),
]   

def hashcode(n: int) -> str:
    return hashlib.sha256(str(n).encode('utf-8')).hexdigest()

@pytest.mark.parametrize("lst,low,high,result",question1_testcases)
def test_question1(capsys, lst, low, high, result):
    quick_sort(lst, low, high)
    captured, _ = capsys.readouterr()
    assert hashcode(captured[:-1]) == result