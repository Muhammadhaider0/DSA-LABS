import pytest
import hashlib
from Question2 import *

question2_testcases = [
(5, 10,'ef2d127de37b942baad06145e54b0c619a1f22327b2ebbcfbec78f5564afe39d'),
("Hello",10,'5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9'),
("Testing key",20,'e629fa6598d732768f7c726b4b621285f9c3b85303900aa912017db7617d8bdb'),
(43,1000, '44cb730c420480a0477b505ae68af508fb90f96cf0ec54c6ad16949dd427f13a')
]

def hashcode(n: int) -> str:
    return hashlib.sha256(str(n).encode('utf-8')).hexdigest()

@pytest.mark.parametrize("lst,item,result",question2_testcases)
def test_question2(lst,item,result):
    assert hashcode(hash_function(lst,item)) == result