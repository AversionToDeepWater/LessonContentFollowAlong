file = open('C:\\Users\\imana\\PycharmProjects\\LessonContentFollowAlong\\PythonLesson7\\ReadingFiles\\text.txt','r')
#When entering file paths, need to use a double backslash and not a single one
#This is as this can be a problem as / + a letter be a special character that will print things differently
# e.g. /n in a print statement will print the next part on a new line

#print(file)

content = file.read()
#print(content)

ask_user =  input("Do you have a new item for your 'To DO List?' ")

if ask_user.lower() == 'y' or ask_user.lower() == 'yes':
    print("Here is your current list /n", content )
    new_item = input("Please enter a new item for your 'To Do' List: ")
    update_file = open('C:\\Users\\imana\\PycharmProjects\\LessonContentFollowAlong\\PythonLesson7\\ReadingFiles\\text.txt', 'a+')
    new_list = update_file.write(new_item)
    update_file.close()
    new_file = update_file.write()
    print(new_file)
else:
    print("Okay! Here is your current list /n", content)
