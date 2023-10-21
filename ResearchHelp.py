#Create a stack wherein you can store task for research and relevant research
import os
import json
import pickle
class ResearchInfo:
    def __init__(self, name, tasklist = ['None'], info = {}):
        self.tasklist = tasklist
        self.info = info
        self.name = name
    
    def nextTask(self):
        return self.tasklist[-1]
    
    def addTask(self):
        task = input("Enter Task")
        self.tasklist.append(task)
    
    def save_file(self):
        output_dir = os.path.join('~/Researchpy/','Projects',self.name)
        dataFile = os.path.join(output_dir,'data.json')
        taskfile = os.path.join(output_dir,'task.bin')
        if not os.path.exists(output_dir):
            os.mkdir(output_dir)

        jsonString = json.dumps(self.info)
        jsonFile = open(dataFile, "w")
        jsonFile.write(jsonString)
        jsonFile.close()
        
        binFile = open(taskfile,'wb')
        pickle.dump(self.tasklist,binFile)
        binFile.close()



def findprevproject():
    save_dir = os.path.join('~/Researchpy/','Projects')
    dirlist = os.listdir(save_dir)
    dirlist = [i for i in enumerate(dirlist)]
    for i in range(1,len(dirlist)+1):
        print("Enter {} for {}".format(i,dirlist[i-1][1]))
    choice = int(input("Enter Your Choice"))
    choice = dirlist(choice-1)[1]
    name = choice
    dir = os.path.join(save_dir,dirlist[i][1])
    dataFile = os.path.join(dir,'data.json')
    taskfile = os.path.join(dir,'task.bin')

    jsonFile = open(dataFile)
    info = json.load(jsonFile)
    jsonFile.close()

    binFile = open(taskfile,'w')
    tasklist = pickle.load(binFile)
    binFile.close()
    task = ResearchInfo(name, tasklist, info)
    return task

def main():
    Choice = input("Enter 1 for old Research and 2 for new")
    if Choice == 1:
        task = findprevproject()
    else:
        task = input("Name of Research Task")
        task = ResearchInfo(task)
    
    while True:
    
        Choice = input("Choose: \nEnter 1 for Create New Task\nEnter 2 to get the next Task\nEnter 3 to print info\nEnter 4 to exit")
        if Choice == '1':
            task.addTask()
        elif Choice == '2':
            task.nextTask()
            Choice = input("Enter 1 to accept task/n Enter 2 to change task")
        elif Choice=='3':
            task.giveinfo()
        elif Choice =='4':
            break
    
main()
