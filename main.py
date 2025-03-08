from stockfish import Stockfish
import tensorflow as tf

# Load the trained ML model
model = tf.keras.models.load_model('models/my_chess_model')

# Set up Stockfish
stockfish = Stockfish(path="stockfish/stockfish_14.1_win_x64_bmi2.exe")
stockfish.set_position(["e2e4", "e7e5"])

# Get the best move from Stockfish
best_move_stockfish = stockfish.get_best_move()

# Get ML-based insights for move recommendations
chess_position = "e2e4 e7e5 ..."  # Example position in a format your model understands
move_prediction = model.predict(chess_position)

print(f"Stockfish suggests: {best_move_stockfish}")
print(f"ML model suggests: {move_prediction}")
