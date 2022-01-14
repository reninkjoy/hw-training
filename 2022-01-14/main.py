from datetime import datetime
import json
import os

task1=[]

class Employee:

    def __init__(self, emp_name, emp_id):
         self.emp_name = emp_name
         self.emp_id = emp_id

    def time(self):
         return datetime.now ().strftime("%Y-%m-%d %H:%M:%S")

    def task_title(self,task_title):
        return task_title

    def task_description(self,task_description):
        return task_description

    def end_task(self,task_success):
       return task_success

def json_write(name,val):

    with open(name+"/"+datetime.now().strftime("%Y-%m-%d %H:%M:%S")+name+'.json',"w") as fp:
            fp.write(json.dumps(json.loads(val),indent=4))

def login(name,emp,a):

    if a[name]==emp:
        print("\nLogin") 
        emp_details=Employee(name,emp)

        logtime=emp_details.time()

        while True:
               
            print("\nEnter the task_title")
            task_tit=str(input())

            print("\nEnter the task_description")
            task_dis=str(input())

            tasktime=emp_details.time()

            print("\nEnter the status(True/False")
            status=str(input())

            task={
                    'task_title':emp_details.task_title(task_tit),
                    'task_description':emp_details.task_description(task_dis),
                    'start_time':tasktime,
                    'end_time':emp_details.time(),
                    'task_sucess': emp_details.end_task(status),
            }
            task1.append(task)

            print("\nDo you want to add an task(yes/no)")
            fla=str(input())
            if fla!="yes":
                break

        details = {
                'name': emp_details.emp_name,
                'emp_id':emp_details.emp_id,
                'login_time': logtime,
                'logout_time':emp_details.time(),
                'task': task1
        }

        val=json.dumps(details)
        path=emp_details.emp_name+"/"
        isExist = os.path.exists(path)
        if not isExist:
            os.makedirs(path)
            json_write(name,val)
        else:
            json_write(name,val)

def information():
    with open('employee.json',"r") as f:
        a = json.loads(f.read()) 
    return a

def main():
    while True:
        try:
            while True:

                print("\n\nEnter the Employee id")
                emp=int(input())

                print("\nEnter the Employee name")
                name=str(input())

                info=information()   

                try:
                    login(name,emp,info) 
                    break
                except KeyError:
                    print("\nFail to connect\n\n") 
        except ValueError:
            print("\nFail to connect\n\n")     

if __name__=="__main__":
    main()
