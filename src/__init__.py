def quiz_category(answers: dict) -> str:

    key_list = list(answers.keys())
    value_list = list(answers.values())
    user_score = 0
    MAX_SCORE = len(key_list)

    for i in range(len(key_list)):
        user_input = input(f"{key_list[i]}: ").lower()
        validate = user_input == str(value_list[i]).lower()
        if validate == True:
            print("✅ Correct")
            user_score += 1
        elif validate == False:
            print("💀 False, correct answer is:", value_list[i])
    
    return(input(f"\n🏆 SCORE: {user_score}/{MAX_SCORE}\n\nℹ️ Type any key to exit"))

if __name__ == "__main__":
    answers = {"Step 1": "Import", "Step 2": "Run"}
    quiz_category(answers)
