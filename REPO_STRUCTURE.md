# Repository Structure

This document explains what's tracked in Git and what's ignored.

## ✅ TRACKED (will be pushed to GitHub)

### Essential Code:
- `src/network.py` - Basic neural network implementation
- `src/network2.py` - Improved version with regularization (recommended)
- `src/network3.py` - Theano-based version (deprecated, but kept for reference)
- `src/mnist_loader.py` - MNIST data loader
- `src/test.py` - **Your training script**

### Supporting Files:
- `data/mnist.pkl.gz` - MNIST dataset
- `requirements.txt` - Python dependencies
- `README.md` - Project documentation
- `.gitignore` - Git ignore rules

## ❌ IGNORED (will NOT be pushed to GitHub)

### Generated Content:
- `fig/` - **Entire directory** (pre-generated book figures)
- `my_figures/` - Your generated plots from test.py
- `src/*.png` - Any PNG files in src/
- `src/*.json` - Any JSON results in src/

### Python Cache:
- `__pycache__/` - Python bytecode cache
- `*.pyc` - Compiled Python files

### System Files:
- `.DS_Store` - macOS metadata
- `*~` - Linux backup files

### Development:
- `venv/`, `env/` - Virtual environments
- `.vscode/`, `.idea/` - IDE settings

## 📁 Recommended Workflow

1. **Run your experiments:**
   ```bash
   cd src
   python3 test.py
   ```

2. **Your figures will be saved to:**
   ```
   my_figures/
   ├── 20250428_143052_accuracy_plot.png
   └── 20250428_143052_cost_plot.png
   ```

3. **Commit only code changes:**
   ```bash
   git add src/test.py
   git commit -m "Updated training parameters"
   git push
   ```

## 🎯 What Gets Pushed

When you push to GitHub, others will get:
- ✅ All the neural network code
- ✅ The MNIST dataset
- ✅ Your training script (test.py)
- ❌ NOT the 70+ pre-generated book figures
- ❌ NOT your experiment results

This keeps your repo clean and focused on code, not output!

