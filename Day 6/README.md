# 🐍 Day 6 - Reeborg's World Hurdle Challenges

Today, I practiced solving three beginner-level obstacle challenges on [Reeborg’s World](https://reeborg.ca/) — a visual Python-based learning platform designed to teach programming concepts interactively.

---

## 🌐 Website

- **Reeborg’s World**: [https://reeborg.ca/](https://reeborg.ca/)

---

## ✅ Solved Challenges & Files

I solved each challenge and experimented with different approaches — creating two versions (`v1`, `v2`) for some problems to compare short and long solutions.

---

### 1. [Hurdle 1](https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Ftutorial_en%2Fhurdle1.json)

- **Objective**: Jump over small hurdles that appear at regular intervals.
- **Constraints**: Fixed hurdle height, fixed number of hurdles.
- **Solution**: Simple `for` loop with a predefined jump sequence.

**File:** [`hurdle1.py`](./hurdle1.py)

---

### 2. [Hurdle 2](https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Ftutorial_en%2Fhurdle2.json)

- **Objective**: Jump over small hurdles, but the number of hurdles is unknown.
- **Constraints**: Fixed height, unknown number of hurdles.
- **Solutions**:
  - `v1`: More verbose approach with step-by-step movement.
  - `v2`: More concise, compact version using reusable functions.

**Files:**

- [`hurdle2-v1.py`](./hurdle2-v1.py)
- [`hurdle2-v2.py`](./hurdle2-v2.py)

---

### 3. [Hurdle 3](https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Ftutorial_en%2Fhurdle3.json)

- **Objective**: Jump over fixed-height hurdles that appear at **random intervals**.
- **Constraints**: Fixed height, random spacing.
- **Solutions**:
  - `v1`: Detailed and more explicit code.
  - `v2`: Optimized, compact version.

**Files:**

- [`hurdle3-v1.py`](./hurdle3-v1.py)
- [`hurdle3-v2.py`](./hurdle3-v2.py)

---

---

## 📝 Summary

These exercises helped reinforce my understanding of:

- Defining and reusing functions
- Using conditionals (`if`, `while`, `not at_goal()`)
- Writing clean, modular Python code for automation logic

---

Happy coding! 🚀
