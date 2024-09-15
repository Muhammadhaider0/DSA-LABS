import pytest
import hashlib
from Question3 import *

question3_testcases = [
([(0,1), (1,2), (42,5)], [0, 1, 42], 10,'cfadf50179eb6fba5b7e73da0c20aa9d347defd3139d37cf22f9770754cbef76'),
([("temp", "data"),(98,1),(532,324)],[532,"temp"], 1000,'472838407db2cbe0c8a99aa79c52445ee4cd24df7e9a8af20aa532bd14f74327'),
]

def hashcode(n: int) -> str:
    return hashlib.sha256(str(n).encode('utf-8')).hexdigest()

@pytest.mark.parametrize("to_put,to_get,size,result",question3_testcases)
def test_question3(to_put,to_get,size,result):
    H = create_hashtable(size)
    for i in to_put:
        put(H,i[0],i[1],size)
    lst = []
    for i in to_get:
        lst.append(get(H,i,size))
    assert hashcode(lst) == result
    