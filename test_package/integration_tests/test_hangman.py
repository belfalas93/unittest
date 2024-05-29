import unittest
import requests
import random as rnd
from hangman import HangMan


class TestHangMan(unittest.TestCase):
    def test_api_dataset(self):
        api='https://api.api-ninjas.com/v1/randomword'
        url=HangMan(api)

        response = requests.get(url.api, headers={'X-Api-Key': 'by9Fu6ZMDue6FdcJBpgUNw==SvDAHgEaGOCm2gr5'})
        words=response.json()["word"].lower()
        url.word=words

        self.assertIsNotNone(response)
        self.assertEqual(response.status_code , 200)
        self.assertEqual(url.word,words)
        #for connection error
        with self.assertRaises(Exception) as f:
            requests.get(url.api, headers={'X-Api-Key': 'by9Fu6ZMDue6FdcJBpgUNw==SvDAHgEaGOCm2gr5'})
            

    def test_lenght_choice(self):
        ex=HangMan('example')
        ex.word="kingcharles"
        ex.set_choice_length()
        len_ex=len(ex.word)
        choic=3*len_ex
        self.assertEqual(ex.length,len_ex)
        self.assertEqual(ex.choices,choic)
        

    def test_default_dataset(self):
        url=HangMan("something")
        colors=['blue','red']
        topics={'Colors':colors}
        topic_choice=rnd.choice(list(topics.keys()))
        words_of_topic=topics[topic_choice]
        words=rnd.choice(words_of_topic)
        url.word=words
        # self.assertListEqual(colors,words_of_topic)
        # self.assertEqual(words,url.word)

        url.length=len(url.word)
        url.choices=3*url.length
        final_word=url.game()
        self.assertEqual(final_word,url.word)


#python -m unittest discover -s test_package\integration_tests -v