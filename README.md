# END - TO - END DEPLOYMENT

1. cd Desktop 
2. mkdir create folder
3. python3 -m venv newvenv
4. source newvenv/bin/activate
5. git init
6. touch README.md   # Create File

7. git config --global user.name "Naveen"
8. git config --global user.email "mr.navi8680@gmail.com"

9.  git branch -M main -> Rename the branch to main
10. git remote add origin https://github.com/naveen-anandhan/ML_Ops.git  -> repo 
11. git remote -v


12. git add README.md             -> stage
13. git commit -m "1-st commit"   -> commit - stage name
14. git pull origin main --rebase -> to ensure the commit are applied on top of the latest commits.
15. git push -u origin main

16. git pull  -> To get fils from gitrepo


# Good Practice  - Outline
1.      setup.py              ->   
2.      requirements.txt      -> 

3.      scr/

         __init__.py 
         Loggers.py   -> to log all the execution to track     
         Exception.py  -> Custome Exception handelling will see 1.what file causing the error and 2.what line causing the error and 3.error!
         utils.py    -> EG: Save my model into cloud 

            Compoments/
                __init__.py
                Data_Ingersion.py  -> Importing data!
                Data_Transform.py  -> Transformation the Data!
                Model_Trainer.Py   -> Specifically to Train the model
            Pipeline/
                __init__.py
                Train_Pipline.py
                Predict_Pipline.py
