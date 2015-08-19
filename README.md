# FFRankings
Flask App for ELO Fantasy Rankings



1. Download the repo

2. cd into it

3. `$virtualenv venv`

4. `$ source venv/bin/activate`

5. Make sure postgres is installed

6. `$ pip install -r requirements.txt`

7. `$ python ffrankings_app.py`

8. Navigate to http://localhost:5000/ in browser.



To populate the db, you can do:

   `$ python populate-db.py`
   
WARNING: this will wipe out anything currently in the db.