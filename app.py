from flask import Flask, render_template, request, jsonify
from models.recommender import TeaRecommender
import os
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

app = Flask(__name__)
# 使用环境变量或生成随机密钥
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', os.urandom(24))

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
    # 根据环境变量决定是否开启调试模式
    debug_mode = os.getenv('FLASK_ENV') == 'development'
    app.run(debug=debug_mode, host='0.0.0.0', port=int(os.getenv('PORT', 5000))) 