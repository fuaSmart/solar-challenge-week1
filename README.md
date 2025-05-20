# 🌞 Solar Data Challenge - Week 1

**Branch:** `setup-task`  
**Latest Update:** `feat: add README files to notebooks and scripts`  

## 🚀 Project Overview
A data analysis project to evaluate solar energy potential using:
- **Solar irradiance data** (GHI, DNI, DHI)  
- **Weather sensor data** (temperature, wind speed)  

## 📂 Repository Structure
```
.
├── .github/workflows/    # GitHub Actions CI
├── notebooks/            # Jupyter notebooks for EDA
├── scripts/              # Python data processing scripts
├── tests/                # Test cases
├── .gitignore           # Excludes data/ and venv/
├── LICENSE              # MIT License
└── requirements.txt     # Python dependencies
```

## ⚡ Quick Start
1. **Clone the repo**:
   ```bash
   git clone https://github.com/fuaSmart/solar-challenge-week-1.git
   cd solar-challenge-week-1
   git checkout setup-task
   ```

2. **Set up Python environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   pip install -r requirements.txt
   ```

3. **Run Jupyter notebooks**:
   ```bash
   jupyter notebook notebooks/
   ```

## 🔍 Key Files
| File/Folder          | Purpose                          |
|----------------------|----------------------------------|
| `notebooks/*.ipynb`  | EDA and data cleaning           |
| `scripts/`           | Automated data pipelines        |
| `.github/workflows/` | CI/CD (GitHub Actions)          |

## 🤝 How to Contribute
1. Create a new branch:  
   ```bash
   git checkout -b your-feature
   ```
2. Commit changes:  
   ```bash
   git commit -m "feat: your description"
   ```
3. Push and open a Pull Request!

---

📜 **License**: [MIT](LICENSE)  
🔗 **Repository**: [github.com/fuaSmart/solar-challenge-week-1](https://github.com/fuaSmart/solar-challenge-week-1)
