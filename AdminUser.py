
import Question as ques

topic_dic = {}
username = "admin"
password = "1234"
test_taken_user_dic = {}


class AdminUser:

    def check_admin_login(self,username,password):
        if username == username and password == password:
            return True
        else:
            return False

    def add_question(self):
        for topic in topic_dic.keys():
            print(topic)

        topic = input("Enter a topic: ")

        temp_dic_diff_level = {}
        if topic_dic.keys().__contains__(topic):
            temp_dic_diff_level = topic_dic.get(topic)

        for diff_level in temp_dic_diff_level.keys():
            print(diff_level)

        difficulty_level = input("Enter difficulty level: ")

        temp_list_question = []
        if temp_dic_diff_level.keys().__contains__(difficulty_level):
            temp_list_question = temp_dic_diff_level.get(difficulty_level)


        num_question = int(input("Enter number of questions to take as input: "))

        for i in range(num_question):
            print ("Enter the question ")
            s = "Enter the question "+str(i+1)+". "
            q = input(s)
            c1 = input("Enter choice1: ")
            c2 = input("Enter choice2: ")
            c3 = input("Enter choice3: ")
            c4 = input("Enter choice4: ")
            ans = input("Enter the answer: ")

            question = ques.Question(q,c1,c2,c3,c4,ans)

            temp_list_question.append(question)
        temp_dic_diff_level[difficulty_level] = temp_list_question
        topic_dic[topic] = temp_dic_diff_level


    def take_test(self):
        print("Enter your details: ")
        name = input("Enter Your Name: ")
        email = input("Enter Your E-MailID: ")

        for topic in topic_dic.keys():
            print(topic)

        topic = input("Enter a topic from above: ")

        temp_dic_diff_level = {}
        if topic_dic.keys().__contains__(topic):
            temp_dic_diff_level = topic_dic.get(topic)

        for diff_level in temp_dic_diff_level.keys():
            print(diff_level)

        difficulty_level = input("Enter the difficulty level from above: ")

        temp_list_question = []
        if temp_dic_diff_level.keys().__contains__(difficulty_level):
            temp_list_question = temp_dic_diff_level.get(difficulty_level)

        print("Start the test: ")

        total_score = len(temp_list_question)
        total_question = len(temp_list_question)
        your_score = 0
        temp_name_score_dic = {}

        for i in range(total_question):
            print( str(i+1) + ". " + temp_list_question[i].question)
            print(temp_list_question[i].choice1)
            print(temp_list_question[i].choice2)
            print(temp_list_question[i].choice3)
            print(temp_list_question[i].choice4)

            ans = input()

            if temp_list_question[i].is_answer_correct(ans):
                your_score = your_score + 1


        temp_name_score_dic['name'] = name
        temp_name_score_dic['score'] = your_score
        temp_name_score_dic['total_score'] = total_score
        test_taken_user_dic[email] = temp_name_score_dic
        print("Email: "+email)
        print("Name: "+name)
        print("Total Score: "+str(total_score))
        print ("Your Score : "+str(your_score))
        print("correct answers: ")
        for i in range(total_question):
            print(str(i+1) +". "+temp_list_question[i].answer)


    def display_user_results(self):
        uname = input("Enter credentials: \nusername: ")
        pwd = input("password: ")
        if uname == username and pwd == password:
            for email in test_taken_user_dic.keys():
                print(" ")
                print ("Email: "+email)
                print ("Name: "+test_taken_user_dic.get(email)['name'])
                print ("Your Score: "+str(test_taken_user_dic.get(email)['score']))

    def display_particular_user_results(self, name, email):
        print ("Email: "+email)
        print ("Name: "+name)
        print ("Your Score: "+str(test_taken_user_dic.get(email)['score']))
