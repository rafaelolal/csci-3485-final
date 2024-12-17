# Easy Embed Package

PyPi page: https://pypi.org/project/easy-embed-rafaelolal/1.0.0/

For more detail, go to `/easy_embed/README.md`

## Demo

* Use `python==3.12.8`
* `python3.12 -m venv demo_env`
* `source demo_env/bin/activate`
* `pip install -r demo_requirements.txt` Note: you may have to remove easy_embed from `requirements.txt` and install it from PyPi
* `python demo/create_collection.py`
* `python demo/main.py`
* Visit `localhost:8000/docs` for API documentation
* Open `demo/frontend/index.html` for simple demonstration

## Build

* Use `python==3.12.8`
* `python3.12 -m venv build_env`
* `source build_env/bin/activate`
* `pip install -r build_requirements.txt`
* `python setup.py bdist_wheel sdist`
* `twine check dist/*`
* `pip install .` Recommendation: switch to a different environment, `demo_env` for example
* `twine upload -r testpypi dist/*` to upload to test.pypi.org