TASKS = {
    "easy": {
        "transcript": "Rahul: I'll send report by Friday.",
        "expected": [
            {
                "description": "send report",
                "owner": "Rahul",
                "deadline": "Friday"
            }
        ]
    },

    "medium": {
        "transcript": """
        Rahul: I'll send report by Friday.
        Priya: I will schedule client meeting next week.
        """,
        "expected": [
            {"description": "send report", "owner": "Rahul"},
            {"description": "schedule client meeting", "owner": "Priya"}
        ]
    },

    "hard": {
        "transcript": """
        Rahul: I'll send report by Friday.
        Priya: schedule client meeting next week.
        Amit: prepare budget draft by Monday.
        """,
        "expected": [
            {"description": "send report", "owner": "Rahul"},
            {"description": "schedule client meeting", "owner": "Priya"},
            {"description": "prepare budget draft", "owner": "Amit"}
        ]
    }
}