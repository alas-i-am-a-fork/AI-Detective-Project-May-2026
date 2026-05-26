# AI Detective Agent

# System Architecture
The project currently consists of two primary modules:
main.py
detectiveagent.py

## 1. main.py
* Initializes the LLM client
* Creates the DetectiveAgent object
* Handles user interaction
* Maintains interrogation flow
* Detects suspect switching
* Detects confessions
* Handles runtime errors
* Generates final case reports

## 2. detectiveagent.py
* Maintains conversation memory
* Sends prompts to the LLM
* Applies reasoning instructions
* Generates detective responses
  
conversation_history stores structured dialogue history for maintaining conversational context with the LLM.

Example:

[
    {"role": "system", "content": "..."},
    {"role": "user", "content": "..."},
    {"role": "assistant", "content": "..."}
]

# Methodology and Design Choices

## Conversational Reasoning Framework

The system uses an iterative conversational reasoning approach.

Instead of using a fixed decision tree, the detective dynamically adapts questioning based on:

* suspicious wording
* inconsistencies
* motive conflicts
* timeline contradictions
* emotional reactions
* evasiveness

This approach was chosen because murder investigations are inherently non-linear and depend heavily on contextual interpretation.

## LLLMs for Primary Reasoning

Initially, a cloud hosted model, Gemini were tested because of its strong instruction-following capabilities. However, the final implementation supports local models through Ollama due to limits on Gemini usage.

The Mistral model was selected due to:
* lightweight execution
* reasonable reasoning ability
* compatibility with Ollama
* fast inference speed

## Controlled Prompt Engineering

Ollama was observed to generate extra characters, make its own suspect dialogue and narrate scenes unnecessarily. To mitigate this, some prompting constraints had to be introduced, like restricting output length.

# Performance Metrics

Due to API limitations and instability encountered during testing with multiple LLM providers, a complete benchmark evaluation against the validation dataset could not be fully completed before submission. However, manual test cases were successfully executed.

## Observed Performance

### Successful Features

* Multi-turn interrogation
* Dynamic questioning
* Suspect switching
* Conversation memory
* Final report generation
* Error handling
* Contradiction-oriented questioning

### Known Limitations

* Smaller local models occasionally hallucinate new characters
* Long conversations may reduce reasoning consistency
* No deterministic contradiction engine yet
* Investigation reasoning is primarily LLM-driven

# Setup and Execution : MacOS and Linux

## 1. Install Python

# 2. Install Ollama

Download Ollama from:

https://ollama.com/download/mac for mac
https://ollama.com/download/linux for linux

# 3. Download the Mistral Model

ollama pull mistral

# 4. Install Python Dependencies
Inside the project directory: 

pip3 install openai

# 5. Start Ollama
Open a terminal:

ollama run mistral

and keep this terminal open.

# 6. Run the Project
Open another terminal in the project folder:

python3 main.py

# How To Use

1. Enter a case introduction
2. Enter suspect names manually
3. Enter suspect statements
4. The detective will generate follow-up questions
5. Continue interrogation until:

   * confession occurs
   * investigation is manually terminated
6. Final case report is automatically generated

# Future Improvements

Upgrades could be:
* structured JSON reasoning outputs
* automated contradiction engine
* evidence tracking database
* multi-agent interrogation

