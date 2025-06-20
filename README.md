# MovieRecommender
Search for a movie and get personalized recommendations along with poster images<br>
It uses a similarity model and data from the TMDB API.<br>

## 💡 What it does
- Search from a movie from the dataset
- Get top 5 similar movie recommendations
- View movie posters and titles of the recommendations
<br>

## 🤖 Machine Learning
- Loaded movie metadata (genres, cast, keywords, etc.)
- Combined features into a single tags attribute
- Used vectorization to convert text to numeric format
- Calculated similarity using cosine distance
- Recommended similar movies based on selected title
<br>

## 🛠️ Tech Stacks
- **Frontend**: React + Tailwind
- **Backend**: Django + Pandas + TMDB API
- **AI-ML**: CountVectorizer + Cosine Similarity (Sklearn)
<br>

## 🚀 How to run it locally

### 1. Clone the repo and initialize the files
```bash
git clone https://github.com/SudevOP1/MovieRecommender.git
pip install -r requirements.py
python initialize.py
```
### 2. Backend Server
```powershell
cd backend
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
### 3. Frontend Server
```powershell
cd frontend
npm install
npm run dev
```
### 4. See the magic happen
Go to `http://localhost:5173`<br>
<br>

## ✨ Website Design
![Example](https://raw.githubusercontent.com/SudevOP1/MovieRecommender/main/Implementation.png)
<br>
