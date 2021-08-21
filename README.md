# regresspy

`regresspy` is a python module for carrying out simple regressions using gradient descent algorithm. However, the library is half complete. Your task is to fill in the necessary codes. The tasks of the project is given below:

- First, I Forked the repository from main branch of the file. 
- Then I cloned this repository in my desktop from the `.vscode` terminal.
- Then I changed the directory of regresspy. Input my mail address and username from my github id. Created a new branch using my username.
- Git add . using this command and all the file added in this branch and finally git push of this branch. 
- Filled  `.gitignore` file by creating one for Python from [.gitignore.io](https://www.toptal.com/developers/gitignore).
- Then write the codes for the mean absolute, sum of squared, mean squared, and root mean squared errors in the `loss.py` file and run this file from `.vscode` terminal.
- After that I changed the `test_loss.py` file and made some functions (test_mase, test_rmse, test_sse). 
- After that, I go to the `gradient_descent.py` file. It contains two functions named `forward` for computing forward propagation and `backward` for computing the gradients. The second one is already done by my course teacher. I just changed the forward function and run this function from terminal.
- Then went to the `main.py` file where the actual training will take place. The first task was to completed the `_initialize_weights` function. Then completed the `_train` function. Finally, completed the `predict` and `score` function.
- After that went to the `model.py` file in the `test` folder. Here, will perform two regressions. First one was carried out using the `SGDRegressor` from the `sklearn` library. Second one was carried out using my own codes. And got SGDRegressor rmse value, where the value is 0.5281799012303121. I estimated regression value through regression function from regression.py file and set epoch/iteration 100 and also learning rate was 0.001. I trained X, Y through fit function from regression file of the regression value. I predicted regression value through predict function from regression.py file. I calculated score of regression rmse through score function from regression.py file. Finally got RMSE value=1.0566434435967054.
- Then I Filled the `requirements.txt` file according to the libraries Which I used in my codes.
- Then Filled the `setup.py` file to install my code as a library which was import find_namespace_packages and setup. In this function I mentioned project name, author, mail address, version, description, all packages and requirement libraries.
- Finally add all the files in my branch on github using (git add .), left comment was "All the files "updated" using (git commit - m "") this command and push all files.