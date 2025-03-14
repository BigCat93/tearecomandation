import pytest
from app import app as flask_app

@pytest.fixture
def app():
    """创建应用实例"""
    return flask_app

@pytest.fixture
def client(app):
    """创建测试客户端"""
    return app.test_client()

def test_home_page(client):
    """测试首页是否正常加载"""
    response = client.get('/')
    assert response.status_code == 200

def test_constitution_page(client):
    """测试体质页面是否正常加载"""
    response = client.get('/constitution')
    assert response.status_code == 200

def test_recommend_page(client):
    """测试推荐页面是否正常加载"""
    response = client.get('/recommend')
    assert response.status_code == 200

def test_recommendation_api(client):
    """测试推荐API是否正常工作"""
    test_data = {
        "age": 30,
        "gender": "female",
        "sleep_quality": 3,
        "digestion": 4,
        "energy_level": 3,
        "stress_level": 4,
        "exercise_frequency": 2,
        "diet_habit": 3
    }
    response = client.post('/get_recommendation', json=test_data)
    assert response.status_code == 200
    data = response.get_json()
    assert "constitution_type" in data
    assert "recommended_teas" in data
    assert "explanation" in data 