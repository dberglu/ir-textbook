# MkDocs Restart Cheat Sheet (Investor Relations Textbook)

## 🪜 Step 1. Open Terminal
You’ll see something like:
```
(base) MacBook-Pro:~ davidberglund$
```

---

## 🪜 Step 2. Activate your MkDocs environment
```bash
conda activate mkdocs
```

✅ You should now see `(mkdocs)` at the start of your prompt:
```
(mkdocs) MacBook-Pro:~ davidberglund$
```

---

## 🪜 Step 3. Navigate to your project folder
```bash
cd ~/ir-textbook
```

Confirm your location:
```bash
pwd
```
Expected:
```
/Users/davidberglund/ir-textbook
```

Check your files:
```bash
ls
```
Expected:
```
docs    mkdocs.yml
```

---

## 🪜 Step 4. Verify your chapters folder
```bash
ls -R docs
```
Expected:
```
docs:
chapters
index.md

docs/chapters:
index.md
chapter-1.md
chapter-2.md
chapter-3.md
```

If missing:
```bash
mkdir -p docs/chapters
touch docs/chapters/index.md
```

---

## 🪜 Step 5. Build your site
```bash
mkdocs build --clean
```

---

## 🪜 Step 6. Serve your site locally
```bash
mkdocs serve
```

✅ Look for:
```
INFO - Serving on http://127.0.0.1:8000/
```

Then open your browser to:
👉 http://localhost:8000

---

## 🪜 Step 7. Stop the local server
Press **CTRL + C** in Terminal.

---

## 💡 Troubleshooting Quick Fixes
| Issue | Solution |
|-------|-----------|
| `(base)` prompt shows, not `(mkdocs)` | Run `conda activate mkdocs` |
| `mkdocs: command not found` | You’re not in the right environment — activate it again |
| Still getting warnings | Check that all `.md` files listed in `mkdocs.yml` exist |
| Want to open in VS Code | From your project folder, run `code .` |
