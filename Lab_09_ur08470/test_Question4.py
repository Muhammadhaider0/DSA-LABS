import pytest
import hashlib
from Question4 import *

question4_testcases = [
([("temp", "data"),(98,1),(532,324)],["temp"], 10,'1d32441295f0aef25a7d89b558736ac783d63c23d0191e40dabf063547fefca9'),
([(0,1), (1,2), (42,5)], [0, 42], 1000,'1201c9a209b3c5bba0a6ac022dd80b2508653a7e89c7cd5324296ac15e28700d'),
]

def hashcode(n: int) -> str:
    return hashlib.sha256(str(n).encode('utf-8')).hexdigest()

@pytest.mark.parametrize("to_put,to_delete,size,result",question4_testcases)
def test_question3(to_put,to_delete,size,result):
    H = create_hashtable(size)
    for i in to_put:
        put(H,i[0],i[1],size)
    for i in to_delete:
        delete(H,i,size)
    assert hashcode(H) == result

