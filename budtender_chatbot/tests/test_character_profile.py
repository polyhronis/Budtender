import unittest
from budtender_chatbot.src.character_profile import CharacterProfile

class TestCharacterProfile(unittest.TestCase):

    def setUp(self):
        self.character = CharacterProfile()

    def test_character_age(self):
        self.assertEqual(self.character.age, 25, "Character age should be 25")

    def test_character_personality(self):
        self.assertEqual(self.character.personality, "hippie", "Character personality should be hippie")

    def test_character_professionalism(self):
        self.assertTrue(self.character.is_professional, "Character should be professional")

    def test_character_knowledge(self):
        self.assertTrue(self.character.is_knowledgeable, "Character should be knowledgeable")

    def test_character_flirtiness(self):
        self.assertTrue(self.character.is_flirty, "Character should be flirty")

if __name__ == '__main__':
    unittest.main()