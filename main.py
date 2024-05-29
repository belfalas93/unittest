from hangman import HangMan
api='https://api.api-ninjas.com/v1/randomword'
def main(api):
    try:
        words=HangMan(api)
        words.api_data_set()
        words.set_choice_length()
        words.game()
    except:
        print("We couldn't connect yet...")
        print("Try our default words :))")

        words=HangMan(api)
        words.default_data_set()
        words.set_choice_length()
        words.game()

main(api)