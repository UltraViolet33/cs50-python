import pytest
from watch import parse


valid_html_tests = [
    ('<iframe src="http://www.youtube.com/embed/xvFZjo5PgG0"></iframe>',
     "https://youtu.be/xvFZjo5PgG0"),
    ('<iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>', "https://youtu.be/xvFZjo5PgG0")
]

invalid_html_tests = [
    ('<iframe src="http://www.youtube.com/embed/xvFZjo5PgG0"</iframe>',
     None),
    ('<iframe width="560" height="315" src="hts://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>', None)

]


@pytest.mark.parametrize("test_input,expected", valid_html_tests)
def test_valid_html_parse(test_input, expected):
    assert parse(test_input) == expected


@pytest.mark.parametrize("test_input,expected", invalid_html_tests)
def test_invalid_html_parse(test_input, expected):
    assert parse(test_input) == expected
