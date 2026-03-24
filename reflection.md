# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

  Answer: 
  - The game's answer was 44 but I guessed 37, 21, 13 and it said no each time and kept telling me to go lower. 
  - The left side panel when switched to hard shows 1-50 as possible choices instead of the true 1-100. 
  -pytest will fail because logic_utils.check_guess raises NotImplementedError

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

Answer: 

I used Gemini to assist with this project. One example that it gave me was immediately telling me that I was incorrectly trying to debug something and that it was already good to go. I also ended up using GitHub Copilot as a standalone to help me plan, with Copilot within codespaces being utilized to implement the steps.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

Answer: 

I manually ran the code and tested it before utilizing pytest to run "automatic" testing. I also ran the test_game_logic.py tests to see what errors populated during the testing process.
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

Answer: 

Rerun causes the script to restart each time you do anything. Session storage is where you store the information so that re-reading doesn't cause you to lose information/progress.


---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.


Answer: 

The project did not change the way I think about AI, but it did reinforce the need to always double check scripts. Something that it did change is how I will implement AI in the future, before this class I never utilized agents within my IDE...or even understood how easy they could be to implement. I have prior familiarity with Google Jules but that was all.