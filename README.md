CVISIONLAB OPS Python Utils
===========================

`cvlops-python` package provides easy installable utils writed on python for cvisionlab internal purposes.

### How to use

```
pip install cvlops
```

Examples:

```python
from cvlops.utils import mail

mail.send("hi", ("admin@example.com"), {'body':"body", 'sender':'server@int.example.com'})
```


### Uploading a new version to pipy

Followed by:

http://stackoverflow.com/questions/1569315/setup-py-upload-is-failing-with-upload-failed-401-you-must-be-identified-t

```
python setup.py sdist upload -r https://www.python.org/pypi
```
