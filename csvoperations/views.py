import csv
from django.shortcuts import render
from .forms import StudentRegistration , StudentSearch
from django.contrib.staticfiles.storage import staticfiles_storage


# Create your views here.
def index(request):
  return render(request,'csvoperations/index.html')


def add_student(request):
  fm = StudentRegistration(request.POST)
  if fm.is_valid():
    with open('csvoperations/static/csv/students.csv',"a",newline='') as f:
      w=csv.writer(f)
      w.writerow([
        fm.cleaned_data['id'], fm.cleaned_data['name'], fm.cleaned_data['gender'],
        fm.cleaned_data['date_of_birth'], fm.cleaned_data['city'], fm.cleaned_data['state'],
        fm.cleaned_data['email'], fm.cleaned_data['qualification'], fm.cleaned_data['stream']
      ])
      return render(request,'csvoperations/add-student.html',{'fm':fm, 'done':'Successfully Added'})
  else:
    fm = StudentRegistration()
  return render(request,'csvoperations/add-student.html',{'fm':fm})


def display_all_student(request):
  row_data=[]
  with open('csvoperations/static/csv/students.csv','r') as f: 
    r=csv.reader(f)
    data=list(r)
    for line in data:
      col_data=[]
      for word in line:
        col_data.append(word)
      row_data.append(col_data)
      print()
    print(row_data)
  return render(request,'csvoperations/display-all-student.html',{'student_data':row_data})


def search_student(request):
  search = StudentSearch(request.GET)
  if search.is_valid():
    row = []
    dict = {}
    label = ['Student Id','Student Name','Gender','Date of Birth','City','State','Email Id','Qualification','Stream']
    with open('csvoperations/static/csv/students.csv','r') as f: 
      r=csv.reader(f)
      data=list(r)
      #print(data)
      flag = False
      for line in data:
        for word in line:
          if(word == str(search.cleaned_data['search'])):
            flag = True
        if(flag == True):
          for word in line:
            row.append(word)
          flag = False
          for i in range(len(label)):
            dict[label[i]] = row[i]
    print(dict)
    return render(request,'csvoperations/search-student.html',{'search':search,'row':row, 'dict':dict})
  else:
    search = StudentSearch()
  return render(request,'csvoperations/search-student.html',{'search':search})