
# 🧠 AI-Powered Chess Coach (Stockfish + ML)

## 🚀 What it does
This project combines **Stockfish**, a powerful open-source chess engine, with **Machine Learning (ML)** to analyze and provide insights into chess moves and strategies.  

It helps chess players by:
- Suggesting the best moves using **Stockfish**.
- Providing additional insights using an **ML model trained on chess data**.

## 🛠 Tech Stack
- **Python**
- **Stockfish API**
- **TensorFlow**
- **python-chess** (for board representation)

---

## Where to find pre-trained models:

You can find **pretrained chess models** for your `models/` directory from several sources, depending on what kind of chess AI you want to integrate. Here are some great places to get them:  

---

### ✅ **1. Pretrained Chess Models from Lichess (Leela Chess Zero)**
- **Leela Chess Zero (LCZero)** is a powerful **neural network-based chess engine**.
- You can download pretrained models from:  
  🔗 [https://lczero.org/play/networks/](https://lczero.org/play/networks/)  

📌 **How to use LCZero models?**  
1. Download a `.pb.gz` or `.nnue` file from the link above.
2. Place it inside your `models/` directory.
3. Modify your TensorFlow code to load it.  

Example:  
```python
model = tf.keras.models.load_model('models/lc0_model.pb')
```

---

### ✅ **2. Pretrained Models from AlphaZero-like Projects**
- Projects inspired by **DeepMind’s AlphaZero** train neural networks for chess.  
- You can check repositories like:  
  🔗 **AlphaZero Chess Implementation**: [https://github.com/Zeta36/chess-alpha-zero](https://github.com/Zeta36/chess-alpha-zero)  

📌 **How to use AlphaZero models?**  
1. Download `.h5` or `.pb` models from GitHub repos.  
2. Save them in `models/`.  
3. Modify your TensorFlow code to use them:  
   ```python
   model = tf.keras.models.load_model('models/alphazero_model.h5')
   ```

---

### ✅ **3. Kaggle Chess Datasets with Trained Models**
- Kaggle has **pretrained ML models and datasets** for chess move predictions.  
- Check out these links:  
  🔗 **Kaggle Chess Models & Datasets**:  
  - [https://www.kaggle.com/datasets/](https://www.kaggle.com/datasets/) (Search for "chess AI")  
  - Example dataset: [https://www.kaggle.com/datasets/arevel/chess](https://www.kaggle.com/datasets/arevel/chess)  

📌 **How to use Kaggle models?**  
1. Download a trained `.h5` model.  
2. Place it inside `models/`.  
3. Load it in your code:  
   ```python
   model = tf.keras.models.load_model('models/kaggle_chess_model.h5')
   ```

---

### ✅ **4. Stockfish’s Neural Network (NNUE)**
- **Stockfish NNUE** uses **pretrained models** to enhance evaluations.  
- You can download the latest NNUE models from:  
  🔗 [https://github.com/official-stockfish/Stockfish/releases](https://github.com/official-stockfish/Stockfish/releases)  

📌 **How to use Stockfish NNUE models?**  
1. Download a `.nnue` file.  
2. Place it in `models/`.  
3. Tell Stockfish to use it:  
   ```python
   stockfish.set_option("UCI_Chess960", "true")
   stockfish.set_option("EvalFile", "models/stockfish.nnue")
   ```

---

### ✅ **5. Chess Reinforcement Learning Models**
- **OpenAI Gym** has chess environments where you can train RL-based models.
- You can download **pretrained RL models** from:  
  🔗 [https://github.com/notAI-tech/Reinforcement_Learning-Chess](https://github.com/notAI-tech/Reinforcement_Learning-Chess)  

📌 **How to use RL models?**  
1. Download the model (usually `.pth` or `.h5`).  
2. Place it in `models/`.  
3. Modify your TensorFlow/PyTorch code to load it:
   ```python
   import torch
   model = torch.load('models/chess_rl_model.pth')
   ```

---

### 🔥 **Which One Should You Use?**
- **For strong move evaluation?** → **Stockfish NNUE**  
- **For AI similar to AlphaZero?** → **LCZero or AlphaZero models**  
- **For Machine Learning-based predictions?** → **Kaggle datasets**  
- **For Reinforcement Learning?** → **Chess RL models**  

## 📥 Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/AI-Powered-Chess-Coach.git
cd AI-Powered-Chess-Coach
```

### 2️⃣ Create a Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate   # For Windows use: venv\Scripts\activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Download and Set Up Stockfish
1. Download **Stockfish** from the official site: [Stockfish Download](https://stockfishchess.org/download/)
2. Extract the executable and place it inside the `stockfish/` directory.
3. Update the path in `main.py`:
   ```python
   stockfish = Stockfish(path="stockfish/stockfish_14.1_win_x64_bmi2.exe")
   ```

---

## ▶️ Usage
### Run the program:
```bash
python main.py
```

It will output:
- **Stockfish's suggested best move**
- **ML model's analysis of the position**

---

## 📁 Project Structure
```
AI-Powered-Chess-Coach/
├── README.md          # Project documentation
├── requirements.txt   # Python dependencies
├── main.py            # Main script to run the program
├── stockfish/         # Stockfish engine binary
├── models/            # Machine learning models
└── data/              # Training data for ML model
```

---

## 📌 Features
✅ Uses **Stockfish** to analyze chess moves  
✅ Integrates **Machine Learning** to provide strategic insights  
✅ **Command-line interface** for easy interaction  
✅ Expandable: You can train custom ML models on different datasets  

---

## ⚡ Future Enhancements
- 🎨 **GUI-based interface** for better visualization  
- 📊 **Train a deep learning model** on a larger dataset  
- 🔄 **Real-time analysis** of chess games  

---

## 📜 License
This project is licensed under the **MIT License**.  
Feel free to use, modify, and contribute!  

---

## 🤝 Contributing
1. **Fork** this repository.
2. Create a **new branch** (`git checkout -b feature-name`).
3. **Commit your changes** (`git commit -m "Added new feature"`).
4. **Push to your branch** (`git push origin feature-name`).
5. Open a **Pull Request**.
