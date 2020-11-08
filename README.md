# Python audio synthesis

This is a project to learn a bit about Python and a bit about music synthesis with Python.


## Introducing Pyo

Take a look at 5 mins of [this YouTube video](https://www.youtube.com/watch?v=ROlkhVs15AM&t=1m20s) to see a demo of the Pyo python module from Ajax Sound Studio.

The video is from [a presentation by Dror Ayalon](https://2017.pygotham.org/talks/music-synthesis-in-python/) at the PyGotham event in 2017.


Let's have a go at that :)


## Setup your git project

Fork my project on githhub so you can have your own copy to check in your scripts to.

```
git clone <your fork>
cd <directory>
```

Add and edit your own script files

When you want to commit to github:
```
git add .
git commit -m 'message'
git push
```
(... and you can do those 3 steps easily in VSCode)


Make your own markdown file to keep notes... or edit the original README.md.


## Getting set up to use Pyo

1. Use Python 3
2. Create and enter a virtualenv
3. Install the pyo module in the virtualenv
    - Note: On Windows, I was unable to successfully install any version of pyo later than 1.0.1.
4. Run a couple of diagnostic scripts to see how pyo sees our audio environment.
    - See the link below about configuring audio for Pyo on Windows.
5. Later, when we're making sounds, let's try using different audio interfaces.

## Start to play with pyo

Take a look at the code [examples](./examples)

Make your own scripts. Commit and push them to your github repo.


## Useful links

### Python

Creating a virtual environment: https://docs.python.org/3/tutorial/venv.html


### Pyo: Ajax Sound Studio

About Pyo: http://ajaxsoundstudio.com/software/pyo/

Pyo Developer docs: http://ajaxsoundstudio.com/pyodoc/

Debugging and configuring audio for Pyo on Windows: http://ajaxsoundstudio.com/pyodoc/winaudioinspect.html

The git repo of Pyo: https://github.com/belangeo/pyo

A git repo with the content of video presentation: https://github.com/dodiku/music-synthesis-with-python


### Might be interesting for further exploration

https://github.com/belangeo/pyo-tools

https://wiki.wxpython.org/FrontPage

