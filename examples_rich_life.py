import numpy as np
from pymcdm.methods import TOPSIS
from pymcdm.helpers import normalize_matrix

# 人生の選択肢
alternatives = ["Science Career", "Artistic Pursuit", "Family Life", "World Travel"]

# 基準（宇宙的＋クオリア）
criteria = ["Impact on Society", "Personal Joy", "Financial Stability"]

# 意思決定マトリックス（定性的データを数値化）
decision_matrix = np.array([
    [0.8, 0.5, 0.8],  # Science Career
    [0.2, 0.8, 0.2],  # Artistic Pursuit
    [0.5, 0.8, 0.5],  # Family Life
    [0.2, 0.8, 0.2]   # World Travel
])

# 基準の重み（ユーザーの価値観に基づく）
weights = np.array([0.4, 0.4, 0.2])

# 基準タイプ（1 = 最大化）
types = np.array([1, 1, 1])

# TOPSISで評価
topsis = TOPSIS()
scores = topsis(decision_matrix, weights, types)

# 最適な選択肢を選択
best_index = np.argmax(scores)
best_alternative = alternatives[best_index]

print(f"豊かな人生のための最適な選択肢: {best_alternative}")
print(f"スコア: {scores}")