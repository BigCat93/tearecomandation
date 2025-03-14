import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier

class TeaRecommender:
    def __init__(self):
        # 初始化体质类型
        self.constitution_types = [
            "平和质", "气虚质", "阳虚质", "阴虚质",
            "痰湿质", "湿热质", "血瘀质", "气郁质", "特禀质"
        ]
        
        # 初始化茶饮数据库
        self.tea_database = {
            "平和质": ["西湖龙井", "碧螺春"],
            "气虚质": ["人参乌龙", "红枣茶"],
            "阳虚质": ["生姜红茶", "桂圆红枣茶"],
            "阴虚质": ["菊花茶", "金银花茶"],
            "痰湿质": ["普洱茶", "荷叶茶"],
            "湿热质": ["绿茶", "菊花茶"],
            "血瘀质": ["玫瑰茶", "红茶"],
            "气郁质": ["薄荷茶", "柑橘茶"],
            "特禀质": ["甘草茶", "枸杞茶"]
        }
        
        # 初始化分类器
        self.clf = RandomForestClassifier(n_estimators=100, random_state=42)
        self.decision_tree = DecisionTreeClassifier(random_state=42)
        
    def preprocess_user_data(self, user_data):
        """处理用户输入数据"""
        # 将用户数据转换为模型可用的格式
        features = []
        for key in ['age', 'gender', 'sleep_quality', 'digestion', 'energy_level', 
                   'stress_level', 'exercise_frequency', 'diet_habit']:
            features.append(user_data.get(key, 0))
        return np.array(features).reshape(1, -1)
    
    def get_constitution_type(self, features):
        """根据用户特征判断体质类型"""
        # 这里使用简化的逻辑，实际项目中需要训练模型
        # 示例：根据特征权重计算最可能的体质类型
        weights = np.random.rand(len(self.constitution_types))
        constitution_index = np.argmax(weights)
        return self.constitution_types[constitution_index]
    
    def get_recommendations(self, user_data):
        """生成茶饮推荐"""
        features = self.preprocess_user_data(user_data)
        constitution_type = self.get_constitution_type(features)
        
        recommended_teas = self.tea_database.get(constitution_type, ["绿茶"])
        
        return {
            "constitution_type": constitution_type,
            "recommended_teas": recommended_teas,
            "explanation": self.get_explanation(constitution_type)
        }
    
    def get_explanation(self, constitution_type):
        """获取体质说明"""
        explanations = {
            "平和质": "体质平和，适合大多数茶饮，建议选择清淡型茶饮。",
            "气虚质": "气虚体质需要补气养生，建议选择温和滋补型茶饮。",
            "阳虚质": "阳虚体质需要温补，建议选择温热性茶饮。",
            "阴虚质": "阴虚体质需要滋阴，建议选择清凉解火型茶饮。",
            "痰湿质": "痰湿体质需要化湿，建议选择具有利水渗湿功效的茶饮。",
            "湿热质": "湿热体质需要清热利湿，建议选择具有清热作用的茶饮。",
            "血瘀质": "血瘀体质需要活血化瘀，建议选择具有活血功效的茶饮。",
            "气郁质": "气郁体质需要疏肝解郁，建议选择具有理气功效的茶饮。",
            "特禀质": "特禀体质需要调养，建议选择温和平和的茶饮。"
        }
        return explanations.get(constitution_type, "建议选择清淡型茶饮。") 