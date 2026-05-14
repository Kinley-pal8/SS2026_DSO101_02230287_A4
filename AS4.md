# Assignment IV
## Continuous Integration and Continuous Deployment (DSO101)
**Bachelor's of Engineering in Software Engineering (SWE)**  
**Date of Submission:** 13th May

---

## 🔹 Title: Build a Complete CI/CD Pipeline with Testing & Deployment

### 🎯 Objective

Implement a real DevOps pipeline including:

- Build
- Test
- Deploy
- Automation

---

## 📌 Task

You must:

- Create a backend app (Flask / Node.js)
- Add unit tests
- Create a CI/CD pipeline:
  - Build
  - Test
  - Deploy
- Deploy to Render automatically

---

## 🛠 Tools Required

- GitHub
- GitHub Actions
- Render
- pytest or Jest

---

## 📂 Project Structure

```
project/
│── app.py
│── test_app.py
│── requirements.txt
│── .github/workflows/ci.yml
```

---

## 🧪 Sample Test (Python)

```python
def test_home():
    assert 1 + 1 == 2
```

---

## 🔄 CI/CD Pipeline Example

```yaml
name: CI/CD Pipeline

on:
  push:
    branches: ["main"]

jobs:
  build-test-deploy:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: "3.9"

      - name: Install dependencies
        run: pip install -r requirements.txt

      - name: Run tests
        run: pytest

      - name: Deploy message
        run: echo "Deploying to Render..."
```

---

## 🌐 Deployment Requirement

- Auto-deploy on push
- Show working live app

---

## 📊 Marking Scheme (10 Marks)

| Criteria | Marks |
|----------|-------|
| Project structure | 2 |
| CI pipeline (build + test) | 3 |
| Test implementation | 2 |
| Deployment automation | 2 |
| Documentation | 1 |
| **Total** | **10** |

---

## 📦 Submission

- GitHub repo
- Workflow file
- Test output screenshot
- Live app URL