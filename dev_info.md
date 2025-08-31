# How to update a new version

1. increment the version in pyproject

2. 

```
python3 -m build
```

3. 

```
python3 -m twine upload dist/quiz_game-0.0.2-py3-none-any.whl
```