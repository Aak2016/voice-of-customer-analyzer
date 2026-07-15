import json
import anthropic
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY from env (loaded via .env)

with open("feedback.txt", "r") as f:
    feedback_text = f.read()

schema = {
    "type": "object",
    "properties": {
        "themes": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "theme": {"type": "string"},
                    "sentiment": {
                        "type": "string",
                        "enum": ["positive", "negative", "neutral", "mixed"],
                    },
                    "action_item": {"type": "string"},
                },
                "required": ["theme", "sentiment", "action_item"],
                "additionalProperties": False,
            },
        },
    },
    "required": ["themes"],
    "additionalProperties": False,
}

response = client.messages.create(
    model="claude-haiku-4-5-20251001",
    max_tokens=2000,
    output_config={"format": {"type": "json_schema", "schema": schema}},
    messages=[{
        "role": "user",
        "content": (
            "Identify the top 3-5 themes in this customer feedback. "
            "For each theme, give its overall sentiment and one concrete "
            f"action item.\n\n{feedback_text}"
        ),
    }],
)

text = next(b.text for b in response.content if b.type == "text")
print(json.dumps(json.loads(text), indent=2))
