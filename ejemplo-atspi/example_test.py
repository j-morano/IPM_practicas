from ipm import e2e

import textwrap
import sys

def show(text):
    print(textwrap.dedent(text))

def show_passed():
    print('\033[92m', "  Passed",'\033[0m')

def show_not_passed(e):
    print('\033[91m', "  Not passed",'\033[0m')
    print(textwrap.indent(str(e), "    "))

def when_i_introduce_some_text_in_the_form(app, some_text):
    entry = e2e.find_obj(app, role='text', name='string_entry')
    assert entry is not None
    entry.set_text_contents(some_text)
    
def then_the_treeview_shows_these_strings_in_its_last_row(app, strings):
    table = e2e.find_obj(app, role='table', name='string_treeview')
    assert table.get_n_columns() == 2
    assert table.get_n_rows() > 0
    last_row = table.get_n_rows() - 1

    # Note that if the order of the columns change, the test 
    # is still valid
    
    # strings['Uppercase'] == table[last_row, 0] 
    # Column 0 header is Uppercase
    assert strings[table.get_column_description(0)] == table.get_accessible_at(last_row,0).get_text(0,-1)
    
    # strings['Lowercase'] == table[last_row, 1]
    # Column 1 header is Lowercase
    assert strings[table.get_column_description(1)] == table.get_accessible_at(last_row,1).get_text(0,-1)
        

if __name__== "__main__":

    path = sys.argv[1]
    process, app = e2e.run(path)
    
    if app is None:
        process and process.kill()
        assert False, f"There is no aplication {path} in the desktop"
    

    do, shows = e2e.perform_on(app)
    
    show("""
        GIVEN the app was launched
        WHEN I introduce 'aAbB' in the form and click the button
        THEN the treeview shows 'AABB' and 'aabb' in its last row
    """)
    try:
        when_i_introduce_some_text_in_the_form(app, 'aAbB')
        do('click', role='push button', name='convert_button')
        
        then_the_treeview_shows_these_strings_in_its_last_row(app,
        {
            'Uppercase': 'AABB', 
            'Lowercase': 'aabb'
        })
        show_passed()
    	
    except Exception as e:
        show_not_passed(e)
        process and process.kill()
        
   
    
    process and process.kill()

