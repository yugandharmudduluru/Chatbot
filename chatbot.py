def chatbot():
    print(" Hello! Iam Iron Lady's Leadership Chatbot. Ask me about our programs!")

    faqs = {
        "programs": "Iron Lady offers leadership programs focused on confidence building, career growth, executive presence, and women’s leadership development.",
        "duration": "The program duration varies: some are short workshops (2-4 weeks), while flagship programs last 3-6 months.",
        "online": "Yes! Most programs are conducted online for flexibility. However, there are occasional offline events.",
        "certificates": "Yes, participants receive certificates upon successful completion of the program.",
        "mentors": "Our mentors and coaches are experienced leaders, certified trainers, and professionals from diverse industries."
    }

    while True:
        print("                                      ")
        print("1. What programs does Iron Lady offer?")
        print("2. What is the program duration?")
        print("3. Is the program online or offline?")
        print("4. Are certificates provided?")
        print("5. Who are the mentors/coaches?")
        print("6. Exit")
        
        user_input = input("Enter choice (1-6):")

        if user_input=="1":
            print("Bot:", faqs["programs"])
        elif user_input=="2":
            print("Bot:", faqs["duration"])
        elif user_input=="3":
            print("Bot:", faqs["online"])
        elif user_input=="4":
            print("Bot:", faqs["certificates"])
        elif user_input=="5":
            print("Bot:", faqs["mentors"])
        elif user_input=="6":
            print("Bot: Bye! Keep leading with confidence ")
            break
        else:
            print("Bot: Sorry, I don't have information about that. Please ask about programs, duration, online/offline, certificates, or mentors.")


chatbot()
