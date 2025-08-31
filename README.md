# Quiz 🎯

## Create your quiz game faster in Python! 🎴

### Why? 🥺

To practice for exams, test your knowledge, and boost your memory!

### How? 😫 (🐧Linux 🪟Windows 🍏Mac)

1. Create VENV 👾

```shell
python -m venv /path/to/new/virtual/environment
```

2. Install 🛠️

```shell
pip install quiz-game
```

3. Create a python file 📁

```shell
echo hi > ./your_script.py
```

4. **Import** this module into your script 📥

```py
from quiz_game import quiz_start
```

5. **Add your questions and answers** in a dictionary 👨🏻‍💻

```py
from quiz_game import quiz_start

quiz_start(
    {
        "question 1": "answer 1",
        "question 2": "answer 2",
        "question 3": "answer 3",
    }
)
```

6. **Run your script** and play the quiz! 🎮

```
python ./your_script.py
```

You’ll see ✅ for correct answers and 💀 for wrong ones.
At the end, you’ll get your score, e.g. "2/3".
