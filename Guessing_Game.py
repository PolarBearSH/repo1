from dotenv import load_dotenv
from groq import Groq
load_dotenv()

class Game:
    def __init__(self):
        self.client = Groq()
        self.model = "llama-3.3-70b-versatile"
        self.points = 0

    def get_animal_name(self):
        system_prompt = "Give a random animal name for a guessing game. One word only, nothing else. Not too hard."
        animal_name = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "system", "content": system_prompt}],
            max_tokens=10
        )
        return animal_name.choices[0].message.content.strip()

    def get_reply(self, messages, max_retries=3):
        for attempt in range(max_retries):
            try:
                reply = self.client.chat.completions.create(
                    model=self.model,
                    messages=messages,
                    max_tokens=50  # short replies only
                )
                ans = reply.choices[0].message.content
                if ans and ans.strip():
                    return ans.strip()
            except Exception as e:
                print(f"[Retry {attempt+1}] Error: {e}")
        return "I can't tell you that."

    def play(self):
        animal = self.get_animal_name()
        letters = len(animal)
        system_prompt = f"""You are playing a guessing game. The user is trying to guess your animal. Your animal is {animal}.
        It has exactly {letters} letters.
            RULES:
            1. The user can either ask a Yes/No question or make a guess.
            2. If it's a Yes/No question, reply ONLY with Yes or No. Nothing else.
            3. If the user guesses wrong, reply ONLY with: [their guess] is not correct.
            If the user guesses correctly, reply ONLY with: Congratulations. You guessed it!
            4. If the question cannot be answered Yes/No and is not a guess, reply ONLY with: I can't tell you that.
            IMPORTANT: Never combine multiple answers. Give exactly one short response per turn."""

        text = []
        guessed = False
        for i in range(10):
            guess = input(f"{i + 1}. Question or guess: ").strip()
            while not guess:
                guess = input(f"{i + 1}. Question or guess: ").strip()

            text.append({"role": "user", "content": guess})
            ans = self.get_reply([{"role": "system", "content": system_prompt}] + text)
            text.append({"role": "assistant", "content": ans})

            if "congratulations" in ans.lower():
                self.points += 1
                print(f"\n🎉 Correct! Score: {self.points}")
                guessed = True
                break
            print(ans)

        if not guessed:
            print(f"\n❌ The animal was: {animal}")

    def start(self):
        print("------------GUESSING GAME--------------")
        print("You have 10 questions. Ask yes/no questions, then guess!\n")
        while True:
            self.play()
            again = input("\nPlay again? (y/n): ").strip().lower()
            if again != "y":
                print(f"Final score: {self.points}. Goodbye!")
                break

g = Game()
g.start()