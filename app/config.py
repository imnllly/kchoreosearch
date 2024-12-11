SECRET_KEY = "your_secret_key"
SECRET_CODE = "2577c72d87c6b9e56ad75e8718431934"
DATABASE_LOGIN = "postgres"
DATABASE_PASSWORD = "147896313"
filter_groups = [
    {
        "title": "gender",
        "translate_title": "группы",
        "filters": [
            {
                "name": "BOY GROUP",
                "translate": "МУЖСКАЯ ГРУППА",
                "code": 'male'
            },
            {
                "name": "GIRL GROUP",
                "translate": "ЖЕНСКАЯ ГРУППА",
                "code": 'female'
            },
            { 
                "name": "SWITCH GROUP",
                "translate": "СОВМЕСТНАЯ ГРУППА",
                "code": 'switch'
            }
        ]
    },
    {
        "title": "number",
        "translate_title": "кол-во участников",
        "filters": [
            {
                "name": "1 MEMBER",
                "translate": "1 УЧАСТНИК",
                "code": 'members_1'
            },
            {
                "name": "2 MEMBERS",
                "translate": "2 УЧАСТНИКА",
                "code": 'members_2'
            },
            {
                "name": "3 MEMBERS",
                "translate": "3 УЧАСТНИКА",
                "code": 'members_3'
            },
            {
                "name": "4 MEMBERS",
                "translate": "4 УЧАСТНИКА",
                "code": 'members_4'
            },
            {
                "name": "5 MEMBERS",
                "translate": "5 УЧАСТНИКОВ",
                "code": 'members_5'
            },
            {
                "name": "6 MEMBERS",
                "translate": "6 УЧАСТНИКОВ",
                "code": 'members_6'
            },
            {
                "name": "7 MEMBERS",
                "translate": "7 УЧАСТНИКОВ",
                "code": 'members_7'
            },
        ]
    }
]