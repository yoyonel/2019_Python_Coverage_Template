"""
https://simplejson.readthedocs.io/en/latest/
https://codingnetworker.com/2015/10/python-dictionaries-json-crash-course/
https://docs.python.org/2/library/inspect.html
https://docs.python.org/2/library/imp.html#imp.load_source
https://pymotw.com/2/inspect/
"""
import imp
from inspect import getmembers
import simplejson as json
from pathlib2 import Path
import widgets


def test_widgets():
    pattern_widget_python_file = "widget*.py"
    for path_widget_python_file in Path(widgets.__file__).parents[0].glob('*/%s' % pattern_widget_python_file):
        python_name_module = str(path_widget_python_file.parents[0].stem)

        # just for coverage
        imp.load_source(python_name_module, str(path_widget_python_file.with_name('__init__.py')))

        # get all dicts in package module and remove __builtin__
        for t_dict_in_module in filter(lambda t: not t[0].startswith('__'),
                                       getmembers(imp.load_source(python_name_module, str(path_widget_python_file)),
                                                  lambda o: isinstance(o, dict))):
                # test dictionnary can be dumps as valid JSON
                # if not that raise a simplejson.JSONDecodeError
                json.dumps(t_dict_in_module[1])
