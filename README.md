# AI Study Planner

A beginner-friendly study planner made with basic Python. It asks about your learning goal and weekly availability, calculates your total weekly study hours, creates a simple personalized schedule, and saves it to a text file.

> This project does not use an AI API. It uses simple Python rules to personalize the plan.

## Features

- Collects the student's name and learning goal
- Asks for study days per week and hours per study day
- Calculates total weekly study hours
- Creates a weekly study schedule
- Saves the plan as `study_plan.txt`
- Validates basic user input
- Uses only Python's standard library

## Requirements

- Python 3.8 or newer
- No external packages required

## How to run

1. Download or clone this repository.
2. Open a terminal in the project folder.
3. Run:

   ```bash
   python main.py
   ```

   On some systems, use `python3 main.py`.

4. Answer the questions. Your plan will appear in the terminal and be saved as `study_plan.txt` in the current folder.

## Project files

- `main.py` — the study planner program
- `study_plan.txt` — generated after the program runs
- `README.md` — project instructions

## Publish on GitHub

1. Sign in at [GitHub](https://github.com/).
2. Create a new repository named `ai-study-planner`.
3. Keep it public if you want others to see your project.
4. Upload `main.py` and `README.md` using **Add file → Upload files**, then commit the changes.

Alternatively, if Git is installed, open a terminal in this folder and run:

```bash
git init
git add main.py README.md
git commit -m "Add beginner-friendly AI study planner"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/ai-study-planner.git
git push -u origin main
```

Replace `YOUR-USERNAME` with your GitHub username. If GitHub asks you to authenticate, follow its sign-in instructions.

## Example calculation

If a student studies 3 days per week for 2 hours each day:

`3 days × 2 hours = 6 study hours per week`

## License

You may add a license file if you want to specify how others can use or modify this project.
