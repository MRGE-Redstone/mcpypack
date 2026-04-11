from MCpypack.utils import Experience

def test_experience_is_float():
    exp: Experience = 10.5
    assert isinstance(exp, float)
