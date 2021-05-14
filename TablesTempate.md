Tables:
    User Info
        User_id primary id
        First name
        Last name
        Username
        Hashed password
        isAdmin
    Assesment Info
        User_id foreign key composite primary key
        Assesment_time foreign key composite primary key
        Q1 
        Q1correct boolean
        Q2
        Q2correct boolean
        Q3
        Q3correct boolean
        Q4
        Q4correct boolean
        Q5
        Q5correct boolean
        Q6
        Q6correct boolean
        Q7
        Q7correct boolean
        Q8
        Q8correct boolean
        Q9
        Q9correct boolean
        Q10
        Q10correct boolean

    Quiz Data
        QuestionID primary key
        questionAns

    Site Data
        User_id foreign key
        Login_key primary key
        Dates
