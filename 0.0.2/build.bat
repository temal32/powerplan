@RD /S /Q "C:\Users\Temal\Desktop\winpower\build"
@RD /S /Q "C:\Users\Temal\Desktop\winpower\dist"
@RD /S /Q "C:\Users\Temal\Desktop\winpower\powerplan.egg-info"
python setup.py sdist bdist_wheel
python -m twine upload dist/*