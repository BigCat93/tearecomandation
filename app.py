from flask import Flask, render_template, request, jsonify
from models.recommender import TeaRecommender
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)

# 初始化推荐系统
tea_recommender = TeaRecommender()

@app.route('/')
def index():
    """首页路由"""
    return render_template('index.html')

@app.route('/constitution')
def constitution():
    """中医体质知识页面"""
    return render_template('constitution.html')

@app.route('/recommend')
def recommend():
    """推荐问卷页面"""
    return render_template('recommend.html')

@app.route('/get_recommendation', methods=['POST'])
def get_recommendation():
    """处理推荐请求"""
    user_data = request.json
    recommendations = tea_recommender.get_recommendations(user_data)
    return jsonify(recommendations)

if __name__ == '__main__':
    app.run(debug=True) 