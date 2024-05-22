# Git: a hands-on course

This repository is meant to provide both slides and exercises to better understand and learn to use git.

## Presentation

The presentation is written in Markdown format and can be converted to a usable format (html, pdf, etc.) using [quarto](https://quarto.org).

For that you will need to:
- install `quarto`
- make sure you have [R](https://www.r-project.org/) with all the necessary dependencies. This can be achieved with conda `conda env create -f conda/presentation_env.yaml`
- Install quarto extensions in `presentation` folder:
    - `quarto install extension andrie/reveal-auto-agenda`
    - `quarto install extension grantmcdermott/quarto-revealjs-clean`
    - `quarto add reuning/codefocus`

Viewing the slides can then be simply achieved with
```
conda activate quarto_r
quarto preview presentation/presentation.qmd
```
which will open a browser window displaying the slides.

To get the `html` file of the presentation you can instead run
```
conda activate quarto_r
quarto preview presentation/presentation.qmd --render revealjs
```
and if you want to have a self contained version of the presentation, you will need the copy the following files and folders:

```
presentation/presentation.html
presentation/presentation_files
presentation/figures
```

## Resources

- [Pro Git](https://git-scm.com/book): great reference book for everything git. Many of the figures from the presentation come from its [git repository](https://github.com/progit/progit2).
