USERS = {}
QUESTIONS = {}
INVITE_CODE = 1111

def addQuestion(userName: str, questionLink: str) -> int:
    if questionLink not in QUESTIONS:
        QUESTIONS[questionLink] = set()
    QUESTIONS[questionLink].add(userName)

    USERS[userName]['questions'].add(questionLink)

    return 1

def listQuestionStats(questionLink) -> []:
    if questionLink not in QUESTIONS:
        return []
    
    users = []
    for user in QUESTIONS[questionLink]:
        users.append(user)
    return users

def listUserStats(userName) -> []:
    if userName not in USERS:
        return []
    
    questions = []
    for user in USERS[userName]:
        questions.append(user["questions"])
    return questions

def listAllQuestions() -> []:
    questions = []
    for question in QUESTIONS:
        questions.append({"question": question, "users": listQuestionStats(question)})
    return questions

def listAllUsers(sort=False) -> []:
    users = []
    for user in USERS:
        users.append({"user": user, "questions": listUserStats(user)})
    if sort:
        users.sort(key=lambda x: len(x["questions"]), reverse=True)
    return users

def listQuestionsAccordingToMostSolved() -> []:
    questions = []
    for question in QUESTIONS:
        questions.append({"question": question, "users": listQuestionStats(question)})
    questions.sort(key=lambda x: len(x["users"]), reverse=True)
    return questions

def checkInviteCode(userName: str, password: str, inviteCode: int) -> int:
    global INVITE_CODE
    if inviteCode != INVITE_CODE:
        return 0
    
    INVITE_CODE += 1

    USERS[userName] = {
        "username": userName,
        "password": password,
        "questions": set()
    }
    
    return INVITE_CODE
        



