import pytest
from bson import ObjectId

from group_q2 import create_network

@pytest.mark.parametrize("test_input,expected", [(ObjectId('5b0fc412065f3902068df21e'), [ObjectId('5b0fc410065f3902088df037'), ObjectId('5b0fc403065f39020d8de52e')]), (ObjectId('5b0fc412065f3902068df21e'), [ObjectId('5b0fc410065f3902088df037'), ObjectId('5b0fc403065f39020d8de52e')])])
def test_network(test_input, expected):
    graph = create_network()
    adj = graph.adj[test_input]
    assert list(adj) == expected