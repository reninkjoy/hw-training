from datetime import datetime
import json
import pymongo
from pymongo import MongoClient
import pprint

client = MongoClient()
db=client.Emplyee
result = db.login.create_index([('emp_id', pymongo.ASCENDING)],unique=True)
task1=[]

class Employee:

    def __init__(self,emp_name, emp_id):
        self.task = None
        self.log_in = None
        self.emp_name = emp_name
        self.emp_id = emp_id
        pprint.pprint(db.login.find_one({"emp_id": self.emp_id}))
        print("DuplicateKeyError")

    def login(self):
        # pprint.pprint(db.login.find_one({"emp_id": self.emp_id}))
        self.log_in = datetime.now().strftime("%Y-%m-%d %H:%M")
        return

    def logout(self):
        details = {
                'name': self.emp_name,
                'emp_id':self.emp_id,
                'login_time': self.log_in,
                'logout_time':datetime.now().strftime("%Y-%m-%d %H:%M"),
                'task': task1
        }
        try:
            post=db.login.insert_one(details)
            sorted(list(db.login.index_information()))

        except:
            print("DuplicateKeyError")

    def add_task(self,task_title , task_description):
        self.task={
        'task_title':task_title,
        'task_description':task_description,
        'start_time': datetime.now().strftime("%Y-%m-%d %H:%M"),
        }

    def end_task(self,task_success):
        self.task.update(end_time = datetime.now().strftime("%Y-%m-%d %H:%M"), task_status=task_success)
        task1.append(self.task)
        self.task=0
        return task1

    def show(self,show):
        pprint.pprint(db.login.find_one({"emp_id": show}))
