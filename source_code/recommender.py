def get_advice(prediction, hr, att):
    if prediction == 1:
        return "✨ Result: Likely to PASS! Recommendation: Maintain your current routine."
    else:
        advice = "⚠️ Result: At RISK of failing."
        if att < 75:
            advice += "\n💡 Action: Your attendance is below 75%. Prioritize physical classes."
        if hr < 5:
            advice += "\n💡 Action: Increase self-study time to at least 7-10 hours/week."
        return advice
