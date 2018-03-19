##  Student's Profile
student_name = input('What is your name?')
student_surename = input('What is your surname?')
student_group = input('What is your group?')
student_university = input('What is the name of your university?')
student_average_mark = input('What is your average mark?')
  print('Student file:' + student_name + ' ' + student_surename + ' ' + student_group + 'group' + ' ' + student_university + ' ' + 'average mark - ' + student_average_mark)
    First_Letter_Name = student_name[0:1]
      First_Letter_Surename = student_surename[0:1]
         Rest_Letter_Name = student_name[1:15]
           Rest_Letter_Surename = student_surename[1:15]
  print(student_university.upper(), First_Letter_Name.upper() + Rest_Letter_Name.lower(), First_Letter_Surename.upper() + Rest_Letter_Surename.lower())

  
print("I am {0} {1}, I am studying at the {2} University with {3}, my average mark is {4}.".format(student_name, student_surename, student_university, student_group, student_average_mark))
