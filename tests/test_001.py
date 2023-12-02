from codigo.puzzle_001 import remove_letters
import pytest

# values to test ['2qlljdqcbeight', 'eight47srvbfive', 'slconeightfoureight557m38', 'xvqeightwosixnine61eightsn2tdczfhx', 'msixonexch1twokjbdlhchqk1', '112ninejlhhjmjzkzgdsix', '6six7jr', '878eightgvsqvzfthree', '2jxzhlkhdktxfjjleightdfpgfxjv', 'mxbzgzg5three']
# result = [22, 47, 58, 62, 11, 12, 67, 88, 22, 55]


@pytest.fixture(
    params=[
        ('2qlljdqcbeight', 22),
        ('eight47srvbfive', 47),
        ('slconeightfoureight557m38', 58),
        ('xvqeightwosixnine61eightsn2tdczfhx', 62),
        ('msixonexch1twokjbdlhchqk1', 11),
        ('112ninejlhhjmjzkzgdsix', 12),
        ('6six7jr', 67),
        ('878eightgvsqvzfthree', 88),
        ('2jxzhlkhdktxfjjleightdfpgfxjv', 22),
        ('mxbzgzg5three', 55)
    ]
)
def test_001_digits(request):
    assert remove_letters(request.param[0]) == request.param[1]

