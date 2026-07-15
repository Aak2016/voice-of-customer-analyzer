# Voice of Customer Analyzer

A small tool that reads raw customer feedback and automatically extracts the top themes, how customers feel about each one, and a concrete next step — as clean, structured data.

## The problem it solves

Customer feedback (reviews, support tickets, survey responses) piles up fast, and reading through it all to spot patterns is slow and easy to get wrong. This tool automates that first pass: instead of a person manually skimming pages of comments, it reads the feedback and returns a short, organized summary — the key themes, whether each one is positive or negative, and a suggested action — in seconds.

## How it works

The script sends the customer feedback to Claude (Anthropic's AI model) along with a strict template — called a JSON schema — that defines exactly what the response must look like: a list of themes, each with a sentiment (positive, negative, neutral, or mixed) and one action item. Because the model is required to fill in that template, the output is always predictable, structured data rather than free-form text that would need further cleanup. That structured output can then be fed directly into a spreadsheet, dashboard, or another program.

## How to run it

1. Install the one dependency:
   ```
   pip3 install python-dotenv
   ```
2. Make sure a `.env` file exists in this folder with your API key:
   ```
   ANTHROPIC_API_KEY=your-key-here
   ```
3. Put the feedback you want analyzed into `feedback.txt`.
4. Run the script:
   ```
   python3 analyze.py
   ```
5. The themes, sentiment, and action items print to the terminal as JSON.

## What I learned

- Prompt Engineering: Learned how small changes in prompts significantly impact output quality and consistency by iteratively refining prompts through multiple versions.
- Designing Reliable AI Workflows: Understood the importance of structured outputs (JSON schemas) to make LLM responses predictable and consumable by downstream systems, turning an AI prototype into a production-ready workflow.
- Prompt–Output Contracts: Learned to think of prompts as APIs, where the prompt guarantees a specific response structure that downstream components depend on, ensuring reliable orchestration.
- LLM Application Architecture: Gained hands-on understanding of the core building blocks of an AI application—from defining prompts and invoking the model to parsing and validating responses.
- Security Best Practices: Implemented secure API key management using environment variables (.env), version control exclusions (.gitignore), and experienced the importance of credential rotation after accidentally exposing a key.
- Cost Optimization: Learned to balance quality and cost by configuring spending limits, usage alerts, and evaluating different models based on performance versus inference cost.
- Model Selection: Explored trade-offs between different Claude models, understanding when a lightweight model is sufficient and when a more capable model is justified based on the use case.
- Human-in-the-Loop Systems: Experienced how human review fits into AI workflows, understanding why many production AI products require human approval before taking critical actions.
- AI Debugging & Iteration: Developed a structured approach to troubleshooting LLM applications by diagnosing context window issues, identifying model behavior problems, and iteratively resolving failures.
- Working with AI as a Development Partner: Built my first AI application by collaborating with Claude as a coding assistant, learning how to effectively guide, validate, and iterate with AI to accelerate development while maintaining ownership of product decisions.
