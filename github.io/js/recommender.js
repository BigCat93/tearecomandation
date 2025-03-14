document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('recommendationForm');
    const modal = new bootstrap.Modal(document.getElementById('recommendationModal'));
    
    // 体质类型和茶饮数据库
    const teaDatabase = {
        "平和质": {
            teas: ["西湖龙井", "碧螺春"],
            description: "体质平和，适合大多数茶饮，建议选择清淡型茶饮。"
        },
        "气虚质": {
            teas: ["人参乌龙", "红枣茶"],
            description: "气虚体质需要补气养生，建议选择温和滋补型茶饮。"
        },
        "阳虚质": {
            teas: ["生姜红茶", "桂圆红枣茶"],
            description: "阳虚体质需要温补，建议选择温热性茶饮。"
        },
        "阴虚质": {
            teas: ["菊花茶", "金银花茶"],
            description: "阴虚体质需要滋阴，建议选择清凉解火型茶饮。"
        },
        "痰湿质": {
            teas: ["普洱茶", "荷叶茶"],
            description: "痰湿体质需要化湿，建议选择具有利水渗湿功效的茶饮。"
        },
        "湿热质": {
            teas: ["绿茶", "菊花茶"],
            description: "湿热体质需要清热利湿，建议选择具有清热作用的茶饮。"
        },
        "血瘀质": {
            teas: ["玫瑰茶", "红茶"],
            description: "血瘀体质需要活血化瘀，建议选择具有活血功效的茶饮。"
        },
        "气郁质": {
            teas: ["薄荷茶", "柑橘茶"],
            description: "气郁体质需要疏肝解郁，建议选择具有理气功效的茶饮。"
        },
        "特禀质": {
            teas: ["甘草茶", "枸杞茶"],
            description: "特禀体质需要调养，建议选择温和平和的茶饮。"
        }
    };

    // 根据用户数据判断体质类型
    function determineConstitutionType(formData) {
        // 将表单数据转换为数值数组
        const features = [
            parseInt(formData.age),
            parseInt(formData.gender),
            parseInt(formData.sleep_quality),
            parseInt(formData.digestion),
            parseInt(formData.energy_level),
            parseInt(formData.stress_level),
            parseInt(formData.exercise_frequency),
            parseInt(formData.diet_habit)
        ];

        // 计算各项指标的权重得分
        const energyScore = (5 - features[4]) * 2; // 精力状态
        const sleepScore = (5 - features[2]) * 1.5; // 睡眠质量
        const digestionScore = (5 - features[3]) * 1.5; // 消化状况
        const stressScore = features[5] * 1.2; // 压力水平
        const exerciseScore = features[6] * 1.2; // 运动频率
        const dietScore = features[7] * 1.2; // 饮食习惯

        // 根据得分判断体质类型
        if (energyScore <= 4 && sleepScore <= 3) {
            return "气虚质";
        } else if (stressScore >= 8) {
            return "气郁质";
        } else if (digestionScore >= 6 && dietScore >= 6) {
            return "痰湿质";
        } else if (energyScore >= 8 && sleepScore >= 6) {
            return "平和质";
        } else if (stressScore >= 6 && energyScore <= 5) {
            return "阴虚质";
        } else if (digestionScore >= 7 && stressScore >= 5) {
            return "湿热质";
        } else if (exerciseScore <= 4 && energyScore <= 5) {
            return "阳虚质";
        } else if (digestionScore >= 5 && sleepScore <= 4) {
            return "血瘀质";
        } else {
            return "平和质";
        }
    }

    if (form) {
        form.addEventListener('submit', function(e) {
            e.preventDefault();
            
            // 收集表单数据
            const formData = {
                age: document.getElementById('age').value,
                gender: document.querySelector('input[name="gender"]:checked')?.value,
                sleep_quality: document.getElementById('sleep_quality').value,
                digestion: document.getElementById('digestion').value,
                energy_level: document.getElementById('energy_level').value,
                stress_level: document.getElementById('stress_level').value,
                exercise_frequency: document.getElementById('exercise_frequency').value,
                diet_habit: document.getElementById('diet_habit').value
            };

            // 检查是否所有字段都已填写
            if (Object.values(formData).some(value => !value)) {
                alert('请填写所有必填项');
                return;
            }
            
            // 获取体质类型和推荐
            const constitutionType = determineConstitutionType(formData);
            const recommendation = teaDatabase[constitutionType];
            
            // 显示推荐结果
            const resultDiv = document.getElementById('recommendationResult');
            resultDiv.innerHTML = `
                <h4>您的体质类型：${constitutionType}</h4>
                <p>${recommendation.description}</p>
                <div class="tea-recommendation">
                    <h5>推荐茶饮：</h5>
                    <ul>
                        ${recommendation.teas.map(tea => `<li>${tea}</li>`).join('')}
                    </ul>
                </div>
            `;
            
            // 显示模态框
            modal.show();
        });
    }
    
    // 表单验证
    const forms = document.querySelectorAll('.needs-validation');
    Array.from(forms).forEach(form => {
        form.addEventListener('submit', event => {
            if (!form.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
            }
            form.classList.add('was-validated');
        }, false);
    });
}); 