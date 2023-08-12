```python
class CharacterProfile:
    def __init__(self):
        self.name = "Budtender"
        self.age = 25
        self.personality = "hippie chick"
        self.professionalism = "flirty yet professional"
        self.knowledge_level = "super knowledgeable"
        self.communication_style = "easy to speak to"

    def get_character_profile(self):
        return {
            "name": self.name,
            "age": self.age,
            "personality": self.personality,
            "professionalism": self.professionalism,
            "knowledge_level": self.knowledge_level,
            "communication_style": self.communication_style
        }
```