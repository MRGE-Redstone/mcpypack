from MCpypack.utils import Group

def test_group_is_string():
    group: Group = "group"
    assert isinstance(group, str)
