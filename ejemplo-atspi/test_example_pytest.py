"""
Application tests using pytest.

Usage:

python3 -m pytest -s
"""


import pytest

from ipm import e2e


# Archivo ejecutable.
# El hecho de que esté hardcoded no es demasiado grave, pues lo habitual
# es tener solo una aplicación objetivo de los tests, no varias.
PATH = './example_atspi.py'


@pytest.fixture(scope='session', autouse=True)
def app():
    process, app = e2e.run(PATH)
    if app is None:
        process and process.kill()
        assert False, f"There is no aplication {PATH} in the desktop"
    yield app
    process and process.kill()


def test_when_i_introduce_some_text_in_the_form(app):
    some_text = 'aAbB'
    entry = e2e.find_obj(app, role='text', name='string_entry')
    assert entry is not None
    entry.set_text_contents(some_text)
    do, shows = e2e.perform_on(app)
    do('click', role='push button', name='convert_button')


def test_then_the_treeview_shows_these_strings_in_its_last_row(app):
    strings = {
        'Uppercase': 'AABB',
        'Lowercase': 'aabb'
    }
    table = e2e.find_obj(app, role='table', name='string_treeview')
    assert table.get_n_columns() == 2
    assert table.get_n_rows() > 0
    last_row = table.get_n_rows() - 1

    # Note that if the order of the columns change, the test 
    # is still valid
    
    # strings['Uppercase'] == table[last_row, 0] 
    # Column 0 header is Uppercase
    assert strings[table.get_column_description(0)] == table.get_accessible_at(last_row,0).get_text(0, -1)
    
    # strings['Lowercase'] == table[last_row, 1]
    # Column 1 header is Lowercase
    assert strings[table.get_column_description(1)] == table.get_accessible_at(last_row,1).get_text(0, -1)
