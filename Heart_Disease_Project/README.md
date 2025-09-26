## Heart Disease ML Pipeline

### Quickstart
1. Create a Python environment (recommended):
   - Ensure Python 3.13 with venv is available: `sudo apt-get install -y python3-venv`
   - `python3 -m venv .venv && source .venv/bin/activate`
   - `pip install -r requirements.txt`

2. Data
   - Place the dataset at `data/heart_disease.csv`.
   - If needed, use `download_data.py` to fetch. If remote fails, a small placeholder can be used for demo.

3. Run Notebooks (recommended order)
   - `notebooks/01_data_preprocessing.ipynb`
   - `notebooks/02_pca_analysis.ipynb`
   - `notebooks/03_feature_selection.ipynb`
   - `notebooks/04_supervised_learning.ipynb`
   - `notebooks/05_unsupervised_learning.ipynb`
   - `notebooks/06_hyperparameter_tuning.ipynb`

4. Streamlit UI
   - After saving `models/final_model.pkl`, run: `streamlit run ui/app.py`

5. Ngrok (optional)
   - See `deployment/ngrok_setup.txt`.

### Repo Structure
See the `Heart_Disease_Project/` layout in the prompt.

