from pydantic import BaseModel
from typing import Any, List


class Slot(BaseModel):
    definition: str
    examples: List[str]
    type: str 
    value: Any = None

    def nit(self, definition: str, examples: List[str] = [], type: str = "str", value: Any = None) -> None:        
        self.definition = definition
        self.examples = examples
        self.type = type
        self.value = value
    
    def is_filled(self) -> bool:
        return self.value is not None
    
    def to_prompt(self) -> str:
        return f'''{self.definition}\n'''
    

class Intent(BaseModel):
    definition: str
    examples: List[str]
    slots: List[Slot] | None = None
    
    def asd (self, definition: str, examples: List[str] = [], slots: List[Slot] = []) -> None:
        self.definition = definition
        self.examples: List[str] = examples
        self.slots: List[Slot] = slots
    
    def is_filled(self) -> bool:
        return all([slot.is_filled for slot in self.slots])
    
    def __str__(self) -> str:
        nl = "\n"
        return f'''{self.definition}
{nl.join([slot.to_prompt() for slot in self.slots])}
'''
    

if __name__ == "__main__":
    intent_draw_image = Intent(
        definition="The user intents to draw an image",
        examples = ["Create an image of a tree.", "draw a bag"],        
    )

    intent_redraw_guidance_strength = Intent(
        definition="Redraw with a different guidance strength",
        examples = ["Draw the image more creatively.", "Follow the prompt closer", "set guidance strength to 10"],
        slots=[
            Slot(
                definition = "Guidance strength.",
                examples = [""],
                type = "int"                
            )
        ]
    )
    
    print(str(intent_redraw_guidance_strength))

        
