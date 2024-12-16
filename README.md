# Amazon-Price-Tracker
A exam project for "Programmieren in Python". It shows the prices and its development of a specific product.

## Setup

### Django

You need to setup a virtual enviroment for the developing with Python and Django.

- [Virtual enviroment](https://docs.python.org/3/tutorial/venv.html)
- [Install Django](https://docs.djangoproject.com/en/5.1/topics/install/)
- [Install important packges in your virtual environment]

#### Templating in Django

In Django we use HTML templates to render content on the viewport! 

Visit the [official documentation](https://docs.djangoproject.com/en/5.1/topics/templates/) for more information!

### GitHub

#### Pull the repo to your local machine

If you want to pull the latest version of the repository to your local machine and start coding with it, you need to pull it from GitHub using `Git`.

Please refer [here](https://git-scm.com/downloads) if you haven't installed it already!

To check if you it setup on your PC:
```bash
  git -v
```
... output should be:
> git version 2.47.1

After making sure you have `Git` installed, you can pull the repository to a folder of your liking. Open a terminal in that directory and enter the following command into your command line:
```bash
  git clone https://github.com/M4tt1-Coder/Amazon-Price-Tracker.git
```

The repo is now installed and ready to go but you need to install all Python packages to start developing.

#### Merge a branch into another

To have your personal branch up-to-date with the `main`-branch you need to merge it into your own!

First switch to the `main`-branch:
```bash
  git checkout main
```
Then pull possible commits from the remote branch:

```bash
  git pull
```
Now, switch back to your branch:

```bash
  git checkout <nameOfYourBranch>
```
... merge the changes made in `main` into yours:

```bash
  git merge main
```
There is a chances that you encounter a merge conflict. In that case please visit [this](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/addressing-merge-conflicts/resolving-a-merge-conflict-using-the-command-line) site to learn more how to resolve the problem!

All important changes are now in the branch you work in!

#### Create a Pull Request

If you are ready with you features, then you can create [Pull Request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests) to merge your changes into the default branch.

On the first landing page, there is a section called **`Pull requests`**:

![The main landing page](./readme_assets/pr_on_landing_page.png)

Click on the tag `Pull requests`!

Now you get to a page, where all open pull requests are listed!

![All listed pull requests & create new pull requests](./readme_assets/new_pr.png)

Next, click on the button `New pull request`!

![Choose a branch where to merge from](./readme_assets/choose_branch.png)

So, here you need to select a branch to compare changes with! Click on the same button / field as marked in the image!

Click on `Create pull request` to continue!

![Select a branch to compare changes with](./readme_assets/create_pr_1.png)

You will get to a new page, where you can add a title and description to your pull request! I recommend doing that, because it allows your team members to understand, why you did what you did!

![Add title and description to your pull request](./readme_assets//create_pr_2.png)

After adding your text, click on `Create pull request`!

You will see something like this! Now you have created a new pull request, I will review the new pull request and possibly merge it into the main branch!

![Summary of the pull request 1](./readme_assets/final_info_page.png)
![Summary of the pull request 2](./readme_assets/final_info_page-2.png)

## How to run the app?

###  Running the Django Server

Please refer to the docs for more information about running the Django server [`here`](https://docs.djangoproject.com/en/5.1/intro/tutorial01/)

To start the server, go the "Amazon-Price-Tracker" folder, open a terminal and type:
```bash
  python manage.py runserver
```
... into the command line.

You should see something like this: 

> December 10, 2024 - 19:27:22
> Django version 5.1.4, using settings 'amazon_price_Tracker.settings'
> Starting development server at http://127.0.0.1:8000/
> Quit the server with CONTROL-C. 

Watch this [video](https://www.youtube.com/watch?v=nGIg40xs9e4) for a brief introduction into Django!

## Tasks for Everyone

- frontend UI development (Matthis)
  - display some charts (matplotlib) (Thomas)
- API endpoints for fetching data from an Amazon API (Simon)
- convert / work with the incoming data -> filter out important data to us (Jannis, Max) -> store data in exel file
- write simple html files (everyone) -> I will possibly assign some ideas to everyone

- link a tutorial for templating in Django