import google.generativeai as genai

# model class
class SentimentModel:

    def get_model(self):
        GOOGLE_API_KEY = "AIzaSyCy7A0kg3sTiW2Ia5qONSSn1YTf3d89ts0"

        try:
            genai.configure(api_key=GOOGLE_API_KEY)
            model = genai.GenerativeModel("gemini-2.0-flash")
            return  model
        except Exception as e:
            print(e)
    
# app
class SentimentApp(SentimentModel):
    def __init__(self):
        self.__database = {}
        self.main_menu()

    def main_menu(self):
        main_input = input("""
        Hello! Choose a menu option:

            1. Don't have an account? Register
            2. Already have an account? Login
            3. Exit
                            
            """)
        if main_input == "1":
            self.__register()

        elif main_input == "2":
            # login
            self.__login()

        else:
            exit()

    def secondary_menu(self):
        secondary_input = input("""
        Hello! What would you like to do? :

            1. Sentiment Analysis
            2. Language Translation
            4. Language Detection
            3. Exit
                            
            """)

        if secondary_input == "1":
            self.__sentiment_analysis()
        
        elif secondary_input == "2":
            self.__language_translation()

        elif secondary_input == "3":
            self.__language_detection()
        
        else:
            exit()

    def __sentiment_analysis(self):
        user_text = input("Enter the sentence to evaluate: ")
        model = super().get_model()
        response = model.generate_content(f"Give me the sentiment of this sentence: {user_text}")
        results = response.text
        print(results)
        self.secondary_menu()

    def __language_translation(self):
        user_text = input("Enter the sentence to translate to english: ")
        model = super().get_model()
        response = model.generate_content(f"Give me the english translation of this sentence: {user_text}")
        results = response.text
        print(results)
        self.secondary_menu()

    def __language_detection(self):
        user_text = input("Enter the sentence to detect the language of: ")
        model = super().get_model()
        response = model.generate_content(f"Give me the language of this sentence: {user_text}")
        results = response.text
        print(results)
        self.secondary_menu()

    def __register(self):
        # register
        name = input("Please enter your fist name: ")
        email = input("Please enter your email address: ")
        password = input("Please enter a password: ")

        if email in self.__database:
            print ("Email is already in use, login or use a different email address.")
    
        else:
            self.__database[email] = [name, password]
            print("Registration successful! Please login.")
            self.main_menu()

    # login
    def __login(self):
        email = input("Please enter your email address: ")
        password = input("Please enter a password: ")

        if email in self.__database:
            if self.__database[email][1] == password:
                print("Login Successful!")
                self.secondary_menu()
            else:
                print("Password does not match!")
                self.main_menu()

        



# initialize object
if __name__ == '__main__':
    sentiment_analysis = SentimentApp()


