# collection of tests to assert flask-empty works properly

from main import App

{%- if cookiecutter.json_friendly in ('yes', 'y') %}
def test_valid_json_():
    from json import dumps

    py_dict = {"foo": True, "bar": False, "zex": None}
    json_dict = {"foo": true, "bar": false, "zex": null}

    # equivalent
    assert dumps(py_dict) == dumps(json_dict)

    # symmetric
    for key, value in py_dict.items():
        assert json_dict.get(key) == value

    for key, value in json_dict.items():
        assert py_dict.get(key) == value

{% endif %}

