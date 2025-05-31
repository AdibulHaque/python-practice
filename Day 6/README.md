# 🐍 Day 6 - Reeborg's World Hurdle & Maze Challenges

Today, I practiced solving several beginner-level obstacle and maze challenges on [Reeborg’s World](https://reeborg.ca/) — a visual Python-based learning platform designed to teach programming concepts interactively.

---

## 🌐 Website

- **Reeborg’s World**: [https://reeborg.ca/](https://reeborg.ca/)

---

## ✅ Solved Challenges & Files

I explored different approaches for solving each challenge and created multiple versions (`v1`, `v2`, etc.) to compare clarity vs. conciseness.

---

### 1. [Hurdle 1](https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Ftutorial_en%2Fhurdle1.json)

- **Objective**: Jump over small hurdles at fixed intervals.
- **Constraints**: Fixed hurdle height, fixed number of hurdles.
- **Solution**: Simple `for` loop with a predefined jump sequence.

📄 **File**: [`hurdle1.py`](./hurdle1.py)

---

### 2. [Hurdle 2](https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Ftutorial_en%2Fhurdle2.json)

- **Objective**: Jump over small hurdles, with an unknown number of them.
- **Constraints**: Fixed height, unknown count.
- **Solutions**:
  - `v1`: More verbose approach with step-by-step logic.
  - `v2`: Refactored into reusable, cleaner functions.

📄 **Files**:
- [`hurdle2-v1.py`](./hurdle2-v1.py)
- [`hurdle2-v2.py`](./hurdle2-v2.py)

---

### 3. [Hurdle 3](https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Ftutorial_en%2Fhurdle3.json)

- **Objective**: Jump over fixed-height hurdles that appear at random intervals.
- **Constraints**: Fixed height, random spacing.
- **Solutions**:
  - `v1`: Explicit and readable version.
  - `v2`: More compact and functionally efficient.

📄 **Files**:
- [`hurdle3-v1.py`](./hurdle3-v1.py)
- [`hurdle3-v2.py`](./hurdle3-v2.py)

---

### 4. [Hurdle 4](https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Ftutorial_en%2Fhurdle4.json)

- **Objective**: Jump over hurdles of **variable height**.
- **Constraints**: Hurdles placed randomly and of varying heights.
- **Solutions**:
  - `v1`: Step-by-step wall-following approach to climb and descend.
  - `v2`: Refactored version with cleaner logic and minimal repetition.

📄 **Files**:
- [`hurdle4-v1.py`](./hurdle4-v1.py)
- [`hurdle4-v2.py`](./hurdle4-v2.py)

---

### 5. [Maze Challenge](https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Ftutorial_en%2Fmaze.json)

- **Objective**: Navigate a maze to reach the goal.
- **Constraints**: Random maze structure. Use wall-following (e.g., right-hand rule).
- **Solutions**:
  - `v1`: Basic wall-following logic.
  - `v2`: Cleaner structure using reusable helpers.
  - `v3`: Optimized version with loop-safety and decision efficiency.

📄 **Files**:
- [`maze-v1.py`](./maze-v1.py)
- [`maze-v2.py`](./maze-v2.py)
- [`maze-v3.py`](./maze-v3.py)

---

## 📝 Summary

These exercises helped reinforce my understanding of:

- Writing reusable and modular functions
- Implementing conditional logic (`if`, `while`, `not at_goal()`)
- Using wall-following strategies (e.g., right-hand rule) in maze navigation
- Structuring clear and maintainable automation logic in Python

---

Happy coding! 🚀
