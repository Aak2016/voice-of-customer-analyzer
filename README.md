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

- How to use a JSON schema to force an AI model's output into a reliable, predictable format instead of unpredictable free text.
- How to keep API keys out of source code (and out of version control) using a `.env` file.
- The practical difference between a general-purpose model and a faster, lighter one for a simple summarization task.
