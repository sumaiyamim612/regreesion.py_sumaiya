# regresspy

`regresspy` is a python module for carrying out simple regressions using gradient descent algorithm. However, the library is half complete. Your task is to fill in the necessary codes. The tasks of the project is given below:

- Fork this repository.
- Create a new branch using your username.
- Fill in the `.gitignore` file by creating one for Python from [.gitignore.io](https://www.toptal.com/developers/gitignore).
- **Commit frequently, usually everytime after changing or completing a function. Make the commit messages clear and complete.** You may read this [blog](https://chris.beams.io/posts/git-commit/) to learn about writing good commit messages.
- Write the codes for the mean absolute, sum of squared, mean squared, and root mean squared errors in the `loss.py` file.
- Complete the `test_loss.py` by filling in the codes to test above functions. An example for testing `mae` is already given. You may read [this](https://realpython.com/pytest-python-testing/) blog or any other to learn about `pytest`.
- After that, go to the `gradient_descent.py` file. It contains two functions named `forward` for computing forward propagation and `backward` for computing the gradients. The second one is already done for you. All you have to do is fill in the codes for forward propagation.
- Then go to the `main.py` file where the actual training will take place. The first task is to complete the `_initialize_weights` function. Then complete the `_train` function. Finally, complete the `predict` and `score` function.
- Now, go the `model.py` file in the `test` folder. Here, you will perform two regressions. First one will be carried out using the `SGDRegressor` from the `sklearn` library. Second one will be carried out using your own codes. Compare the results and write in the `README.md` file (You can delete this README file).
- Fill in the `requirements.txt` file according to the libraries you have used in your codes.
- Fill-in the `setup.py` file to install your code as a library. You may read [this](https://godatadriven.com/blog/a-practical-guide-to-using-setup-py/) blog or the Python documentation to learn how to prepare this file.
- Give an appropriate license to your library in the `LICENSE` file. You may use [choosealicense.com](https://choosealicense.com/) to select the best one according to your case.
- Try to make your code look beautiful. You can add optional documentation about how to use your library in the `README` file. Look for other repositories and see how they have documented.
- **Finally, email me the link of your repository.**