document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('recommendationForm');
    const modal = new bootstrap.Modal(document.getElementById('recommendationModal'));
    
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
            
            // 发送请求到后端
            fetch('/get_recommendation', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(formData)
            })
            .then(response => response.json())
            .then(data => {
                // 显示推荐结果
                const resultDiv = document.getElementById('recommendationResult');
                resultDiv.innerHTML = `
                    <h4>您的体质类型：${data.constitution_type}</h4>
                    <p>${data.explanation}</p>
                    <div class="tea-recommendation">
                        <h5>推荐茶饮：</h5>
                        <ul>
                            ${data.recommended_teas.map(tea => `<li>${tea}</li>`).join('')}
                        </ul>
                    </div>
                `;
                
                // 显示模态框
                modal.show();
            })
            .catch(error => {
                console.error('Error:', error);
                alert('抱歉，推荐系统暂时出现问题，请稍后再试。');
            });
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