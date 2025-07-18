
# 🧠 MCQ Quiz Web Application

A simple and elegant Multiple Choice Quiz application built with **Python Flask**, **Bootstrap 4.5**, and the **Open Trivia API**. This project was developed with guidance from **ChatGPT**, focusing on full-stack development, API integration, form processing, and dynamic UI/UX enhancements.

---

## 🚀 Features

* 🎯 Choose from quiz categories like *Technology*, *General Knowledge*, etc.
* 📡 Fetches 5 random multiple-choice questions using [OpenTDB API](https://opentdb.com).
* ✅ Submit answers and get immediate score feedback.
* 🎨 Displays correct/incorrect answers with color indicators.
* ⏱️ Built-in 2-minute countdown timer with auto-submit.
* 💻 Mobile responsive design with **Bootstrap 4.5 (CDN)**.
* ✨ Smooth UI animations for question loading.

---

## 🛠️ Technologies Used

| Layer     | Tech Stack                            |
| --------- | ------------------------------------- |
| Frontend  | HTML, CSS, Bootstrap 4.5              |
| Backend   | Python 3.x, Flask                     |
| API       | [Open Trivia DB](https://opentdb.com) |
| Utilities | Jinja2, UUID, HTML unescape           |

---

## 📂 Project Structure

```
quiz-app/
├── static/
│   └── script.js               # Timer & animations
├── templates/
│   ├── index.html              # Home page with category selection
│   ├── quiz.html               # Displays questions
│   └── result.html             # Displays result after submission
├── app.py                      # Flask application logic
├── requirements.txt            # Python dependencies
└── README.md                   # Project description
```

---

## 🔧 Setup Instructions

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your-username/quiz-app.git
   cd quiz-app
   ```

2. **Create a Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate      # Linux/macOS
   venv\Scripts\activate         # Windows
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Flask App**

   ```bash
   python app.py
   ```

5. Open in browser: `http://127.0.0.1:5000`

---


## 🧠 Developed with ChatGPT

This project was created with **ChatGPT** acting as a collaborative coding assistant. ChatGPT helped:

* Architect the app structure
* Build routes and logic
* Generate template code
* Debug backend issues
* Add UI/UX polish and advanced features

---

## 📌 Future Enhancements

* Save scores to a database
* Add authentication for users
* Create a leaderboard
* Allow difficulty level selection

---

## 💡 License

This project is open-source under the [MIT License](LICENSE).

---


