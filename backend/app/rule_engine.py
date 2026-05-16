import random

def rule_engine(user_input, round):
    responses = [
        {
            "attack": "⚠️ System fails under concurrent requests.",
            "edge_cases": "Multiple simultaneous transactions.",
            "feedback": "Concurrency not handled properly.",
            "score": random.randint(50, 70)
        },
        {
            "attack": "⚠️ Performance bottleneck detected.",
            "edge_cases": "Queue buildup under load.",
            "feedback": "Response time too high.",
            "score": random.randint(60, 75)
        }
    ]
    return random.choice(responses)