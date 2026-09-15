# AGENT.md

## Data practice folder
This folder is for beginner-friendly file and data work using simple CSV examples.

## Conventions
- Keep data examples easy to read and easy to run.
- Prefer plain Python tools such as the built-in `csv` module unless a task explicitly asks for a more advanced library.
- Use simple, explanatory variables and comments.
- Treat the CSV like a teaching dataset, not a large production dataset.

## Relevant file
- `ReefFish.csv` contains rows with columns such as `Site`, `Month`, `Transect`, `Species`, and `Abundance`.
- Typical beginner tasks here include counting rows, filtering by species, grouping by site, and summarizing abundance.

## Avoid
- Heavy data pipelines, notebooks, or large library dependencies.
- Over-engineered solutions when a short loop or dictionary is enough.
- Complex abstractions that hide the basic idea being taught.